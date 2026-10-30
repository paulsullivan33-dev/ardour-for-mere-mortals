# Editing Regions

Editing is where a pile of takes becomes an arrangement. In Ardour, editing happens to **regions** — the blocks on the timeline — and almost never to the audio files beneath them. This chapter is the vocabulary of that work: what a region is made of, and the handful of operations from which nearly every edit is assembled. The concepts are taught from the program's model and its manual; the region facts quoted are from the lab's real session file, and the operations' *effects* are stated as the manual documents them — the lab's scripting door can create and inspect regions but the fine mouse work of the editor is, honestly, documented-only in this guide.

## A region, up close

Chapter 5 met the lab's region in the session file. Its attributes are the editing model in miniature:

```xml
<Region name="Take1_Tone-1" muted="0" opaque="1" locked="0" ...
        whole-file="1" ... start="a0" length="a1091233920@a0" ...
        default-fade-in="0" default-fade-out="0"
        fade-in-active="1" fade-out-active="1" ...
        source-0="279" source-1="281" channels="2"/>
```

- It has a **position** (where it starts on the timeline) and a **length**.
- It has a **start offset** into its source files: a region need not begin at its file's beginning. *Trimming* a region is nothing but moving its start offset and length — the file is untouched.
- It points at **sources** by ID — one per channel.
- It carries **fades**: a fade-in and fade-out, each with a length and a shape, both switched active here even at length 0. Fades are how clicks at cut points are avoided.
- It can be **muted** (present but silent) and **locked** (protected from accidents), and it sits in a stacking order among overlapping regions — **opaque** here, meaning the top region is what plays where regions overlap.

## The core operations

Everything else is combinations of these, all performed in the Editor window with the mouse and keyboard, all reversible (the session keeps an undo history — the lab's session folder has the `.history` file to prove it):

- **Move** — drag a region along its track, or to another track of the same kind. Its sources do not move; only the pointer does.
- **Trim** — drag a region's edge: the start offset and length change. Trim it back and the audio "comes back" — because it was never gone.
- **Split** — cut a region at a point (the playhead or the mouse), making two regions. Splitting at a mistake and deleting the middle is the single most common edit in spoken-word and music work alike.
- **Copy and duplicate** — the chorus again, the loop four times: copies are new region entries pointing at the same sources, costing no disk.
- **Fade** — drag a region's top corners to shape its fade-in and fade-out; drag across a join for a **crossfade** where two regions meet.
- **Gain** — each region has its own volume, adjustable as a line across it, independent of the track's fader: fix one loud word without touching the mix.
- **Stretch and pitch** — Ardour can time-stretch a region (slower or faster, pitch kept) with the stretch tool, at a quality cost that grows with the amount; the session file's region carries `stretch="1" shift="1"` fields for exactly this. Treat large stretches as an effect, not a correction.

## Layers, playlists and comping

Regions recorded over the same ground stack in **layers**; the topmost opaque one plays. **Comping** — assembling the best performance from several takes — is choosing, passage by passage, which layer is on top, usually by splitting the stack at phrase boundaries and promoting the best take in each span. A track can also hold several whole **playlists** — alternate arrangements of the same material — and switch wholesale; a playlist is cheap (pointers, not audio), so "the long version" and "the single edit" can live in one session.

## What editing cannot do

Editing rearranges what was recorded; it does not improve the recording itself. Noise reduction, pitch correction of a sung note, and removing a room's echo are processing (plugins, chapter 10, or a dedicated editor like Audacity for surgical work on a single file). And because Ardour's edits are pointers, a region can only ever play audio that exists in the session's sources — chapter 5's arithmetic (length in superclock ticks, checked against the file) is the ground truth every edit stands on.

**Check:** pick any region in a session and state its source files, its start offset, its length in samples, and its fade lengths. When those four answers come easily, the editor's mouse gestures are just shortcuts for changing them.
