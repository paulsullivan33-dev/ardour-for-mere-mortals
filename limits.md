# Limits

What Ardour — and this guide — will not do, collected in one place so nothing elsewhere has to be re-read with suspicion.

**The version taught is not the current version.** This guide teaches Ardour **8.4.0** from Ubuntu 24.04's packages. Ardour **9.x** exists (9.8 at the time of writing) and added, among other things, clip recording and launching, separate piano-roll windows, per-region effects and broader interface rework. Workflows here transfer; those specific features are absent from the taught program, and screenshots from the internet will sometimes show a program yours is not.

**This guide cannot hear.** The lab ran with no audio hardware and no listening of any kind; every claim about sound in these chapters is either a measurement (levels, durations, frequencies — chapter 11) or the manual's text. Nothing here grades a mix, a plugin's tone, or a performance, and chapters say "documented-only" wherever a judgement of the ear would be needed.

**Recording here is machinery, not music.** The lab recorded real takes through the real path, of silence, from a pretend device. A real session with your interface — levels, monitoring, room, performance — is the documented part, and no chapter pretends the lab tested your hardware.

**Ardour's scripting has a hard edge in 8.4.** Sessions, tracks, plugins, recording and transport are scriptable headlessly; **importing audio files is not** (the only import route lives in the graphical editor). Chapter 12 documents the wall and the workaround the lab used.

**One backend, one device, per session opening.** Ardour does not aggregate several interfaces into one pretend device, and changing backend means closing and reopening the session. Large studios plan around this; beginners mostly meet it as the setup dialog asking again.

**A session is not self-contained across machines.** It names its plugins; a machine lacking them loads placeholders. It can reference *external* files outside the folder. Chapter 13's archiving habits exist because portability is a practice, not a property.

**The program is dense.** Ardour exposes professional machinery — routing grids, latency compensation, a full tempo map — without hiding much of it. The learning curve is real, and the interface will not simplify itself for beginners. This is a limit of approachability, not of quality, and it is the one most likely to decide whether Ardour is *your* tool.

**The project's support boundary is explicit.** The developers support their own builds. The source is free to build, but ardour.org states plainly that they provide no help for doing so and cannot support the result; distribution packages are supported by their distributions in the first instance.

**Out of scope for this guide, not for Ardour:** video playback and sync (Ardour has a video timeline), surround and ambisonic mixing, hardware control surfaces beyond the basics, and live-performance clip workflows. They exist; they are each their own guide.
