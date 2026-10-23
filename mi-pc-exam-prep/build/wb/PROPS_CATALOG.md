# Sketch prop catalog

Use these names as `"p"` in drawing elements. Size: give `h` (or `w`) in canvas units; `dh` is the default height.
Look at the picture sheets in `S/wb/catalog/` to see each prop. Any Lucide icon is also available as `{"p":"icon","name":"..."}`.

## business (33 props; pictures: catalog/business-*.png)

| prop | aspect w:h, default h | notes and options |
|---|---|---|
| `gavel` | 72:60, 10 | gavel: judge's gavel over its sound block. o.block (default true), o.strike (impact lines: the ruling lands) |
| `scale` | 92:80, 18 | scale: scales of justice. o.tilt: -1 (left pan lower/heavier), 0 (balanced, default), 1 (right pan lower); o.left / o.right: prop name resting in that pan (e.g. 'money', 'house'), o.leftOpt / o.rightOpt |
| `handshake` | 100:58, 10 | handshake: two hands shaking (deal, agreement, contract). o.left / o.right: sleeve colors (default 'blue' / 'gray') |
| `certificate` | 86:66, 14 | certificate: framed certificate / license with a ribbon seal. o.title (default 'CERTIFICATE'), o.frame (default true; false = loose document), o.seal (seal color, default 'red'), o.name (optional line of text under the title) |
| `idcard` | 72:46, 8 | idcard: license / ID card with a photo. o.title (header text, default 'LICENSE'), o.color (header band, default 'blue') |
| `badge` | 50:54, 8 | badge: police / license badge. o.star (6-point sheriff star instead of a shield), o.text (short word in the center, e.g. 'POLICE'), o.color (metal, default 'yellow') |
| `magnifier` | 60:60, 10 | magnifier: magnifying glass, handle to the lower right. o.inside (prop name seen in the lens, e.g. 'house'), o.insideOpt, o.color (handle, default 'brown') |
| `cashregister` | 86:74, 14 | cashregister: shop cash register. o.open (cash drawer out, bills showing), o.amount (display text, default '$12'), o.color (body, default 'teal') |
| `oven` | 96:86, 22 | oven: brick pizza oven. o.fire (flames in the mouth, smoke from the chimney), o.pizza (a pizza sitting in the mouth) |
| `pizza` | 60:60, 10 | pizza: whole pizza, top view, cut in 6 slices. o.slice (one slice instead), o.missing (slices eaten, 0-5), o.cut (slice lines, default true) |
| `cart` | 86:72, 14 | cart: shopping cart, faces right. o.full (groceries in the basket), o.color (basket tint) |
| `parcel` | |  |
| `pallet` | 92:74, 16 | pallet: boxes stacked on a wooden shipping pallet. o.n (box layers 1-3, default 3), o.wrap (plastic stretch-wrap lines) |
| `firstaid` | 64:54, 10 | firstaid: first aid kit (case with a white cross). o.color (case, default 'red') |
| `crutches` | 52:100, 20 |  |
| `wheelchair` | 66:86, 18 | wheelchair: side view, facing right. o.who (cast name of a person seated in it, e.g. 'grandma'), o.mood, o.color (seat, default 'blue') |
| `hospitalbed` | 114:72, 16 | hospitalbed: hospital bed, side view, head at the left. o.patient (head on the pillow, blanket over the body), o.iv (IV drip stand), o.color (blanket, default 'sky') |
| `pills` | 52:58, 8 | pills: prescription pill bottle with loose capsules. o.spill (default true), o.color (bottle, default 'orange') |
| `stethoscope` | 62:66, 10 | stethoscope: doctor's stethoscope |
| `computer` | 86:70, 14 | computer: desktop monitor with keyboard and mouse. o.screen: 'lines' (default) / 'chart' / 'alert' (hacked: red warning) / 'lock' / 'off' |
| `server` | 52:98, 22 | server: server rack (data center, cyber). o.alert (red warning lights and a warning sign), o.n (units, default 6) |
| `envelope` | 62:48, 8 | envelope: letter envelope. o.open (flap up, letter peeking out), o.seal (red wax seal on the flap), o.color (paper tint) |
| `megaphone` | 72:52, 10 | megaphone: bullhorn facing right. o.waves (sound lines, default true), o.color (default 'red') |
| `sign` | 72:86, 20 | sign: signboard on a post. o.text (a short word or two; '\n' for a second line), o.color (board border tint), o.tcolor (text color) |
| `folder` | 66:52, 10 | folder: manila file folder with papers. o.label (short text on the front), o.color (default 'yellow'), o.papers (default true) |
| `filecabinet` | 52:92, 20 | filecabinet: metal filing cabinet. o.n (drawers 2-4, default 4), o.open (top drawer pulled out with files), o.color (default 'gray') |
| `desk` | 120:80, 18 | desk: office desk (drawers on the left) with a computer. o.computer (default true), o.screen (passed to the computer), o.mug (default true), o.papers (paper stack) |
| `chair` | 52:82, 16 | chair: office swivel chair, front view. o.color (default 'blue') |
| `piggybank` | 82:66, 12 | piggybank: piggy bank facing right. o.coin (a coin dropping into the slot), o.color (default 'pink') |
| `wallet` | 66:48, 8 | wallet: leather wallet with cash sticking out. o.empty (no cash: open and empty), o.color (default 'brown') |
| `creditcard` | 64:42, 7 | creditcard: bank card with chip. o.color (default 'blue'), o.back (magnetic stripe side) |
| `receipt` | 40:82, 14 | receipt: long paper receipt with $ lines and a total. o.n (item lines 2-6, default 4), o.total (total text, default '$$$') |

