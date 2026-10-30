# Audio Backends

A backend is the engine's driver: the module that carries sound between Ardour and the outside world. You choose one every time a session starts, in the Audio/MIDI Setup dialog, and the choice decides what Ardour can hear, what it can play through, and how quickly it answers. This chapter explains the choice, the two numbers that come with it, and the pretend backend this guide's lab used for everything.

## The four backends in the Linux build

Ardour 8.4's Ubuntu package ships four backend modules — the lab listed them in the installed tree (`libalsa_audiobackend.so`, `libjack_audiobackend.so`, `libpulseaudio_backend.so`, `libdummy_audiobackend.so`):

- **ALSA** talks straight to the Linux kernel's sound drivers. If you have one audio interface and want the shortest, simplest path to it, this is the normal choice for recording on Linux.
- **JACK** talks to the JACK sound server instead. JACK exists for studios: it lets several programs run against one device at once and patch sound between them (Ardour into a standalone effect, a drum machine into Ardour) with sample-accurate timing. If you do not need that routing, you do not need JACK; if you do, nothing else replaces it.
- **PulseAudio** talks to the standard desktop sound server — the one already playing your browser videos. It is the convenient way to get sound out of Ardour on a laptop with no setup, and the wrong tool for careful recording: it is built for convenience, resamples freely, and its delays are large and variable.
- **Dummy** — shown in the program as **None (Dummy)** — is a pretend device. It runs the engine on an internal clock, offers pretend inputs and outputs, and produces perfect silence. It exists so the program can be tested, demonstrated and run on machines with no audio hardware at all.

On macOS the corresponding choice is CoreAudio; on Windows, ASIO (with your interface maker's driver). The shape of the decision is the same everywhere: one backend, one device, per session.

## The two numbers

Every backend asks for the same two settings:

- **Sample rate** — how many times per second the audio is measured: 44,100 (CD rate) or 48,000 (the video and broadcast rate) cover nearly all work. The rule that matters: everything in a session — interface, files, Ardour — runs at the session's one rate, so pick it when the session is created and leave it alone. This guide's lab worked at 48,000 throughout.
- **Buffer size** — how much audio the engine moves per trip, in samples: 64, 128, 256, 512, 1024… Small buffers mean low **latency** (the delay between playing a note and hearing it back through Ardour — at 48,000 Hz, a 128-sample buffer is about 2.7 milliseconds of the journey), but give the computer less slack: miss a deadline and the audio cracks — an **xrun**, chapter 16's home ground. Large buffers are forgiving and fine for mixing, where nobody is listening to themselves live. The working habit: record with the smallest buffer that runs cleanly, mix with a big one.

Ardour will also refuse, or convert, when things disagree — a session created at 48,000 Hz opened with the device set to 44,100 Hz is a classic first-day puzzle; the setup dialog is where you see it and set it right.

## Why the Dummy backend matters to you

The Dummy is a laboratory instrument, and this guide used it as one. With it, the lab could:

- start the real engine and run real sessions on a machine with **no sound hardware** (transcript `t09` shows the engine reporting its backend as `Dummy`);
- record a genuine take — the transport rolled, the recorder wrote real files, a real region appeared — whose content is silence, because a pretend microphone hears a pretend room (chapter 6);
- export a mix and measure it, since exporting needs the engine and the session but not a speaker (chapter 11).

For you, the same door opens on any machine: a laptop on a train, a computer whose interface is elsewhere, a first exploration before any hardware arrives. Choose **None (Dummy)** in the setup dialog and the whole program — editor, mixer, plugins, scripting — works; only the sound is imaginary. It is also the honest limit of this guide's lab, stated once here and again in `criteria.md`: every procedure that needs real ears or a real interface is labelled documented-only wherever it appears.

## Choosing, in one paragraph

One interface, recording: **ALSA**, 48,000 Hz, 256 samples to start. Routing between programs: **JACK**. Just want it to make noise through the laptop speakers while you explore: **PulseAudio** and no shame. No hardware, testing, scripting, or following this guide's lab exactly: **Dummy**. You can change backend only while no session is open — closing the session and reopening it on another backend is the normal move, and sessions remember nothing about the choice that would trap you.

**Check:** in the Audio/MIDI Setup dialog you can name the backend you are on, its device, the session's sample rate, and the buffer size — and say in one sentence what each of the last two trades away.
