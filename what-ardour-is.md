# What Ardour Is

A **digital audio workstation** — DAW for short — is a program that does the whole job of a recording studio in one place:

- **Record** several tracks at once: the singer on one track, the guitar on another, each kept separate.
- **Arrange** the recorded pieces on a timeline: move the chorus earlier, repeat a verse, cut the cough between phrases.
- **Mix** the tracks together: set each one's loudness, position in the stereo picture, and effects, until they add up to one piece of music.
- **Export** the result as one finished file you can hand to anyone.

**Ardour** is a DAW. It is **free software** — released under the GNU General Public License (GPL), which means the program's source code is public, anyone may copy and modify it, and no licence server or subscription decides whether it runs today. It has been in development since the early 2000s, it runs on Linux, macOS and Windows, and it is used for everything from bedroom demos to full studio recording. Its own site describes the same job list this chapter opened with: you can use Ardour "to record an orchestra, create with audio/MIDI loops, edit the perfect vocal take, mix a live show with effects, dub a video, and master your tracks for digital distribution" — that sentence is on the first screen of Ardour's own first-run wizard, which this guide's lab met in chapter 3.

## The one idea to keep

Everything in Ardour hangs off a small number of nouns, and the whole guide is easier if you hold them apart from the start:

- A **session** is one song or project. On disk it is a *folder*, not one opaque file — chapter 5 opens a real one and reads it.
- A **track** is one lane of the timeline, holding one instrument or voice at a time.
- A **region** is one recorded or placed chunk sitting on a track: a take, a verse, a loop.
- The **mixer** is where tracks are balanced; the **master bus** is the final lane every track flows into, and the thing an export actually records.
- A **plugin** is an effect or instrument that sits inside a track's chain: a compressor, a reverb, a synthesiser.

Chapter 2 gives each of these its proper introduction. The short version is: performances and files go in, regions on tracks are what you arrange, the master bus is what you hear, and the export is the master bus written to a file.

## Where Ardour sits

DAWs divide by price and by philosophy more than by capability:

- The commercial names — Pro Tools, Logic Pro, Cubase, Ableton Live — are sold or rented, and some tie sessions to accounts and licence managers.
- REAPER is inexpensive commercial software with a famously generous trial.
- Ardour asks for money differently: its ready-made downloads are **pay what you can** (chapter 3 explains the arrangement honestly, including the part where paying a little more gets you the next big version), the source code is free to build, and Linux distributions package it for free — usually a version behind, which is the version this guide teaches.
- Harrison's Mixbus, a commercial DAW, is built on Ardour's core with Harrison's own mixer design on top — Ardour is infrastructure as well as an application.

None of that makes Ardour a cut-down anything. It records unlimited tracks (your hardware sets the real limit), edits non-destructively, mixes with full automation, and scripts itself in a programming language — chapter 12 drives it that way. What it does not have is a marketing department, a bundled content library of loops and sounds, or an interface designed to be learned in an afternoon. Chapter 15 states the costs plainly.

## What Ardour is not

- **Not a sound editor in the small.** Audacity (a neighbour, chapter 14) edits one piece of audio directly, like a word processor edits text. Ardour *arranges references* to audio — editing a region does not change the recorded file under it. That difference is a feature: you can always go back.
- **Not a media player with ambitions.** It will not organise your music library.
- **Not a notation program.** It records performances as sound and as MIDI note data; printing sheet music is another tool's job.
- **Not magic.** It cannot fix a bad performance, a noisy room, or a take that was never recorded — chapter 6 meets a take that contains literally nothing, and chapter 11 shows how to *prove* whether yours does.

## The lab, and the honest frame

This guide's lab ran Ardour 8.4.0 — Ubuntu 24.04's package — on a machine with **no sound card at all**, using a backend that pretends to be one (chapter 4). It recorded a real take through that pretend hardware, exported a real mix, and measured both. It could not listen to anything, and the guide never grades sound quality. Where a topic needs ears, a real interface, or the graphical program's slower paths, the text says so and teaches from the official manual instead. `criteria.md` is the full ledger.

Check you have the model before moving on: a **session** is the folder, **regions** are the pieces, **tracks** are the lanes, the **master bus** is the exit, and an **export** is the exit written to a file. Chapter 2 names the moving parts properly.
