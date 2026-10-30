# MIDI, Honestly

MIDI is the other kind of track. An audio region holds a *recording of sound*; a MIDI region holds *instructions* — note on, note off, how hard, when — which a synthesiser turns into sound at playback. The same session can hold both: recorded voices as audio, composed parts as MIDI. This chapter explains MIDI's place in Ardour and states plainly what this guide can back with evidence and what it cannot.

## What the lab can prove

MIDI is not an afterthought bolted onto the session format; it is in the plumbing, and the lab touched several pieces of it for real:

- The session folder grew a **`midifiles`** twin of `audiofiles` (`interchange/<session>/midifiles`) the moment the session was created — MIDI sources live beside audio sources, in the same inventory (chapter 5).
- The startup log of the graphical program records **459 MIDI patch files** loaded from the program's data — the instrument-name maps Ardour uses to label the sounds of external MIDI hardware (transcript `t33`).
- The Ubuntu package ships **two synthesisers** among its seven bundled LV2 plugins: **a-fluidsynth**, which plays SoundFont sample libraries (the lab's download included over 100 MB of General MIDI soundfonts, fetched as Ardour's own dependencies), and **Reasonable Synth**, a small built-in synth that makes a MIDI track audible with zero setup. A MIDI track plus Reasonable Synth is the shortest path from silence to a composed note in Ardour.
- The program ships MIDI Lua tooling among its example scripts (note remapping, a MIDI monitor, CC-to-automation conversion) — MIDI is scriptable like everything else (chapter 12).

## What the lab cannot claim

The lab did not compose, play or record a single note of MIDI music. Its attempt to create a MIDI track by script met the API's exactness instead (the call wants channel counts as objects, not bare numbers — transcript `t26` records the refusal), and no MIDI keyboard exists in the lab to record from. So: **MIDI performance and editing in this guide are documented-only**, taught from the official manual's description of the taught version, and this chapter does not grade any of it by ear.

## The model, briefly

- A **MIDI track** takes input from a keyboard/controller (or from drawn notes) and outputs sound through an instrument plugin placed in its chain — the synth *is* a processor, first in line (chapter 10's chain applies unchanged).
- Notes live in **MIDI regions**, edited in the editor's piano-roll view: pitch vertically, time horizontally, **velocity** (how hard the note was struck) as a per-note value. In version 8.4 the piano roll is inline in the track; version 9 moved it into separate windows — one of the visible differences between the taught program and the current one.
- MIDI data is small and indestructible in a way audio is not: change the synth and the same region is a different instrument; fix a wrong note by dragging it. That is the entire appeal — the performance is data, not sound, until the moment it plays.
- Sessions store MIDI as standard `.mid` files in `midifiles`, importable and exportable like the WAVs — the same no-lock-in property as the audio side.

## When MIDI is the right tool, and when it is not

Reach for MIDI when the part is *composed* — keyboards, programmed drums, anything you will still be adjusting after the fact — and for controlling external hardware. Reach for audio when the thing itself is the performance: a voice, a guitar through a real amplifier, a room. Recording a singer as MIDI is not a thing; recording a keyboard as audio only is a missed opportunity. Most real sessions end up, like this chapter, honestly mixed.

**Check:** in a session of your own, find the `midifiles` folder next to `audiofiles`, put Reasonable Synth on a MIDI track, and draw one note that plays back. That single note exercises the whole model: region, data, instrument, chain, master.
