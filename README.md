# Ardour for Mere Mortals

A digital audio workstation — a **DAW** — is the program a recording studio fits inside: it records several tracks of sound at once, lets you arrange the pieces on a timeline, mixes them together with effects, and exports one finished file. **Ardour** is a DAW that is free software, released under the GNU General Public License, and it runs on Linux, macOS and Windows. No account, no licence server, no subscription is needed to run it — and a session it makes is a folder of ordinary files on your disk, including one XML file you can open and read.

This guide explains how Ardour is put together, how to get it, and how a session, a track, a take and a mix relate. Then it does the thing this series always tries to do: it **proves** the result. The lab that wrote this guide had no sound card, no speakers and no ears. It drove Ardour through the program's own scripting door, recorded a take from a backend that produces only silence, and measured everything — file headers, sample counts, levels, and the pitch of the exported mix, checked by counting zero crossings. A DAW that fails quietly still writes files, so measuring is not pedantry; it is how you know the music is actually in there.

The lab ran the real thing: **Ardour 8.4.0**, Ubuntu 24.04's own package, on a small shared Linux machine. Against it the lab created sessions two different ways, added tracks and a compressor plugin by script, armed a track and recorded a four-second take on the **Dummy backend** — Ardour's pretend sound card, which runs the whole engine with no hardware at all — pulled the session file apart to show where every piece lives, exported the mix from the command line, and measured the export three independent ways. It also launched the full graphical program under a virtual display as far as its first-run welcome wizard, and deliberately hit the walls: the package manager lock held by another user of the machine, the import command that scripting does not have, and the take that is only silence until you understand why.

What the lab could not do, it did not fake. It could not listen, record a real instrument, or test a single plugin by ear, so it never claims anything *sounds* good; it reports durations, levels and frequencies and leaves the listening to you. The taught version is Ubuntu's 8.4.0 while Ardour's own site offers the 9 series — that gap is real, it is explained in chapter 3, and features that only exist in version 9 are not taught here as if you had them. `criteria.md` keeps the full ledger of what was run and what was only read.

## What this guide covers

- [**What Ardour is**](what-ardour-is.md) — the mental model: performances in, one finished file out, and where Ardour sits among DAWs
- [**The moving parts**](the-moving-parts.md) — the audio engine, backends, sessions, tracks, playlists, regions, the mixer and the master bus, and which part holds what
- [**Getting Ardour**](getting-ardour.md) — the three honest ways to get it (pay-what-you-can official builds, your distribution's package, building the source), the version gap between them, and the first-run wizard
- [**Audio backends**](audio-backends.md) — ALSA, JACK, PulseAudio and the Dummy: what a backend is, sample rates and buffer sizes, and why the pretend one matters
- [**Sessions and their files**](sessions-and-their-files.md) — a session is a folder: the XML file read piece by piece, the interchange folder, snapshots, and the backup Ardour keeps on its own
- [**Your first take**](your-first-take.md) — recording, for real: arming a track, rolling, stopping, and the region that appears — done by script in the lab, with the on-screen route described alongside
- [**Editing regions**](editing-regions.md) — the timeline's vocabulary: regions, splits, trims, fades, layers and playlists, in plain terms
- [**The mixer**](the-mixer.md) — channel strips, faders, pan, the processor chain Ardour builds before you add anything, sends, buses and the master
- [**MIDI, honestly**](midi.md) — MIDI tracks and files, the two synths in the box, and what this guide can and cannot claim about composing with it
- [**Plugins**](plugins.md) — LV2 first on Linux, VST3 and the rest, the ACE set that ships with Ardour, and where in the chain an effect sits
- [**Exporting and proving the mix**](exporting-and-proving-the-mix.md) — exporting from the command line, and measuring the result: format, levels, and pitch by zero crossings
- [**The Lua door**](the-lua-door.md) — Ardour's built-in scripting: what the lab drove through it, the one important thing it cannot do, hooks, and the scripts Ardour ships
- [**Recipes**](recipes.md) — back a session up properly, archive a finished song, run Ardour with no sound card at all, and check a folder of exports in one pass
- [**The neighbours**](the-neighbours.md) — Audacity the editor, Mixbus the close relative, REAPER and the commercial DAWs, and the smaller free tools: what each does that Ardour doesn't, and vice versa
- [**Limits**](limits.md) — the version gap, the silent backend, the import scripting cannot do, the steep first hour, and the rest, stated plainly
- [**Troubleshooting**](troubleshooting.md) — the locked package manager, xruns, the take that came out silent, the session that will not open, and the traps this guide's lab fell into
- [**Glossary**](glossary.md) — the terms, collected in one place

## What it doesn't cover

Playing or singing anything. This guide operates the recorder; it cannot teach music, and its only fixture is a generated tone. Mixing by ear — levels, equalisation taste, when a compressor helps — is a craft of its own and the lab had no ears to practise with. Version 9 features (clip launching, the separate piano-roll windows) are named where they change the picture but not taught; the taught program is 8.4.0. Film and video work, surround formats, and control surfaces are pointed at, not covered.

## How to use this guide

Read chapter 1 for the model and chapter 2 before installing anything — knowing which part holds what turns later confusion into a named problem. Chapters 3 to 5 get you a program, a backend and a session folder you understand. Chapter 6 records in the same sitting. Chapter 11 is the one to read slowly even if you have speakers: its checks are how you catch the silent failures — including the take that contains nothing at all — before they reach anyone's ears. The lab's transcripts live in `ardour-lab/transcripts/`, its scripts are `ardour-lab/lab-build-session.lua` and `ardour-lab/lab-verify-reload.lua`, and its measuring script is `ardour-lab/check-mix.py`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Audacity for Mere Mortals](https://paulsullivan33-dev.github.io/audacity-for-mere-mortals/)
- [ffmpeg for Mere Mortals](https://paulsullivan33-dev.github.io/ffmpeg-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/ardour-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/ardour-for-mere-mortals/blob/main/LICENSE-CODE).
