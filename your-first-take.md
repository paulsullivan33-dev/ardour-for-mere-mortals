# Your First Take

Recording in Ardour is three acts: **arm** the track (tell it to listen), **roll** the transport (play and record together), **stop** and keep the take. This chapter performs all three for real. The lab had no microphone — its backend was the Dummy, whose inputs are silence — so the lab's take is four seconds of perfectly recorded nothing, and that turns out to be the ideal first take: everything about the *process* is real, measurable, and safe to repeat while you learn. Where the on-screen route differs from the lab's scripted one, both are given.

## Before you roll

You need: a session (chapter 5), a track (in the editor: *Track → Add Track or Bus*, an audio track, named for what it will hold — the lab's is called `Tone`), and a backend running (chapter 4). On a real machine you also need the track's **input** set to the interface channel your microphone or instrument is plugged into, and headphones if a microphone and speakers share the room — the feedback howl is a rite of passage you may skip. Input selection, input monitoring choices, and setting a sensible recording level are covered by the manual for your interface; none of them could be exercised in the lab, which had no interface, and this guide does not pretend otherwise.

In the lab, the track was added by script instead of by menu — the two are the same operation, and chapter 12 shows the script whole. The result, verified in the session: a stereo audio track named `Tone`, plus the master bus it feeds.

## Arm, roll, stop — the lab's recording, with the evidence

The lab drove the recording through Ardour's Lua door (transcript `t22`):

1. **Arm.** The track's record-enable was switched on, and the session was told to enable recording (`maybe_enable_record` — Ardour's "if anything is armed, be ready" step). On screen, this is the track's red record-arm button plus the transport's main record button.
2. **Roll.** The transport was set rolling. Four seconds later the playhead stood at sample 186,368 of 48,000 per second — the engine had genuinely run, at full speed, on the Dummy clock.
3. **Stop, keeping the take.** The stop request carries a *keep or discard* decision; the lab kept the take. On screen this is simply stopping, and answering the keep/discard question if the take was very short or you have Ardour set to ask.

Then the part no screenshot can give you — the receipts. The session folder gained two files, `Take1_Tone-1%L.wav` and `Take1_Tone-1%R.wav` (chapter 5 read their entries in the session XML), and the track's playlist gained exactly **one region**, named after the take. An independent tool measured each file:

```
Duration: 00:00:03.87, Audio: pcm_f32le, 48000 Hz, 1 channels
```

3.87 seconds at the session's rate, 32-bit float WAV — a real recording artefact. And its content, measured just as plainly:

```
Maximum amplitude:     0.000000
RMS     amplitude:     0.000000
```

Silence. Not a fault: arithmetic proof of what the Dummy backend is. A pretend microphone in a pretend room records a pretend performance, at full quality, with correct paperwork. On real hardware the identical steps produce your actual playing — and, with a microphone left muted or an interface unplugged, they can just as easily produce this same silent file, which is why chapter 11 teaches proving a mix rather than trusting one, and chapter 16 keeps "the take came out silent" as a named, diagnosable failure rather than a mystery.

## Takes, plural

Record again over the same ground and Ardour does not overwrite: each pass is a new take with its own files, stacked as **layers** in the same region position or laid end to end, as you choose. The playlist (chapter 2) holds the arrangement you settled on; earlier takes stay in the session, in `interchange`, until a cleanup. Discarded-on-purpose takes go to the session's `dead` folder rather than vanishing — Ardour prefers keeping your audio to tidying your disk, a preference chapter 13's archiving recipe respects by copying everything.

## Punching in and looping — honestly labelled

Two recording refinements every DAW offers, both taught here from the manual because a silent backend cannot demonstrate their *musical* use, though the machinery is the same:

- **Punch recording**: set a range, and Ardour records only inside it — the standard way to re-do one fluffed line inside a good take.
- **Loop recording**: set a loop, and each pass becomes another take layer — the standard way to record several tries of a solo and comp the best.

Both live on the transport's range and loop controls; the arm–roll–stop underneath them is the one you have already done.

**Check:** after your first take you can find, in the session folder, one new file per channel in `interchange/<session>/audiofiles`, one new region on the track's playlist, and a measured duration for the file that matches how long you rolled. If the duration is right and the levels are not all zero, you have recorded — whatever it sounded like.
