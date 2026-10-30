# Getting Ardour

There are three honest ways to get Ardour, and they differ in version, price and who supports the result. This chapter lays them side by side, because the difference matters: at the time of writing, Ardour's own site offers the **9 series** (9.8, August 2026), while this guide teaches **8.4.0** — the version Ubuntu 24.04's package archive carries. Everything in this guide was verified against 8.4.0. Features that arrived in version 9 — clip launching, separate piano-roll windows, region effects — are real, but they are not in the program this guide runs, and the guide does not teach them as if they were.

## Way one: the official builds (pay what you can)

Ardour's developers sell ready-made, supported downloads for Linux, macOS and Windows from ardour.org — on an unusual arrangement that deserves stating exactly:

- The program is free software (GPL). There is **no licence fee** and the downloaded program is yours to keep and run forever.
- To download a ready-built copy you are asked to **pay what you can** — a single payment of any amount you choose (the floor is one dollar), or a monthly subscription if you would rather spread it out.
- Paying at least $45 in one payment, or subscribing, also gets you the **next major version** and the nightly test builds; paying less still gets you the current version in full.

This is the project's income, and it is why the program exists in its current shape. If Ardour becomes a tool you rely on, this is the route that keeps it alive — and the only route where the developers support the exact binary you are running.

## Way two: your distribution's package

Every major Linux distribution packages Ardour, free of charge, installable like anything else:

```
sudo apt install ardour        # Debian / Ubuntu
```

What you get is whatever version your distribution froze when it built its release. Ubuntu 24.04 carries **Ardour 8.4.0** (package version `1:8.4.0+ds1-2ubuntu8`); the last 8-series release upstream was 8.12, and version 9 arrived in February 2026. Distribution packages also split Ardour into pieces: on Ubuntu the program, its data files and its bundled LV2 plugins arrive as three packages (`ardour`, `ardour-data`, `ardour-lv2-plugins`), installed together as dependencies.

The honest trade: the package is free, effortless, and built to fit your system — and it is a version or two behind, and if it misbehaves your first call is your distribution, not Ardour's developers. For learning the program — everything in this guide — 8.4 is entirely sound. Professionals who need the current version take way one.

## Way three: build the source

The source code is public and free (it is GPL software; GitHub mirrors it and the project's own git server hosts it). Ardour's download page is candid about this route: building is "a challenging and complex process, especially on Windows and macOS", the project provides **no help** for it and cannot support the result. This guide did not build Ardour and does not teach it; it is the route for people who want to modify the program or join its development.

## What this guide's lab actually did

The lab intended to install the Ubuntu package the ordinary way and was stopped by the machine itself — the lab computer is shared, and another user's package operation held the lock:

```
E: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 74887 (apt-get)
```

(Transcript `ardour-lab/transcripts/t01-apt-install.txt`.) Rather than disturb the other work, the lab downloaded the very same `.deb` files the package manager would have used — 37 packages, Ardour and everything it depends on that was not already present — unpacked them into a private folder, and ran the identical files from there with the library path pointed at them. Nothing was installed system-wide, and every claim in this guide comes from those exact Ubuntu binaries. On your own machine, `sudo apt install ardour` is the whole story; the lab's detour is recorded here, and in `criteria.md`, because a guide's evidence should say where it came from.

The version check that proves the program is really there (transcript `t04`):

```
$ ardour8 --version
Ardour8.4.0~ds1 (built using 8.4.0~ds1-2ubuntu8 and GCC version 13.2.0)
```

Ubuntu names the command `ardour8` (older releases used `ardour6`, `ardour7` — the number follows the major version). The same package also installs the command-line companions this guide uses later: `ardour8-new_session`, `ardour8-export` and `ardour8-lua` (chapters 5, 11 and 12).

## The first run: a short wizard, then a decision

Launched with a screen, Ardour 8.4 opens with a **Welcome wizard** — the lab launched the full graphical program under a virtual display and met it there (screenshot kept as `ardour-lab/gui-welcome-wizard.png`). Its first page says what the program is for and offers a GUI and font scaling setting. The pages after it ask for the few things Ardour needs to know once: where new sessions should live by default, and how you intend to monitor what you record. None of it is binding — every choice can be changed later in Preferences — so the right way through the wizard is to read each page, accept the sensible defaults, and finish.

After the wizard, opening or creating a session raises the **Audio/MIDI Setup** dialog: which backend, which device, which sample rate, which buffer size. That dialog is where chapter 4 begins — and it is a decision worth a chapter, because the same dialog is also where most first-session confusion lives.

**Check before you move on:** `ardour8 --version` prints a version, and you can say which of the three ways you got the program — and, if it was the package, why its version number is not the one on Ardour's home page.
