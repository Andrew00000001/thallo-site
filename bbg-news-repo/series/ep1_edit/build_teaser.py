# Draft Oct 28 teaser: C1 window + B-1000 dub + HUD + captions + super + end card (episode1_package.md §4)
import json, subprocess, numpy as np, soundfile as sf, librosa, os
S='/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad'
E=f'{S}/ep1/edit'; A=f'{S}/ep1/audio/b1000'; CLIP=f'{S}/ep1/clips/C1_take1.mp4'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'; SR=48000
lines=[('b1000_c1_l1_b-one-thousand-live-scanning-location','B-1000. Live. Scanning location.'),
       ('b1000_c1_l2_hazard-crashed-dropship','Hazard: crashed dropship.'),
       ('b1000_c1_l3_status-still-crashed','Status: still crashed.'),
       ('b1000_c1_l4_launch-pad-destination','Launch pad destination:\nthe other crashed dropship.')]
def tighten(y, sr, max_gap=0.25, pad=0.03):
    m=y.mean(1); hop=int(0.01*sr); rms=librosa.feature.rms(y=m,frame_length=2*hop,hop_length=hop)[0]
    db=20*np.log10(rms+1e-9); on=db>db.max()-35
    chunks=[]; i=0
    while i<len(on):
        if on[i]:
            j=i
            while j<len(on) and on[j]: j+=1
            chunks.append([i*hop,j*hop]); i=j
        else: i+=1
    merged=[]
    for c in chunks:
        if merged and c[0]-merged[-1][1] < 0.12*sr: merged[-1][1]=c[1]
        else: merged.append(c)
    out=[]; p=int(pad*sr)
    for k,(a,b) in enumerate(merged):
        a=max(0,a-p); b=min(len(y),b+p)
        if k: out.append(np.zeros((min(int(max_gap*sr), merged[k][0]-merged[k-1][1]),y.shape[1])))
        out.append(y[a:b])
    return np.concatenate(out)
start=0.5; hold=0.32; t=start; vo=[]; caps=[]
for name,text in lines:
    y,sr=sf.read(f'{A}/{name}.flac',always_2d=True); assert sr==SR
    seg=tighten(y,sr,max_gap=0.16); caps.append((t,t+len(seg)/sr,text)); vo.append((t,seg)); t+=len(seg)/sr+hold
vo_end=caps[-1][1]; total=max(8.4, vo_end+0.6)
track=np.zeros((int((total)*SR)+SR,2))
for t0,seg in vo:
    i=int(t0*SR); track[i:i+len(seg)]+=seg
sf.write(f'{E}/vo_dry.wav',track[:int(total*SR)],SR,subtype='PCM_24')
# B-1000 post chain (draft): drive, bitcrush ~12 kHz sample-and-hold / 8-bit at ~55% wet, low cut
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'{E}/vo_dry.wav','-af','highpass=f=80,volume=3dB,asoftclip=type=tanh,acrusher=bits=8:samples=4:mix=0.55:mode=log:aa=0.5',f'{E}/vo_fx.wav'],check=True)
json.dump({'captions':caps,'vo_end':vo_end,'total':total},open(f'{E}/timing.json','w'),indent=1)
# captions as text files (avoids drawtext escaping)
dt=[]
for k,(a,b,text) in enumerate(caps):
    open(f'{E}/cap{k}.txt','w').write(text)
    dt.append(f"drawtext=fontfile={FONT}:textfile={E}/cap{k}.txt:fontsize=34:fontcolor=white:borderw=2:bordercolor=black@0.8:box=1:boxcolor=black@0.35:boxborderw=12:line_spacing=8:x=(w-text_w)/2:y=h*0.745:enable='between(t,{a:.2f},{b+0.25:.2f})'")
