# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's fixtures are a generated tone and one demonstration
   session, nothing personal.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 15 names what the tool —
   and this guide's lab — cannot do: the version taught is not
   the current version, no sound was ever heard by the lab,
   recording here is machinery rather than music, scripting
   cannot import audio in the taught version, and sessions are
   not self-contained across machines.
8. **The ethics rule is in the text, early.** Ardour raises no
   interception question; its own line is drawn in chapter 1 and
   the README instead — the program is free software, your
   recordings and sessions are yours, there is no account and
   no telemetry, and the pay-what-you-can arrangement that
   funds it is stated exactly, in chapter 3, before any reader
   is asked to choose how to get it.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a small shared Ubuntu 24.04 sandbox. The
guide teaches **Ardour 8.4.0**, the version in Ubuntu 24.04's
package archive (package `1:8.4.0+ds1-2ubuntu8`); Ardour's own
site currently offers the **9 series** (9.8, August 2026), and
chapters 1, 3 and 15 state the gap and its consequences plainly.

**How the software was obtained, disclosed in full:** the lab
intended `apt install ardour` and found the package manager's
lock held by another tenant's work on the shared machine
(transcript `t01`, verbatim). Rather than disturb it, the lab
downloaded the identical distribution `.deb` files — Ardour and
the 37 dependencies not already present — and ran them unpacked
from a private directory via `LD_LIBRARY_PATH`, with the
program's data/config/library paths pointed at the same tree.
Nothing was installed system-wide. Every claim below comes from
those exact Ubuntu binaries; on a normal machine they are what
`sudo apt install ardour` delivers.

**The lab had no audio hardware and no way to listen.** All
engine work ran on Ardour's **Dummy backend** (shown in the
program as "None (Dummy)"), which runs the engine on an
internal clock with pretend inputs and outputs. Consequently:
recordings are real takes whose content is true silence, every
claim about sound is a *measurement* (durations, sample counts,
peak/RMS levels, zero-crossing pitch estimates), and nothing in
the guide grades how anything sounds.

Run for real, with transcripts as evidence (`ardour-lab/`):

- The target program and its package metadata identified
  (`t00`); the held apt lock recorded verbatim (`t01`); the
  extracted tree's dependency closure verified with `ldd`
  showing no missing library (`t03`).
- `ardour8 --version` — `Ardour8.4.0~ds1` — and the full
  `--help` flags, including the `-d` / `--bypass-plugins`
  escape hatches quoted in chapter 16 (`t04`). Help for the
  shipped tools `ardour8-new_session`, `ardour8-new_empty_session`,
  `ardour8-export`, `ardour8-copy-mixer` and the Lua interpreter
  (`t05`).
- Through the standalone Lua interpreter: engine created, Dummy
  backend selected and confirmed by name, session created and
  loaded, audio track added, the **ACE Compressor** inserted
  into its processor chain, record-armed roll for ~4 s, stop
  keeping the take, session saved (`t22`; probes in `t09`,
  `t13`, `t18`, `t20`).
- The session folder on disk: `FirstTake.ardour` XML read
  directly — Source entries for the two take files, the Region
  element naming both source IDs, its superclock length
  (1,091,233,920 ticks = 185,584 samples at 48,000 Hz)
  cross-checked against `soxi`'s independent count of the
  files (`t27`). The session file itself is kept at
  `ardour-lab/FirstTake.ardour`.
- `ardour8-new_session` creating a session at 48,000 Hz, and
  reporting an empty template list for this build (`t21`).
- **The export, measured three ways** (`t29`, `t30`):
  `ardour8-export` rendered the session to a 48,000 Hz stereo
  16-bit WAV of 185,587 frames (3.866 s), and the lab's own
  script `ardour-lab/check-mix.py` measured both channels at
  peak 0.4999 (−6.02 dBFS), RMS 0.3534 (−9.04 dBFS — the
  sine-wave relationship, peak ÷ √2), with zero crossings
  estimating 439.9 Hz against the 440 Hz fixture.
- A fresh interpreter loading the saved session and confirming
  the region on the playlist, the LV2 plugin inventory of the
  package (seven bundles: ACE Compressor, EQ, Expander, Delay,
  Reverb, a-fluidsynth, Reasonable Synth) and the
  ACE Compressor present in the chain (`t31`, `t32`); the track's full
  ten-processor chain enumerated (`t32`).
- The full graphical program launched under a virtual display,
  reaching the first-run Welcome wizard; startup log and
  screenshot kept (`t33`, `ardour-lab/gui-welcome-wizard.png`);
  the log shows 459 MIDI patch files loaded.

Disclosed fixture swap (chapter 11, in the text): the Dummy
backend records only silence, and 8.4's scripting provably
cannot import an audio file (below). To prove the export path
carries *signal*, the lab replaced the samples **inside** the
two recorded take files with a generated 440 Hz tone at half
scale — same filenames, same format, same 185,584-frame
length; the session file was never edited (`t28` records
levels 0.000000 → 0.499878 before export). From the program's
side this is indistinguishable from the microphone having
heard a tone; the guide says so rather than implying a
recording of one.

Boundaries hit and kept verbatim:

- **No scriptable import in 8.4.** `Session` has no import
  method; `ARDOUR.RegionFactory` exposes only cloning and
  lookup; the one import routine, `Editor:do_import`, belongs
  to the graphical editor object — confirmed both by probing
  the interpreter (transcripts `t09`–`t19`) and in the
  project's official Lua class reference.
- **A wrongly-shaped Lua call segfaults the interpreter**
  (exit 139; transcripts `t13`–`t18`) — the processor-adding
  call with invented arguments crashed where the documented
  `add_processor_by_index` shape worked. Chapter 12 teaches
  the caution; nothing was hidden.
- The wizard was reached but not clicked through: later pages
  and opening the session in the editor window are described
  from the manual, and the screenshot shows exactly the step
  that was reached.

Documented only — described from the official manual and the
project's site for the taught version, not run, and the text
does not claim otherwise:

- Recording with a real interface: input routing, levels,
  monitoring, punch and loop recording as musical acts.
- All judgements by ear: mix quality, plugin sound, latency as
  *felt* while performing.
- Graphical editing and mixing work beyond the wizard: the
  operations in chapter 7 are specified by the session model
  (whose region attributes are quoted from a real file) and
  the manual, not performed with a mouse in the lab.
- MIDI composition and performance; the piano roll; external
  MIDI hardware and its patch names.
- VST3 plugins (the scanner ships in the tree; no VST3 plugin
  was installed or loaded) and LADSPA beyond its mention.
- Loudness-target exports for delivery (LUFS normalisation in
  the graphical export dialog); the lab's measurements are
  peak/RMS/pitch of a known fixture.
- Version 9 features (clip recording, separate piano-roll
  windows, region effects), and building Ardour from source.
- The neighbour tools of chapter 14 — characterised, not run
  or benchmarked here (Audacity and ffmpeg have their own
  guides in this series).

Fixtures are this guide's own and deliberately generic: one
session named FirstTake, one track named Tone, a 440 Hz
concert-A tone generated by ffmpeg, and silence recorded from
a pretend device. No names, organisations, or real events.
