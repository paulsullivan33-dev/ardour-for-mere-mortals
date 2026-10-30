# Glossary

**Backend** — the engine module that carries audio between Ardour and the world: ALSA, JACK, PulseAudio, or the pretend Dummy (chapter 4).

**Buffer size** — how many samples the engine moves per trip. Small means low latency and less slack; large means the reverse.

**Bus** — a mixer strip whose input is other tracks, letting a group share one fader and one chain. The **master bus** is the final one: everything exits through it.

**Comping** — assembling one good performance from several takes by choosing the best layer passage by passage.

**dBFS** — decibels below full scale, digital audio's level unit. 0 dBFS is the ceiling; everything real is below it.

**DAW** — digital audio workstation: the program category Ardour belongs to — recorder, editor and mixer in one.

**Export** — rendering the master bus to an ordinary audio file (chapter 11).

**Fader** — a strip's main loudness control, and the fixed landmark near the end of its processor chain.

**Interchange** — the folder inside a session holding its audio (`audiofiles`) and MIDI (`midifiles`) source files.

**Latency** — the delay between sound entering and leaving the program; set mainly by buffer size and sample rate.

**Layer** — one of several regions stacked at the same timeline position; the topmost opaque one plays.

**LUFS** — a loudness unit weighted to match hearing, used by broadcast and streaming delivery standards.

**Lua** — the scripting language built into Ardour; the door of chapter 12.

**LV2** — the free, native Linux plugin format; Ardour's first choice. **LADSPA** is its older, simpler ancestor. **VST3** is Steinberg's current commercial-world format, which Ardour also loads.

**MIDI** — note-and-control data rather than recorded sound: which note, when, how hard (**velocity**). Needs an instrument — a synthesiser plugin or hardware — to become audible.

**Normalise** — raising a file's level so its peak reaches a target. Peak normalisation is not loudness normalisation; see LUFS.

**Playlist** — the list of regions a track plays, in order. A track can keep several and switch.

**Processor** — anything in a strip's chain that can change the sound: plugins, plus Ardour's own meter, trim, polarity and fader landmarks.

**Punch-in** — recording only within a chosen range, to repair one passage inside a good take.

**Region** — a block on the timeline: a start offset and length into one or more source files, plus position, fades and gain. Editing moves regions, not files (chapter 7).

**Sample rate** — measurements per second of audio: 44,100 or 48,000 in nearly all work. A session has exactly one.

**Send** — a tap that copies a track's signal to another strip, typically a shared reverb bus.

**Session** — a whole project, stored as one folder: an XML description plus its source files (chapter 5).

**Snapshot** — a named extra copy of a session's description, sharing its audio; the cheap "before I change everything" save.

**SoundFont** — a file of sampled instrument sounds, played by a synthesiser such as the bundled a-fluidsynth.

**Source** — an audio or MIDI file a session knows about, listed in the session XML with an ID that regions point at.

**Superclock** — Ardour's internal time unit: 282,240,000 ticks per second, the unit region lengths are stored in.

**Take** — one recorded pass, kept as its own files and region.

**Track** — one row of the session: a playlist, a strip, a sound of its own.

**Template** — a session saved as a starting shape for new ones.

**Xrun** — a missed audio deadline; the crackle you hear and the counter in the setup dialog both count them (chapter 16).