# HUD: LIVE label, 6-frame scan line, cyan corner brackets locking on the pad from 1.2 s
x0,y0,x1,y1=222,172,482,292; L=34; th=3; br=[]
for (bx,by,sx,sy) in [(x0,y0,1,1),(x1,y0,-1,1),(x0,y1,1,-1),(x1,y1,-1,-1)]:
    br.append(f"drawbox=x={bx if sx>0 else bx-L}:y={by if sy>0 else by-th}:w={L}:h={th}:color=0x46E6F0@0.95:t=fill:enable='gte(t,1.2)'")
    br.append(f"drawbox=x={bx if sx>0 else bx-th}:y={by if sy>0 else by-L}:w={th}:h={L}:color=0x46E6F0@0.95:t=fill:enable='gte(t,1.2)'")
hud=[f"drawtext=fontfile={FONT}:text='● LIVE':fontsize=34:fontcolor=0xFF3B3B:borderw=2:bordercolor=black@0.7:x=36:y=52",
     "drawbox=x=0:y='(t-0.15)/0.25*h':w=iw:h=4:color=0x46E6F0@0.7:t=fill:enable='between(t,0.15,0.40)'"]+br
vf=','.join([f"trim=0:8.4,setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop_duration={total-8.4:.3f},fps=24,scale=720:1280,setsar=1"]+hud+dt)
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',CLIP,'-i',f'{E}/vo_fx.wav','-filter_complex',f'[0:v]{vf}[v]','-map','[v]','-map','1:a','-t',f'{total:.3f}','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-c:a','pcm_s24le',f'{E}/seg1.mov'],check=True)
# super card 1.5 s with an original two-note sting
open(f'{E}/super1.txt','w').write('LOCAL HAZARDS'); open(f'{E}/super2.txt','w').write('NOV 4')
sting="aevalsrc='0.35*sin(2*PI*880*t)*exp(-6*t)*lt(t,0.18)+0.35*sin(2*PI*660*(t-0.18))*exp(-5*(t-0.18))*gte(t,0.18)':s=48000:d=1.5,aformat=channel_layouts=stereo"
subprocess.run(['ffmpeg','-y','-loglevel','error','-f','lavfi','-i','color=c=0x0E1626:s=720x1280:r=24:d=1.5','-f','lavfi','-i',sting,'-filter_complex',
  f"[0:v]drawtext=fontfile={FONT}:textfile={E}/super1.txt:fontsize=74:fontcolor=white:x=(w-text_w)/2:y=h*0.44,drawtext=fontfile={FONT}:textfile={E}/super2.txt:fontsize=56:fontcolor=0x46E6F0:x=(w-text_w)/2:y=h*0.52,drawbox=x=0:y='t/0.25*h':w=iw:h=4:color=0x46E6F0@0.8:t=fill:enable='lt(t,0.25)',setsar=1[v]",
  '-map','[v]','-map','1:a','-t','1.5','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-c:a','pcm_s24le',f'{E}/seg2.mov'],check=True)
# end card 2 s, silent
open(f'{E}/end.txt','w').write('Unofficial fan film, not affiliated\nwith SkyVu; characters © SkyVu.')
subprocess.run(['ffmpeg','-y','-loglevel','error','-f','lavfi','-i','color=c=black:s=720x1280:r=24:d=2','-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-filter_complex',
  f"[0:v]drawtext=fontfile={FONT}:textfile={E}/end.txt:fontsize=30:fontcolor=white:line_spacing=10:x=(w-text_w)/2:y=(h-text_h)/2,setsar=1[v]",
  '-map','[v]','-map','1:a','-t','2','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-c:a','pcm_s24le',f'{E}/seg3.mov'],check=True)
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'{E}/seg1.mov','-i',f'{E}/seg2.mov','-i',f'{E}/seg3.mov','-filter_complex',
  '[0:v][0:a][1:v][1:a][2:v][2:a]concat=n=3:v=1:a=1[v][a];[a]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[an]',
  '-map','[v]','-map','[an]','-c:v','libx264','-pix_fmt','yuv420p','-crf','20','-movflags','+faststart','-c:a','aac','-b:a','192k',f'{E}/teaser_draft_v1.mp4'],check=True)
print(json.dumps({'captions':[(round(a,2),round(b,2),t) for a,b,t in caps],'vo_end':round(vo_end,2),'c1_section':round(total,2)}))
