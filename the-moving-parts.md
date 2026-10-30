# The Moving Parts

Ardour looks like one big window, but it behaves better once you know which part is which. This chapter names the parts and — more useful — says which part *holds* what, because most beginner confusion in a DAW is really "which thing remembers this?"

## The audio engine and its backends

At the bottom sits the **audio engine**: the part that moves sound between the program and the outside world, one small chunk at a time, to a strict clock. The engine talks to the world through a **backend** — a driver module chosen when a session starts. Ardour 8.4 ships four backends, and this guide's lab listed them in the installed program:

- **ALSA** — talks to the Linux kernel's sound system directly; the usual choice for serious recording on Linux.
- **JACK** — talks to the JACK audio server, which lets several programs share one device and route sound between them.
- **PulseAudio** — talks to the desktop sound server most Linux desktops run; convenient, not built for low-delay recording.
- **Dummy** (listed in the program as *None (Dummy)*) — pretends. It runs the whole engine on a clock with no hardware at all. It exists for testing, development and headless use — and it is what this guide's lab recorded through, which is why the lab's first take is silence (chapters 4 and 6).

On macOS and Windows the same job is done by CoreAudio and ASIO backends respectively. Chapter 4 is devoted to choosing among these, and to the two numbers that rule them: **sample rate** and **buffer size**.

## The session

A **session** is one project — one song, one podcast episode, one film scene. It is a folder on disk containing:

- one XML file named after the session (for example `FirstTake.ardour`) that describes everything: tracks, regions, mixer settings, the tempo map;
- an `interchange` folder holding the actual recorded audio and MIDI files;
- side folders for exports, peak data (the waveform pictures), analysis and backups.

Chapter 5 reads a real session file line by line. The fact that a session is *readable text plus ordinary WAV files* is one of Ardour's great virtues: nothing about your work is locked inside a format only Ardour can open.

## Tracks, playlists and regions

A **track** is a lane: one input source, one chain of processing, one fader. Audio tracks hold sound; MIDI tracks hold note data for instruments (chapter 9); **buses** are tracks whose input is other tracks, used to treat a group — all the drums, say — as one thing.

What a track *plays* at any moment is decided by its **playlist**: the ordered list of **regions** currently assigned to it. A region is a chunk of audio (or MIDI) with a position, a length, and a pointer to the file it came from. Editing in Ardour is almost entirely region work — moving, splitting, trimming, fading — and it is **non-destructive**: the underlying recorded files are never changed by an edit. A track can keep several playlists (several candidate arrangements of the same takes) and switch between them, which is how "comping" a best take from several tries is organised.

In the lab's session, one stereo region named `Take1_Tone-1` sat on a track named `Tone`, pointing at two files — one per channel — in the interchange folder. Chapter 5 shows the exact lines of XML that say so.

## The two windows: editor and mixer

The program presents the same session through two main windows:

- The **Editor** is the timeline: tracks stacked vertically, time running left to right, regions as blocks. Recording and arranging happen here.
- The **Mixer** is the mixing desk: one vertical **strip** per track — fader, pan knob, mute and solo buttons, and the track's list of plugins — all flowing right into the **master strip**.

They are two views of one thing. Move a fader in the mixer and the track's loudness changes in the editor; add a plugin in either and it appears in both.

## The master bus

Every session has a **master bus**: the final lane. Each track's output flows into it (directly, or through buses), its fader sets the overall level, and it is what an **export** records. When this guide says "the mix", it means what comes out of the master bus. In the lab session, exporting produced a stereo file even though the only track was fed by two mono files — the master bus is stereo, so the mix is stereo.

## Plugins and processors

A track's sound passes through a chain of **processors** before its fader: some are built in (a meter, the recorder itself, a polarity switch, a trim), and some are **plugins** — separate little programs loaded into the chain: compressors, equalisers, reverbs, synthesisers. Chapter 10 covers the formats (LV2 is the native one on Linux) and shows the real chain from the lab's track, in which the compressor the lab added sits eighth in line, behind seven processors most users never notice Ardour put there.

## The transport and the tempo map

The **transport** is the play/record machinery: playhead position, rolling and stopped, record armed or not. Under it sits the **tempo map** — the session's record of beats per minute and time signature over time — which is why positions in Ardour can be spoken of in bars and beats as well as minutes and seconds. The session file stores positions in an internal unit (the *superclock*, 282,240,000 ticks per second); chapter 5 turns one of those numbers back into a sample count and checks it against the file it describes.

## The scripting door

One more part, invisible until you look: Ardour embeds the **Lua** programming language. Scripts can create sessions, add tracks and plugins, arm recording, roll the transport, and react to events such as an export finishing. Ardour ships dozens of example scripts, and its Debian package adds command-line tools built on the same machinery — a session maker, a session exporter, and a Lua interpreter that runs Ardour with no windows at all. This guide's lab did most of its work through that door, and chapter 12 reports exactly how far it opens — including the one everyday job, importing an audio file, that in version 8.4 it does not reach.

You now have the cast. Chapter 3 gets the program itself.
