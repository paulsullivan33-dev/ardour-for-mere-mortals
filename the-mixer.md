# The Mixer

The Mixer window is the studio desk: one vertical **strip** per track, sound flowing down each strip and out to the right, into the **master strip**. This chapter walks a strip from top to bottom. The anatomy is not theoretical — the lab listed the processors of its real track from inside the program, and the list is longer, and more instructive, than the one most users imagine.

## A strip, top to bottom

A track's signal passes, in order, through:

1. **Input** — where the track's sound comes from: an interface channel when recording, its playlist when playing back.
2. **The processor chain** — plugins and built-ins, in a row, each able to change the sound (chapter 10).
3. **The fader** — the track's loudness control, the one control every strip guarantees.
4. **Pan** — where the track sits between left and right (on stereo tracks, a balance/pan arrangement).
5. **Output** — usually the master bus, or a bus that itself flows to the master.

Around those sit the strip's switches: **mute** (silence this track), **solo** (silence all the *others* — the fastest way to inspect one track), phase/polarity invert, and the record-arm button while recording.

## The chain you already have

When the lab reloaded its session and enumerated the processors on its one track, Ardour reported ten, in this order (transcript `t32`):

```
Meter, Recorder, latcomp, Player, TriggerBox, Polarity, Trim,
ACE Compressor, Fader, main outs
```

Only one of those — the **ACE Compressor** — was added by the lab (chapter 10). The rest are the track's permanent machinery: a **meter** watching levels, the **Recorder** (disk writer) and **Player** (disk reader), a latency compensator, the **TriggerBox** (Ardour's clip-launching slot), **Polarity** and **Trim** (a small gain stage), then your plugins, then the **Fader**, then the outputs. Two lessons live in that list. First, a track is never "just the file": even an empty track is a chain of decisions. Second, **plugin order is signal order**: a compressor before the fader hears the track at full level whatever the fader says, which is why "the effect sounds different when I turn the track down" is the expected behaviour, not a bug.

## Buses: treating tracks as a group

A **bus** is a strip whose input is other tracks. Route all the drum tracks to one bus and the drums get one fader, one compressor, one mute. Buses flow into the master in turn; a session can nest them as deep as the work needs. In a small session — the lab's one track — the master *is* the whole desk, and that is a legitimate way to work.

## Sends: borrowing a track's sound

A **send** taps a copy of a track's signal and routes it elsewhere — classically to a bus holding a reverb, so several tracks can share one "room" in different amounts (the send level per track is the amount). Sends can tap the signal before or after the fader, which decides whether the reverb amount follows the track's loudness or stays put; the distinction matters the first time a faded-down vocal leaves a ghost of reverb behind it.

## The master strip, and what "loud" means

The master strip is the exit: its fader sets the overall level and its meter is the one that must never clip — digital audio has a hard ceiling at **0 dBFS** (decibels below full scale), and an export that passes it is distorted in a way no later step can undo. Chapter 11 exports the lab's mix and measures a peak of −6.02 dBFS: comfortably below the ceiling, and the arithmetic of why (a half-scale sine put there on purpose) is part of the proof. **Automation** — fader moves, pan moves and plugin changes recorded against time, so the mix can ride a vocal up in the chorus by itself — lives on every strip and is drawn as lines over the timeline in the editor; it is the mixer's memory, and the last mixer idea a beginner needs: set it static first, automate when a static mix is nearly right.

**Check:** on any strip, name the signal's path from input to master, count its processors, and say which ones you added. Then look at the master meter while playing: if it touches the top, the mix — not the speakers — is the problem to fix.
