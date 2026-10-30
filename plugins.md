# Plugins

A **plugin** is a small program that lives inside a track's processor chain and changes the sound passing through: compressors that tame loud parts, equalisers that reshape tone, reverbs that fake rooms, synthesisers that *are* the instrument on a MIDI track. This chapter covers the formats you will meet, the set that arrives with Ardour itself, and where a plugin sits in the chain — one chapter where the lab can show receipts for the loading, if not for the listening.

## The formats, in the order a Linux user meets them

- **LV2** — the free, native plugin standard of the Linux audio world and Ardour's own first choice. Plugins are small folders (bundles) ending in `.lv2`, found by the program in its plugin paths. If an effect exists as LV2, prefer it: it is the format Ardour's developers test most, and its state saves cleanly into the session file.
- **VST3** — the current Steinberg format, increasingly common from commercial makers with Linux builds. Ardour 8.4 ships its own scanner for them (`ardour-vst3-scanner` in the installed tree) and loads them in the same chain. The lab installed no VST3 plugin, so VST3 in this guide is described, not exercised.
- **LADSPA** — the older, simpler Linux format: elderly, widely available, effects only (no instruments, no fancy interfaces). Still loads, still useful.
- **VST2** — the previous Steinberg generation; supported, but licences kept it out of some builds, and new plugins are not made in it. Treat it as legacy.
- **Standalone Lua processors** — Ardour can run small plugins written in Lua, shipped as scripts (the program bundles some, such as a noise generator and a DTMF dialer). They are the gentlest way to learn what a processor *is*.

On Windows and macOS the same chain also loads VST3 and (on macOS) Audio Units. The rule that survives every platform: **a session file names its plugins; open the session on a machine without them and those slots load as inactive placeholders** — the session survives, the sound of those slots does not. Chapter 13's archiving recipe exists largely because of this sentence.

## What arrives in the box: the ACE set

Ardour's Ubuntu package carries a second package, `ardour-lv2-plugins`, with seven bundles (transcript `t31`), all from the **ACE** range (Ardour Community Effects) plus one instrument:

- **ACE Compressor**, **ACE EQ**, **ACE Expander** (a compressor's quieter cousin), **ACE Delay**, **ACE Reverb** — the working week of effects: dynamics, tone, space.
- **a-fluidsynth** — a SoundFont player: the instrument that makes MIDI tracks sound like pianos, strings and the rest of the General MIDI zoo (chapter 9).
- **Reasonable Synth** — the small always-available synthesiser.

The lab proved the loading end of this for real: by script, it asked for the **ACE Compressor** by name, received a live processor (the API answered "not nil"), inserted it into the track's chain at the standard position, saved the session, and — in a fresh load — found it still there, **eighth of ten processors**, between the track's Trim and its Fader (transcripts `t22` and `t32`). What the lab cannot report is how it *sounds*; no ears, remember. Parameter twiddling by ear is yours.

## Placement is meaning

Chapter 8's chain bears repeating here because it is the whole craft in one line: processors run **in order**, each one hearing the previous one's output. Reverb into a compressor is a different sound from compressor into reverb. Two working rules follow. Dynamics and EQ usually sit before the fader (they do — the fader is not a processor position you choose but the chain's fixed landmark), and time-based effects (reverb, delay) often live on a **bus fed by sends** (chapter 8) so several tracks share one room. When a plugin's own manual says "place after the EQ", it is speaking this language.

## Finding, installing and scanning

Further LV2 plugins install like other software — your distribution packages many (search its archive for `lv2` and names like Calf, LSP, x42) — and Ardour **scans** its plugin paths when it needs the list, which is why a newly installed plugin may need a rescan from the Plugin Manager before it appears. The Plugin Manager dialog (Window menu) is also where blacklisted, broken plugins are shown; a plugin that crashes its scan gets listed there rather than being allowed to take the program down — and chapter 16 uses that fact.

**Check:** open the Plugin Manager, find the ACE Compressor, add it to a track, and save and reopen the session: the slot, with its name, should still be in the chain — exactly the round trip the lab verified by script.
