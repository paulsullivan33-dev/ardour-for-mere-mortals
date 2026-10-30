# The Neighbours

Ardour is one answer to "how do I record and mix sound on a computer?" These are the others, placed fairly. Nothing here was benchmarked for this guide; the characterisations are the tools' own shapes, and the one relationship claim — Mixbus — is a matter of public record.

## Audacity — the editor

[Audacity for Mere Mortals](https://paulsullivan33-dev.github.io/audacity-for-mere-mortals/) covers the free sound editor in this same series. Audacity works on one piece of audio at a time, directly: open a recording, see it, cut it, clean it, export it. It has multitrack abilities but its centre of gravity is the single file. The tools are complements, not rivals: record and mix in Ardour, then trim and tag the finished stereo file in Audacity — or rescue one bad field recording there before it ever becomes a region. If your whole job is "fix this one recording", Audacity alone is the shorter path.

## Harrison Mixbus — the close relative

Mixbus is a commercial DAW built **on Ardour's core**, with Harrison's own console-style mixer and channel DSP on top, sold and supported by Harrison. Sessions and skills transfer further between Ardour and Mixbus than between any other pair in this chapter. People choose it for the mixer design and the support line; people choose Ardour for the price arrangement and the unmodified program. (Ardour's developers note they have no responsibility for Harrison's product, and vice versa.)

## REAPER — the inexpensive professional

REAPER is commercial software with a small price, a long evaluation, and a reputation for running anything anywhere: every plugin format, huge sessions, deep customisation. It is not free software — you cannot read or modify its source — which is the real fork in the road between it and Ardour, more than any feature list. Studios that need its particular powers choose it with open eyes.

## The commercial lane — Pro Tools, Logic Pro, Cubase, Ableton Live

The names your collaborators will mention. Pro Tools is the entrenched studio standard (and the most account-and-licence-bound); Logic Pro is Apple's, Mac-only, with a large bundled instrument library; Cubase is Steinberg's veteran; Ableton Live is built around live performance and clip launching. All are capable; all cost money up front or by subscription; none is free software. The practical fact for collaboration: **no DAW opens another DAW's sessions natively.** Moving work between them means exporting **stems** — one rendered file per track — which is a chapter-11 export per track, and a reason the export habit matters more than the badge on the program.

## The smaller free tools

- **LMMS** — a free, pattern-based studio aimed at electronic music: step sequencers, loop lanes, bundled instruments. For beat-first composing it is a gentler first day than Ardour; for recording a band, it is not the tool.
- **Qtractor** and **Rosegarden** — long-standing free Linux sequencer/DAWs, lighter than Ardour, with Rosegarden adding music notation. Capable, smaller communities.
- **Zrythm** — a newer free DAW with a modern interface and automation-first design; younger than Ardour by two decades, which shows in both polish and track record.

## ffmpeg and SoX — underneath everything

Not DAWs at all: command-line converters and processors. This guide used **ffmpeg** to make its fixture tones and read its files back, and its sibling guide [ffmpeg for Mere Mortals](https://paulsullivan33-dev.github.io/ffmpeg-for-mere-mortals/) teaches it properly. When the job is "convert these forty files" rather than "mix this song", they are the right size of tool.

**The summary in one line:** edit a file in Audacity, compose loops in LMMS, pay for REAPER or the commercial lane when their specifics earn it — and record, arrange and mix multitrack work in the open in Ardour.
