# Troubleshooting

Symptoms first. Where the lab met the problem itself, the entry says so and points at the transcript.

**"Could not get lock … package manager" (installing anything).** Another package operation is running on the machine. The lab met this verbatim — `E: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 74887 (apt-get)` (transcript `t01`). Wait for it to finish; check with `ps` who holds it before concluding anything is stuck. Do not delete lock files to "fix" it.

**The Audio/MIDI Setup dialog appears every time / no sound device listed.** The engine has not started on a real backend. Pick a backend and device and start it (chapter 4); on a machine with no audio hardware, choose **None (Dummy)** deliberately rather than fighting for a device that is not there.

**Ardour opens a different program name than expected.** The command follows the major version: `ardour8` for the 8 series, `ardour7`, `ardour6` before it. `ls /usr/bin | grep ardour` shows what is installed — along with the useful companions `ardour8-export`, `ardour8-lua`, `ardour8-new_session`.

**The take recorded, but it is silent.** A family of causes, checked in this order: (1) the backend is **Dummy** — silence is its job; (2) the track's input is not the channel your source is plugged into; (3) the source or interface channel is muted or its gain is down; (4) the wrong device is selected in the setup dialog. Prove which one with arithmetic before re-recording: measure the file (`sox <file> -n stat`, or chapter 11's script) — all-zero maxima mean the zeros arrived *before* the file, not from your playing. The lab's own take is the worked example (chapter 6).

**Crackles, pops, and the xrun counter climbing.** An **xrun** is a missed deadline: the engine needed the next buffer before the computer delivered it. In order: raise the **buffer size** (chapter 4 — mixing tolerates 1024 easily); make sure the session rate matches the device rate; close other heavy programs; on laptops, use mains power and a performance power profile. *About special "realtime" kernels:* you will meet advice insisting one is required. It is not, for most setups — modern stock kernels handle Ardour's needs; what matters is that the audio work gets thread priority (the ALSA/JACK setup Ardour itself guides you through at first run) and a sane buffer. Treat a kernel swap as the last resort of a measured problem, not the first step of a new install.

**A session will not open, or opens wrong.** Rename the spare in: close Ardour, rename `<name>.ardour` aside, rename `<name>.ardour.bak` to `<name>.ardour`, reopen (chapter 5). Ardour also ships its own escape hatches, in its `--help`: open with all plugins disabled (`ardour8 -d`) to test whether a plugin is the blocker, and `--bypass-plugins` when asked to export or inspect without them.

**A plugin is missing, greyed out, or the session sounds different elsewhere.** The session names plugins the machine lacks (chapter 10). Open the **Plugin Manager** to see what is installed and what was blacklisted after a failed scan; rescan after installing anything new. A plugin that crashes its scan is listed there rather than loaded — that is the system working.

**The export is tiny, silent, or the wrong length.** Check the **session range** first: exports render between the session's start and end markers, not "the whole timeline as you see it". Then the master: a muted master or a solo left active elsewhere exports exactly that mistake. Then measure the file (chapter 11) — all-zero levels with the right duration point back to the session, not the exporter.

**A Lua script crashes the whole interpreter.** A wrongly-shaped call to certain functions can segfault the process instead of raising a Lua error (chapter 12). Imitate the bundled scripts' call shapes, wrap experiments in `pcall`, and save the session before running new script code against it.

**"No session templates found."** On the Ubuntu build, the template list is genuinely empty — this is normal for the package, not corruption (transcript `t21`). Build one session the way you like it and save it as your own template from inside the program.
