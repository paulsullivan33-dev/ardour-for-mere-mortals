# Sessions and Their Files

A session is a folder. That single fact — no database, no opaque project blob — shapes how you back Ardour work up, how you rescue it, and how this guide can show you one. This chapter opens the lab's real session, `FirstTake`, and reads it.

## Making one

You can create a session in the program (the session dialog offers *New Session*, a name, and a sample rate), or without the program at all. Ubuntu's package includes a command-line session maker, and the lab used both it and scripting (chapter 12); here is the tool (transcript `t21`):

```
$ ardour8-new_session -s 48000 ~/FirstTake
Created session in '/home/hatch/workspace/ardour-labwork/FirstTake'
```

One honest detail from the same transcript: asked to list its session **templates** (`ardour8-new_session -L`), the Ubuntu package answered with an empty list — this build ships no ready-made templates, so a new session starts as the plain default: one stereo master bus and nothing else. Sessions you design can be saved as templates of your own from within the program.

## The folder, as found on disk

After the lab recorded one take in it, the session folder held (transcript `t27`):

```
FirstTake/
├── FirstTake.ardour          the session itself — one XML file
├── FirstTake.ardour.bak      the previous saved version, kept automatically
├── FirstTake.history         the undo history
├── instant.xml               window and editor state
└── interchange/
    └── FirstTake/
        └── audiofiles/
            ├── Take1_Tone-1%L.wav
            └── Take1_Tone-1%R.wav
```

Plus standing folders the session grows as you work: `peaks` (the waveform pictures the editor draws), `export` (default home of exported mixes), `analysis`, `plugins`, `externals` (files the session references but does not own) and `dead` (sounds from discarded takes, kept until you clean up — chapter 13).

Three consequences worth learning now:

- **Back up the folder, the whole folder.** The `.ardour` file alone is a description of music whose audio lives in `interchange`. Chapter 13's recipe is built on this.
- **The audio is ordinary WAV.** The takes are standard files (here, 48,000 Hz, 32-bit float, one channel each) that any audio tool can open. Nothing is locked in.
- **Ardour keeps a spare of the description.** `FirstTake.ardour.bak` is the session file as it was before the last save — the first thing to try if a session file is ever damaged (chapter 16).

## Inside the XML: where the take lives

Open `FirstTake.ardour` (the lab kept its copy at `ardour-lab/FirstTake.ardour`; it is long — a real session file runs to thousands of lines) and three sections explain almost everything:

**Sources** — the inventory of audio files the session knows:

```xml
<Source name="Take1_Tone-1%L.wav" take-id="2026-10-30 23.02.16" type="audio"
        flags="" id="279" timestamp="1793401336" natural-position="a0"
        captured-for="Tone" channel="0" origin="" gain="1"/>
<Source name="Take1_Tone-1%R.wav" ... id="281" ... captured-for="Tone" .../>
```

Read it plainly: two files, one per channel of a stereo recording, captured for the track named `Tone`, each with its own numeric ID. MIDI sources appear the same way, pointing into `interchange/<name>/midifiles`.

**Regions** — the chunks placed on tracks:

```xml
<Region name="Take1_Tone-1" ... whole-file="1" ... start="a0"
        length="a1091233920@a0" ... id="304" type="audio"
        source-0="279" source-1="281" channels="2"/>
```

The region is *whole-file* (it uses its sources end to end), it is stereo because it names **two** sources — the IDs from the section above — and its length is written in Ardour's internal time unit, the **superclock**: 282,240,000 ticks per second. The number is checkable, and the lab checked it: 1,091,233,920 ÷ 5,880 ticks-per-sample at 48,000 Hz = **185,584 samples** — precisely the sample count an independent tool (`soxi`) reported for the take files. The session file and the audio agree; that is what a healthy session looks like.

**Playlists** — further down, each track's playlist lists which regions it plays and where. The lab confirmed the same fact from inside the program as well: after saving, a fresh script load of the session reported the `Tone` track's playlist holding exactly one region, `Take1_Tone-1` (transcript `t31`).

Everything else in the file — mixer strip settings, plugin configurations, the tempo map, your region's fades — is the same kind of declarative XML, written when you save and read when you open. You will probably never edit it by hand, and you should not need to; but knowing it is *there, readable, and checkable* changes a session from a leap of faith into an artefact.

## Snapshots and saving

Saving a session writes the XML (and moves the old one to `.ardour.bak`). A **snapshot** is a named extra copy of the session file inside the same folder — "before the big edit" as a file, not a hope — sharing the same audio. Ardour's scripting and export tools address sessions by folder plus snapshot name (chapter 11's exporter takes both). Plain habit worth forming: save often, snapshot before anything irreversible, and let the folder — audio included — be what your backups copy.

**Check:** in your own session folder, find the `.ardour` file, the `interchange` folder, and one `<Source>` line per file in `audiofiles`. If you can point at the file a region came from, you understand sessions.