## core (35 props; pictures: catalog/core-*.png)

| prop | aspect w:h, default h | notes and options |
|---|---|---|
| `person` | 44:100, 26 | a person (stick figure). opt: who (dana sam jen tony rosa kid adjuster judge thief worker doctor boss neighbor grandma regulator person), pose (stand wave point shrug cheer think hold sad run stop sit walk), mood (happy smirk sad worried angry shocked laugh neutral sleep), hold (a prop name held in the hand: money policy phone clipboard check ...), sign (short text on a sign they hold), plus look overrides: hair (short spiky curly bob long pony bun none), hairColor, shirt (color), hat (cap hardhat chef beanie top), glasses, beard, mustache, tie, badge, apron, vest, coat, robe, mask, stripes. Anchors: head (bubble tails), hand. |
| `house` | 100:92, 30 | house. opt: roof (color), wall (color), garage (true: attached garage on the right). Anchors: door, roof, chimney. |
| `shed` | 60:56, 16 | detached shed (other structure). opt: roof (color) |
| `store` | 120:90, 30 | shop with awning. opt: name (sign text), awning (color) |
| `insurer` | 100:96, 30 | the insurance company building. opt: name (default "INSURANCE CO.") |
| `office` | 70:100, 32 | office tower. opt: name |
| `factory` | 120:84, 28 | factory with chimney. opt: name |
| `apartment` | 80:110, 34 | apartment building |
| `car` | 120:56, 14 | car facing right. opt: color, dent (true) |
| `truck` | 130:66, 16 | box truck. opt: color |
| `semi` | 200:76, 20 | semi tractor-trailer. opt: color, trailer (color), name |
| `tree` | 70:100, 28 | tree |
| `fire` | 44:56, 12 | flames (add loop: "flicker") |
| `smoke` | 50:60, 14 | smoke blob |
| `cloud` | 80:46, 12 | cloud. opt: dark |
| `rain` | 80:80, 22 | rain cloud |
| `storm` | 80:84, 24 | storm cloud with lightning |
| `lightning` | 30:50, 12 | lightning bolt |
| `snow` | 40:40, 8 | snowflake |
| `sun` | 50:50, 12 | sun |
| `wind` | 70:40, 10 | wind gusts |
| `water` | 120:30, 8 | water waves strip (wide). opt: fill (false: no hatch) |
| `money` | 56:34, 9 | stack of bills |
| `bill` | 50:26, 7 | one dollar bill |
| `coins` | 40:34, 8 | coin stack |
| `moneybag` | 50:56, 14 | money bag |
| `policy` | 40:52, 16 | policy document. opt: title (header text, default POLICY), tsize, tcolor, sign (true: signature line signed) |
| `paper` | | same as policy |
| `clipboard` | 40:54, 15 | clipboard checklist |
| `bankcheck` | 60:28, 7 | bank check (paper check). opt: amount (text) |
| `calendar` | 44:44, 12 | calendar page. opt: n (big number or short text), label (month text on the red bar), size |
| `clock` | 44:44, 12 | clock. opt: h (hour), m (minute) |
| `shield` | 40:46, 12 | protection shield. opt: color, check (false hides the check mark), markColor |
| `umbrella` | 70:70, 18 | umbrella. opt: color |
| `phone` | 26:44, 10 | smartphone |

