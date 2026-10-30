# Exporting and Proving the Mix

An **export** renders the master bus — everything the session plays, through every fader and plugin — into one ordinary audio file. It is the moment a session becomes a song other people can hear, and it is the chapter this guide has been aiming at: the lab exported a real mix and then *measured* it three ways, because an export is also where a DAW can fail silently — a muted track, a wrong range, an empty render — and still hand you a file.

## Exporting from the command line

In the program, exporting is *Session → Export*. Ubuntu's package also ships the same machinery as a tool, and the lab used it (its options, from the program's own help — transcript `t05`): choose a bit depth (16, 24, 32 or float), a sample rate, broadcast WAV headers if you need them, peak **normalisation** if you ask for it, and an output name. It exports the **session range** — the span between the session's start and end markers — through the master bus:

```
$ ardour8-export -o ~/FirstTake-mix.wav ~/FirstTake FirstTake
* Writing /home/hatch/workspace/ardour-labwork/FirstTake-mix.wav
* Exporting Audio
* Done.
```

Note what the tool was handed: the session *folder* and the *snapshot name* — chapter 5's model, used exactly as promised. The default output is 16-bit WAV at the session's sample rate, the same shape as a CD track.

## What was in the lab's session, honestly

One disclosure belongs in the text, not just the ledger. The lab's take (chapter 6) was silence, because the Dummy backend hears nothing. Silence exports perfectly — and proves only that the plumbing works. To prove the plumbing carries *signal*, the lab replaced the samples inside the two take files with a generated tone (440 Hz, the A above middle C, at half of full scale), keeping the same filenames, the same format (48,000 Hz float) and the exact same length of 185,584 samples per file — then exported the untouched session (transcript `t28` records the before and after levels: maximum amplitude 0.000000 → 0.499878). No session file was edited; from Ardour's side of the glass, the microphone simply heard a tone instead of a quiet room. Why this detour exists at all — scripting in 8.4 cannot import a file — is chapter 12's story and `criteria.md`'s ledger entry.

## The proof: three measurements of one file

**1. The format.** `ffprobe` reads the export as: WAV, **48,000 Hz, 2 channels, 16-bit** — the session's rate, the master bus's channel count, the tool's default depth (transcript `t30`).

**2. The duration.** The measuring script (`ardour-lab/check-mix.py`, kept in this repository) counts **185,587 frames = 3.866 seconds**, against the take's 185,584 samples. Three frames of difference over 3.87 seconds — the fades and rounding at the region's edges — is agreement, not error: the export covers the take, all of it, and nothing else.

**3. The content.** Per channel, the script measures:

```
channel 1: peak 0.4999 (-6.02 dBFS), RMS 0.3534 (-9.04 dBFS),
           zero crossings 3402 -> ~439.9 Hz
channel 2: peak 0.4999 (-6.02 dBFS), RMS 0.3534 (-9.04 dBFS),
           zero crossings 3402 -> ~439.9 Hz
```

Every number cross-checks. Peak −6.02 dBFS is exactly half of full scale — the level the tone was made at, arriving through the track, its fader at unity, its compressor not driven (a −6 dB tone under a default threshold), and the master untouched. RMS −9.04 dBFS is what a sine wave must read: peak divided by √2, 3.01 dB below the peak. And the **zero crossings** — how often the waveform crosses silence, twice per cycle — estimate the pitch at **439.9 Hz** against the 440 Hz generated. The file does not merely exist and is not merely loud; it contains the right note, at the right level, for the right length, in both channels. That is what "the export worked" means when it is said carefully.

## Loudness, in one honest section

Peak level is not loudness. A file can peak at −6 dBFS and sound quiet or loud depending on its average energy and its content, which is why delivery standards are written in **LUFS** — a loudness unit that weights sound roughly as ears do. Broadcast standards such as EBU R128 specify −23 LUFS integrated; streaming services commonly normalise around −14 LUFS. Ardour's graphical export dialog can analyse and normalise a mix to a loudness target and report its true peak; the command-line tool's `-n` is the simpler peak normalisation to 0 dBFS, which is *not* the same thing (it makes the loudest instant full-scale and leaves the perceived loudness wherever it was). The lab used neither — its tone's level was fixed by construction, and measured, not normalised. Choosing targets for a real release is documented-only here; the measurement habit above is the part to keep.

## Formats in passing

WAV at the session rate is the archival answer. Export additionally to what the destination needs — FLAC for a lossless file half the size, MP3/Ogg for convenience copies — from the same render, and keep the WAV. The export dialog and the tool both offer the choices; the rule is to render once at full quality and derive the rest, never to export an export.

**Check:** export any session, then run the three measurements — format, duration against the session's range, and a level or crossing count that matches what you put in. A file that passes all three is a mix. One that fails any is a bug report with numbers attached.
