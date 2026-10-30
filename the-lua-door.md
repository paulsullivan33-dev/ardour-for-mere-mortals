# The Lua Door

Ardour contains a programming language. The **Lua** interpreter built into the program can create and load sessions, add tracks and plugins, arm recording, roll the transport, rearrange regions, and react to events — and Ardour's own package turns parts of it into command-line tools. This guide's lab did most of its work through this door, so this chapter is a field report: what opened, what did not, and what to make of the difference.

## The three shapes of the door

- **Scripts inside the program.** Ardour ships dozens of ready-made Lua scripts — actions for the editor, snippets, DSP processors, and *hooks* that run when something happens (one bundled hook saves a fresh snapshot of the session every time an export finishes; the lab read its source). You run them from menus and the Lua Script Manager, and you can write your own: the manual carries a complete class reference for the API.
- **A standalone interpreter, `ardour8-lua`.** The Debian package installs a command that runs Ardour's engine with no windows at all — "Ardour at your finger tips…", its help says — taking a script file as its argument (transcript `t05`). Everything in this guide's lab ran through it.
- **Tools built on it.** `ardour8-new_session` and `ardour8-export` (chapters 5 and 11) are the same machinery wearing a fixed purpose.

## What the lab drove through it — all verified

The lab's main script is kept at `ardour-lab/lab-build-session.lua`; its run is transcript `t22`. In order, through the door went:

- **Choosing the backend**: `AudioEngine:set_backend("None (Dummy)", ...)` — after which the engine itself reported its backend as `Dummy`.
- **Loading a session** and reading its name and sample rate back.
- **Creating tracks**: a stereo audio track named `Tone`, created with the same call the program's own "Add Audio Track" script uses.
- **Adding a plugin**: the ACE Compressor, requested by name and inserted into the track's chain (chapter 10) — and still there on a fresh load.
- **Recording**: arm the track, enable session recording, roll the transport, wait four seconds of real time, stop and keep the take — which produced real files and a real region (chapter 6).
- **Introspection**: routes listed, playlists counted, processors enumerated (chapter 8's ten-processor chain came from here).

A second script (`ardour-lab/lab-verify-reload.lua`) reopened the saved session in a new interpreter and confirmed the region and the plugin chain had persisted — the round trip that separates "it printed OK" from "it is so".

## The wall: importing a file

One everyday operation is **not** behind the door in version 8.4, and the lab hit the wall three ways before believing it (transcripts `t11`–`t16`, and the project's own Lua class reference):

- The `Session` object has no import method — the names a programmer would guess are simply absent.
- `ARDOUR.RegionFactory`, which sounds like the factory for making regions, exposes only cloning and lookup — no way to create a region from a file.
- The one import routine that exists, `Editor:do_import`, belongs to the graphical **Editor** object — present only when the full program is running, not in the headless interpreter.

That is why chapter 11's tone reached the session by replacing the samples inside a recorded take's files rather than by importing a tone file: the recording path is scriptable end to end; the importing path, in this version, is a graphical act. Readers on version 9 should check the current class reference — the API grows — but in the taught program the wall stands exactly where the lab found it, and a script that needs imported audio must either pre-place it in a session by hand or drive the graphical program instead.

## Two cautions the lab paid for

Scripts are powerful enough to hurt. A wrongly-shaped call to a processor-adding function **crashed the interpreter outright** — segmentation fault, no Lua error, unsaved state gone (the lab's transcripts keep the corpse). The same wrong call written as the program's own scripts write it (`add_processor_by_index`, found in the shipped examples) worked first try. The lessons generalise: prefer imitating Ardour's bundled scripts to guessing signatures, wrap experiments in `pcall` (which catches Lua errors, though not crashes), and keep sessions saved before a script runs — the interpreter and the session live in the same process, so a script crash is a program crash.

And a smaller discovery worth its line: probing is a legitimate technique here. The interpreter is interactive (`ardour8-lua -i`), and the lab mapped much of the API by asking it questions — which globals exist (`create_session`, `load_session` and `close_session` are the interpreter's own gifts), what a call refuses and why. An API that answers *"bad argument #3 — number expected"* is an API you can explore safely, one refusal at a time.

**Check:** run `ardour8-lua` on a script that loads a session and prints its sample rate and its routes' names. If the output matches the session you see on screen, you hold the door handle.