## home (33 props; pictures: catalog/home-*.png)

| prop | aspect w:h, default h | notes and options |
|---|---|---|
| `sofa` | 100:58, 12 | sofa: o.color (fabric hatch, default 'teal'), o.pillow (default true) |
| `tv` | 80:64, 11 | tv: flat screen on a stand. o.broken (cracked screen), o.off (dark screen), o.retro (old box TV with rabbit ears) |
| `laptop` | 80:56, 7 | laptop: open laptop, front view. o.broken (cracked screen), o.off (dark screen) |
| `diamondring` | | alias: the scene renderer treats p:'ring' as the circle-highlight primitive, so scenes must use 'diamondring' |
| `camera` | 72:52, 6 | camera: photo camera, front view. o.flash (default true: lit flash with sparkle lines) |
| `guitar` | 44:100, 15 | guitar: acoustic guitar, upright. o.color (body hatch, default 'orange') |
| `bicycle` | 120:74, 13 | bicycle: faces right. o.color (frame, default 'red') |
| `washer` | 60:70, 13 | washer: front-loading washing machine. o.hose (burst supply hose spraying water), o.color (body hatch, default none) |
| `waterheater` | 52:86, 18 | waterheater: tank water heater with hot/cold pipes. o.leak (drips, rust crack and a puddle) |
| `furnace` | 56:86, 17 | furnace: forced-air furnace with ductwork and a flame window. o.off (no flame), o.smoke (gray smoke from the top, e.g. malfunction) |
| `pipe` | 100:44, 7 | pipe: horizontal water pipe. o.burst (crack spraying water), o.frozen (icy pipe with icicles and frost) |
| `window` | 60:64, 14 | window: four-pane window with sill. o.broken (impact hole with cracks, shards on the sill) |
| `fence` | 120:52, 10 | fence: white picket fence. o.color (hatch the wood, e.g. 'brown'), o.broken (a missing and a leaning picket, snapped rail) |
| `pool` | 120:62, 14 | pool: in-ground pool with a ladder. o.float (default true: a ring float) |
| `trampoline` | 100:64, 12 | trampoline: round backyard trampoline. o.net (safety net with poles) |
| `grill` | 60:80, 14 | grill: kettle barbecue grill. o.color (default 'red'), o.smoke (default true), o.fire (flames out of the lid) |
| `mailbox` | 52:80, 14 | mailbox: rural mailbox on a post. o.color (box hatch, default 'blue'), o.flag (default true: red flag up), o.letters (letters sticking out) |
| `fridge` | 52:92, 24 | fridge: two-door refrigerator. o.spoiled (stink lines: food spoiled in a power outage), o.color (body hatch) |
| `painting` | 72:90, 18 | painting: framed landscape painting on an easel. o.wall (hanging on a nail, no easel) |
| `silverware` | 56:62, 8 | silverware: fork, knife and spoon. o.gold (gold instead of silver) |
| `lawnmower` | 100:70, 12 | lawnmower: push mower, faces right. o.color (deck, default 'red'), o.grass (default true: grass tufts) |
| `snowblower` | 104:74, 13 | snowblower: walk-behind snow blower, faces right, throwing snow. o.color (default 'orange') |
| `ladder` | 44:104, 26 | ladder: straight ladder. o.step (A-frame step ladder), o.color (rails, default 'orange') |
| `toolbox` | 70:52, 7 | toolbox: red metal toolbox with handle. o.color (default 'red'), o.open (no lid, tools sticking out) |
| `hammer` | 56:64, 8 | hammer: claw hammer, upright |
| `key` | 64:30, 4 | key: house key (brass) |
| `lock` | 44:58, 7 | lock: padlock. o.broken (shackle cut and sprung open, cracked body), o.open (unlocked, shackle lifted) |
| `safe` | 60:66, 12 | safe: steel safe with a dial. o.open (door swung open: cash and gold inside), o.empty (with o.open: nothing inside) |
| `briefcase` | 60:48, 7 | briefcase: leather briefcase. o.color (default 'brown') |
| `coffee` | 52:52, 5 | coffee: coffee mug. o.color (mug hatch, default 'red'), o.steam (default true) |
| `gift` | 52:56, 7 | gift: wrapped present with bow. o.color (paper, default 'red'), o.ribbon (default 'yellow') |
| `jewelry` | 64:56, 8 | jewelry: open jewelry box with a pearl necklace spilling out. o.necklace (just the necklace with a pendant) |

