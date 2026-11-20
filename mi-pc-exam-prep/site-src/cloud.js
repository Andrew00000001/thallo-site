/* Runs the study app on its own website instead of inside Claude.

   Inside Claude the app asks the page's host for three services: a small document store, the id of the person using it,
   and permission to save. This file offers the same three under the same names, built on Firebase: Google sign-in for
   the id, and one Firestore document per person for the progress. Signing in stands in for "permission to save".
   The app's own saving code (read the account copy, combine, write, retry) then runs unchanged.

   The progress is stored as one JSON string, not as thousands of separate fields: Firestore indexes every field of a
   document, and a study record has more of them than its limits are comfortable with. */
(function(){
  'use strict';
  var fb = window.firebase, auth = null, fs = null, ok = false, denied = false, told = null, listeners = [];
  try{ if(fb && fb.apps && fb.apps.length){ auth = fb.auth(); fs = fb.firestore(); ok = true; } }catch(e){ ok = false; }
  // Talk to the database with ordinary short requests instead of one long-lived stream. A stream can stall without any
  // error on a phone (seen on an iPhone: signed in, then stuck on "connecting"); short requests either answer or fail.
  if(ok){ try{ fs.settings({experimentalForceLongPolling: true, experimentalAutoDetectLongPolling: false, merge: true}); }catch(e){} }

  // A read or write that gets no answer is cut off, and the connection is dropped and reopened so the next try starts
  // clean. The same reset runs when the page comes back from the background, where phones quietly close connections.
  var kicking = null, hiddenAt = 0;
  function kick(){
    if(!ok) return Promise.resolve();
    if(!kicking) kicking = fs.disableNetwork().then(function(){ return fs.enableNetwork(); }).catch(function(){}).then(function(){ kicking = null; });
    return kicking;
  }
  function timed(make, ms){
    return (kicking || Promise.resolve()).then(function(){
      return new Promise(function(res, rej){
        var t = setTimeout(function(){ kick(); rej({code:'unavailable', cause:'no answer'}); }, ms);
        make().then(function(v){ clearTimeout(t); res(v); }, function(e){ clearTimeout(t); rej(mapErr(e)); });
      });
    });
  }
  document.addEventListener('visibilitychange', function(){
    if(document.visibilityState === 'hidden') hiddenAt = Date.now();
    else if(hiddenAt && Date.now() - hiddenAt > 3000){ hiddenAt = 0; kick(); }
  });

  function current(){ return ok ? auth.currentUser : null; }
  function tell(){ var u = current(), id = u ? u.uid : null; if(id === told) return; told = id; denied = false; listeners.slice().forEach(function(f){ try{ f(u); }catch(e){} }); }

  // resolves once Firebase has said whether someone is signed in on this device (or after 10 s without an answer)
  var ready = new Promise(function(res){
    if(!ok){ res(); return; }
    var first = true, t = setTimeout(function(){ if(first){ first = false; told = current() ? current().uid : null; res(); } }, 10000);
    auth.onAuthStateChanged(function(){
      if(first){ first = false; clearTimeout(t); told = current() ? current().uid : null; res(); }
      else tell();
    }, function(){ if(first){ first = false; clearTimeout(t); res(); } });
  });

  // Firestore's error names, in the words the app's saving code already understands
  function mapErr(e){
    var c = String((e && e.code) || '').replace(/^firestore\//, '');
    if(c === 'permission-denied' || c === 'unauthenticated'){ if(current()) denied = true; return {code:'not_granted', cause:c}; }
    if(c === 'resource-exhausted') return {code:'resource_exhausted', cause:c};
    if(c === 'invalid-argument' || c === 'out-of-range') return {code:'transform_error', cause:c};
    return {code:'unavailable', cause:c};
  }
  function wrap(snap){
    return { exists: !!snap.exists, metadata: snap.metadata || {},
      data: function(){ var d = snap.data(); if(!d) return null; if(typeof d.json === 'string'){ try{ return JSON.parse(d.json); }catch(e){ return {}; } } return d; } };
  }
  var db = {
    doc: function(path){
      var id = String(path).split('/')[2];                 // the app asks for data/users/<id>/progress
      if(!id) throw {code:'invalid_argument'};
      var r = fs.collection('progress').doc(id);
      return {
        get: function(){ return timed(function(){ return r.get(); }, 9000).then(wrap); },
        set: function(body){ return timed(function(){ return r.set({json: JSON.stringify(body), updated: +body.updated || Date.now(), v: 1}); }, 15000).then(function(){ denied = false; }); },
        onSnapshot: function(next, fail){ return r.onSnapshot(function(s){ next(wrap(s)); }, function(e){ if(fail) fail(mapErr(e)); }); }
      };
    }
  };

  function provider(){ var p = new fb.auth.GoogleAuthProvider(); p.setCustomParameters({prompt:'select_account'}); return p; }
  function signIn(){
    if(!ok) return Promise.reject({code:'unavailable'});
    return auth.signInWithPopup(provider()).then(function(){ tell(); }, function(e){
      var c = e && e.code;
      if(c === 'auth/popup-closed-by-user' || c === 'auth/cancelled-popup-request' || c === 'auth/user-cancelled') return;        // changed their mind
      if(c === 'auth/popup-blocked' || c === 'auth/operation-not-supported-in-this-environment') return auth.signInWithRedirect(provider());   // the page reloads signed in
      throw e;
    });
  }
  function signOut(){ return ok ? auth.signOut().then(tell, tell) : Promise.resolve(); }

  var user = { id: function(){ return ready.then(function(){ var u = current(); return u ? u.uid : null; }); } };
  var permissions = {
    state: function(){ return ready.then(function(){ return !ok ? '' : !current() ? 'prompt' : denied ? 'denied' : 'granted'; }); },
    request: function(){ return signIn(); },
    manage: function(){ return signOut().then(signIn); }       // "use a different account"
  };

  window.claude = {
    use: function(name){ return Promise.resolve(name === 'db' ? (ok ? db : null) : name === 'user' ? user : name === 'permissions' ? permissions : null); },
    // only present on the stand-alone site: who is signed in, and the sign-in and sign-out buttons' actions
    site: {
      ok: ok,
      who: function(){ var u = current(); return u ? {name: u.displayName || '', email: u.email || ''} : null; },
      signIn: signIn, signOut: signOut,
      onChange: function(f){ listeners.push(f); }
    }
  };
})();