## places (28 props; pictures: catalog/places-*.png)

| prop | aspect w:h, default h | notes and options |
|---|---|---|
| `mobilehome` | 130:60, 16 | mobilehome: single-wide manufactured home on blocks. o.color: side stripe (default teal), o.wall: wall hatch color, o.roof, o.wheels: on wheels instead of blocks |
| `condo` | 140:84, 26 | condo: row of attached townhouse units. o.n: units (default 3), o.roofs: roof colors, cycled (default red, brown, blue) |
| `garage` | 80:70, 18 | garage: detached garage. o.open: door rolled up (dark inside), o.roof: roof color (default red) |
| `barn` | 90:86, 24 | barn: farm barn with gambrel roof, hayloft and X doors. o.color: wall color (default red) |
| `crops` | 120:56, 13 | crops: a row of crops on a strip of soil. o.type: 'corn' (default) / 'wheat', o.n: stalks (default 6), o.damaged: snapped, flattened and browned (hail, wind, drought) |
| `tractor` | 116:84, 18 | tractor: farm tractor facing right (big rear wheel). o.color: body (default green) |
| `warehouse` | 140:70, 22 | warehouse: long low warehouse with roll-up loading doors. o.name: sign text on the wall, o.n: loading doors (default 3), o.roof |
| `hospital` | 110:96, 30 | hospital: hospital with a red-cross sign tower and an entrance canopy. o.name: optional word on the canopy |
| `courthouse` | 120:100, 32 | courthouse: courthouse with pediment (scales of justice), six columns and wide steps. o.name (default "COURT") |
| `bank` | 100:96, 30 | bank: classic bank with green pediment, $ coin, columns and "BANK". o.name (default "BANK") |
| `school` | 130:100, 30 | school: school with bell tower, clock, flag and "SCHOOL" over the doors. o.name (default "SCHOOL") |
| `church` | 80:110, 34 | church: church with steeple and cross, rose window, arched door and pointed windows. o.roof (default red) |
| `restaurant` | 120:94, 30 | restaurant: restaurant with a name sign, scalloped awning and a plate-fork-knife window. o.name (default "DINER", e.g. "TONY'S PIZZA"), o.awning color (default red), o.signColor |
| `gasstation` | 130:80, 24 | gasstation: gas station with canopy, two pumps and a price sign. o.price (default "3.49"), o.color: canopy band (default red) |
| `construction` | 110:100, 30 | construction: building going up: steel frame, scaffolding with planks, traffic cone. o.crane: tower crane lowering a beam |
| `crane` | 100:110, 36 | crane: tower crane. o.load: 'beam' (default) / 'box' / 'none', o.color (default yellow) |
| `road` | 240:24, 7 | road: two-lane road strip, long and flat. o.center: 'dash' (default) / 'double' / 'none', o.pothole: a pothole in the near lane, o.crack |
| `bridge` | 160:64, 18 | bridge: suspension bridge over water (two towers, cables, hangers). o.color: towers (default red), o.water:false hides the water, o.broken: deck snapped in the middle |
| `dog` | 86:60, 12 | dog: side view dog facing right. o.mood: 'happy' (default, tongue out, wagging) / 'angry' (bares teeth, hackles up), o.color: fur (default brown) |
| `cat` | 50:64, 12 | cat: sitting cat, front view. o.color: fur (default orange), o.mood: 'angry' (hissing, ears back) |
| `deer` | 94:92, 19 | deer: Michigan whitetail, side view facing right. o.antlers:false = doe, o.pose: 'stand' (default) / 'leap' (jumping, e.g. into a car's path) |
| `cow` | 96:66, 14 | cow: Holstein dairy cow, side view facing right. o.spots: spot color (default ink) |
| `horse` | 100:88, 19 | horse: horse, side view facing right, with mane and tail. o.color: coat (default brown) |
| `bird` | 44:32, 6 | bird: small songbird, side view facing right. o.color: body (default blue), o.breast: breast color (e.g. 'orange' for a Michigan robin), o.fly: wings up in flight |
| `mouse` | 64:32, 7 | mouse: gray mouse (rodent), side view facing right, long tail |
| `bug` | 56:40, 7 | bug: insect (termite / ant), top view facing right. o.wings: termite swarmer wings, o.color: body (default brown) |
| `michigan` | 100:100, 30 | michigan: outline map of Michigan (Lower Peninsula mitten + Upper Peninsula). o.fill (default green), o.pin: city key (detroit, grandrapids, lansing, annarbor, kalamazoo, flint, traversecity, marquette, holland, saginaw, muskegon) or [lon,lat], o.pinLabel: text beside the pin (o.pinSize, default 7) |
| `lake` | 120:56, 14 | lake: lake with a wavy shoreline, waves, cattails and pines on the far shore. o.dock: small wooden dock, o.boat: little sailboat, o.trees:false hides the pines |

## symbols (40 props; pictures: catalog/symbols-*.png)

| prop | aspect w:h, default h | notes and options |
|---|---|---|
| `dice` | 84:58, 12 |  |
| `coin` | 54:52, 10 | coin: one big coin, slightly turned so its edge shows. o.sym (symbol on the face, default '$'), o.color (metal: 'yellow' gold (default), 'gray' silver, 'brown' copper) |
| `lottery` | 86:50, 10 | lottery: lottery ticket with a torn-off stub, a title and number balls. o.title (default 'LOTTO'), o.nums (up to 4 short strings, default ['7','21','3','9']), o.color (stub and balls, default 'orange') |
| `seesaw` | 100:56, 14 | seesaw: balance beam on a triangle pivot (trade-off, balance). o.tilt: -1 (left end down), 0 (level, default), 1 (right end down); o.left / o.right: prop name sitting on that end (e.g. 'person', 'money', 'house'), o.leftOpt / o.rightOpt, o.size (their height, default 22), o.color (pivot, default 'gray') |
| `piechart` | 60:60, 14 | piechart: pie chart. o.slices: list of percentages (default [50,30,20]), o.colors: slice colors (default cycles blue, orange, green, red, purple, teal, pink, yellow), o.pop: index of one slice pulled out of the pie |
| `barchart` | 70:60, 14 |  |
| `percent` | 52:52, 10 | percent: a big % sign in a ring (rates, interest, discount). o.color (ring, default 'green') |
| `stairs` | 80:64, 14 | stairs: steps rising to the right (growth, step by step, climbing the ladder). o.n (steps, default 4), o.color (default 'blue'), o.flag (goal flag on the top step), o.arrow (rising arrow above the steps) |
| `gears` | 66:62, 12 |  |
| `lightbulb` | 56:70, 14 | lightbulb: light bulb (idea, insight). o.off (unlit: no glow or rays), o.color (glow, default 'yellow') |
| `target` | 64:62, 14 | target: archery bullseye with an arrow stuck in it (goal, aim). o.arrow (default true), o.miss (arrow lands in the outer ring instead), o.color (rings, default 'red') |
| `trophy` | 60:66, 14 | trophy: winner's cup on a stand. o.color (metal, default 'yellow'; 'gray' = silver), o.text (short text on the cup instead of a star, e.g. '#1') |
| `medal` | 46:70, 14 | medal: medal on a two-colored ribbon. o.color (metal, default 'yellow'), o.ribbon ([left, right] colors, default ['blue','red']), o.n (short text on the medal instead of a star, e.g. '1') |
| `star` | 50:48, 10 | star: five-point star (rating, quality, favorite). o.color (default 'yellow'), o.empty (outline only, e.g. a missing rating star) |
| `heart` | 52:48, 10 |  |
| `crown` | 62:48, 10 | crown: king's crown (top choice, premium). o.color (default 'yellow') |
| `puzzle` | 56:56, 12 | puzzle: one jigsaw puzzle piece (fit, missing piece). o.color (default 'blue') |
| `brain` | 62:50, 12 | brain: brain, side view (thinking, knowledge, smart choice). o.color (default 'pink') |
| `eye` | 64:40, 8 | eye: an open eye (watch, notice, inspection). o.color (iris, default 'blue'), o.lashes (default true), o.closed (shut eye) |
| `magnet` | 66:56, 12 | magnet: horseshoe magnet, poles pointing right, with pull lines (attraction, drawing customers in). o.lines (pull lines, default true), o.color (default 'red') |
| `scissors` | 66:46, 10 | scissors: open scissors (cut costs, cancel). o.color (handles, default 'red') |
| `cycle` | 56:56, 12 |  |
| `warning` | 58:52, 12 | warning: warning triangle with '!' (risk, caution, hazard). o.color (default 'yellow') |
| `question` | 40:60, 12 | question: big question mark (unknown, uncertainty, "what if?"). o.color (default 'blue') |
| `exclaim` | 28:60, 12 | exclaim: big exclamation mark (important, alert, surprise). o.color (default 'red') |
| `thumbsup` | 54:62, 12 |  |
| `thumbsdown` | 54:62, 12 |  |
| `chain` | 112:36, 8 | chain: a row of chain links (connection, liability chain, weakest link). o.n (links, default 5), o.broken (the middle link snapped open), o.color (default 'gray') |
| `hourglass` | 44:66, 14 | hourglass: sand timer (time running out, deadline, waiting period). o.sand: share of sand still in the top bulb, 0-1 (default 0.5), o.color (frame, default 'brown') |
| `thermometer` | 34:76, 14 | thermometer: thermometer (heat, risk level, rising rates). o.level: 0-1 (default 0.7), o.color (liquid, default 'red'; 'blue' for cold) |
| `funnel` | 60:66, 14 | funnel: sales funnel with colored layers (narrowing down, filtering, conversion). o.layers (bands, 0-4, default 3), o.colors (band colors, default ['blue','teal','green','orange']), o.drops (dots falling out the spout, 0-3) |
| `globe` | 58:58, 12 |  |
| `boom` | 72:62, 14 |  |
| `crack` | 100:40, 10 | crack: crack splitting the ground (earthquake, sinkhole, foundation damage). o.shake (tremor marks above the ground, default true) |
| `tornado` | 60:80, 18 | tornado: twister funnel with spinning debris (windstorm). o.debris (default true), o.color (default 'gray') |
| `hail` | 80:88, 22 | hail: dark cloud dropping hailstones (hail damage). o.big (bigger stones) |
| `ice` | 110:46, 10 |  |
| `flood` | 200:44, 11 | flood: wide band of rising flood water with ripples; place it over the bottom of a house or street. o.debris (floating plank and ball), o.color (default 'blue') |
| `puff` | 46:64, 14 | puff: smoke puffs rising, small to large (smoke damage, gone up in smoke). o.n (3 or 4 puffs, default 4), o.color (default 'gray') |
| `sparkle` | 50:50, 10 |  |

## vehicles (25 props; pictures: catalog/vehicles-*.png)

| prop | aspect w:h, default h | notes and options |
|---|---|---|
| `motorcycle` | 100:64, 12 | motorcycle: street motorcycle, side view facing right. o.color: tank and tail (default red) |
| `atv` | 104:70, 13 | atv: four-wheeler (quad bike), side view facing right. o.color: fenders and body (default red) |
| `golfcart` | 96:84, 15 | golfcart: golf cart with canopy and a golf bag on the back, facing right. o.color: roof and seat (default green), o.body: body color (default white) |
| `snowmobile` | 120:62, 13 | snowmobile: snowmobile with front ski and rear track, facing right. o.color: body (default red), o.snow:false hides the snow spray and ground |
| `police` | 120:64, 15 | police: police car with red and blue light bar and POLICE on the door, facing right. o.color: body (default blue), o.lights:false = no flashing rays, o.text (default 'POLICE'), o.dent |
| `rental` | 120:84, 21 | rental: car with a big hanging "RENTAL" tag tied to its roof, facing right. o.color: car (default blue), o.text (default 'RENTAL'), o.tag: tag color (default yellow), o.dent |
| `van` | 120:64, 15 | van: minivan / passenger van facing right. o.color: body (default gray), o.cargo: windowless cargo van, o.name: business name on the side (implies cargo), o.dent |
| `pickup` | 130:60, 15 | pickup: pickup truck with an open bed at the back, facing right. o.color: body (default green), o.load: boxes in the bed, o.dent |
| `bus` | 200:80, 20 | bus: yellow school bus, side view facing right. o.color: body (default yellow), o.text (default 'SCHOOL BUS'), o.stop: stop arm swung out |
| `ambulance` | 150:76, 18 | ambulance: box ambulance with red cross, stripe and roof lights, facing right. o.lights:false = no flashing rays |
| `towtruck` | 150:76, 18 | towtruck: tow truck facing right. Default wrecker with boom and hook; o.flatbed: flatbed carrier, o.car: a car on the flatbed (true or a color), o.color: body (default orange) |
| `dumptruck` | 150:88, 20 | dumptruck: dump truck facing right. o.color: body (default yellow), o.load: dirt heaped in the bed, o.dump: bed tipped up with dirt pouring out the back |
| `rv` | 180:90, 22 | rv: Class C motorhome with over-cab bunk, facing right. o.color: side stripe and cab (default teal) |
| `trailer` | 140:70, 16 | trailer: travel trailer (towable camper) with hitch tongue on the right. o.color: stripe (default orange) |
| `boat` | 120:64, 13 | boat: small motorboat with outboard motor on water, facing right. o.color: hull (default red), o.water:false hides the water |
| `sailboat` | 90:100, 24 | sailboat: sailboat with mainsail and jib on water, facing right. o.color: hull (default blue), o.sail: sail color (default white), o.water:false hides the water |
| `jetski` | 100:56, 10 | jetski: personal watercraft (jet ski) on water, facing right. o.color: body (default yellow), o.spray:false hides the spray, o.water:false hides the water |
| `forklift` | 96:90, 16 | forklift: forklift facing right with mast and forks. o.color: body (default orange), o.load: pallet with a box on the forks, o.raised: forks lifted high |
| `bulldozer` | 136:84, 19 | bulldozer: crawler bulldozer with blade, facing right. o.color: body and blade (default yellow) |
| `plane` | 180:64, 16 | plane: airplane, side view facing right. o.kind: 'jet' (airliner, default) / 'prop' (small single-engine plane), o.color: tail, wing and stripe (default blue) |
| `trafficlight` | 36:96, 20 | trafficlight: traffic signal on a pole. o.on: 'red' (default) / 'yellow' / 'green' / 'none' |
| `stopsign` | 50:96, 18 | stopsign: red octagonal STOP sign on a post. o.text (default 'STOP') |
| `cone` | 44:56, 8 | cone: orange traffic cone with reflective bands. o.color (default orange) |
| `gaspump` | 60:96, 18 | gaspump: gas station fuel pump with price screen, hose and nozzle. o.color: body (default red), o.price: screen text (default '$3.49'; '' for a blank screen) |
| `crash` | 110:80, 16 | crash: comic-book collision burst with a shout word. o.text (default 'CRASH!'), o.color: burst (default yellow), o.ink: word color (default red) |
