# Recipes

Short, complete jobs. Each assumes the chapters behind it; each ends with the check that proves it worked.

## Back up a session so it can actually be restored

A session is a folder (chapter 5), so a backup is a copy of the folder — the whole folder, audio and all:

```
cp -r ~/Sessions/FirstTake /backup-drive/FirstTake-2026-10-30
```

Two failure modes to avoid. Copying only `FirstTake.ardour` copies the *description* and none of the music. And the `.ardour.bak` inside the folder is not a backup of anything but the previous save of that one file. **Check:** the copy's `interchange/<name>/audiofiles` holds the same files with the same sizes as the original (`diff -r` if you want certainty), and — the real test, once — open the *copy* and play it.

## Snapshot before the big edit

About to restructure the chorus, try the risky plugin chain, let a script loose on the session (chapter 12)? Take a **snapshot** first: *Session → Snapshot* in the program gives the session file a named sibling; if the experiment goes wrong, open the snapshot instead — same audio, earlier decisions. Snapshots cost almost nothing because the audio is shared. **Check:** the session folder contains both `<name>.ardour` and your snapshot's file, and the session dialog lists both.

## Archive a finished song

When a song is done, render the final mix at full quality (chapter 11), then archive the session itself. Ardour has a built-in *Session → Archive* that packs a session into a single file, optionally encoding the audio losslessly as FLAC to save space — the right shape for cold storage. The manual route also works: the backup recipe above, plus a `README` of your own in the folder naming the plugins used and the Ardour version, because the archive's one true dependency is a future machine that still has those plugins (chapter 10). **Check:** the archive plus its mix, copied elsewhere, with the plugin list written down. An archive you cannot reopen is a souvenir, not an archive.

## Run Ardour on a machine with no sound at all

Choose the **None (Dummy)** backend in the Audio/MIDI Setup dialog (chapter 4). Everything works — editor, mixer, plugins, recording, scripting — except that inputs are silence and outputs go nowhere. For no screen at all, the command-line trio does the same job: `ardour8-new_session` to create, `ardour8-lua` to work, `ardour8-export` to render. The lab ran this entire guide that way; the transcripts in `ardour-lab/` are the proof and the template. **Check:** the engine reports its backend as Dummy, the transport rolls, and an export measures like chapter 11's.

## Check a folder of exports in one pass

The measuring script from chapter 11 works on any WAV; run it over a folder and read the table it makes:

```
for f in exports/*.wav; do python3 ardour-lab/check-mix.py "$f"; done
```

Durations that match the sessions, peaks below 0 dBFS, and a pitch/level estimate where you expect one: a folder of mixes you have *verified*, rather than a folder of files with encouraging names. **Check:** no file reports all-zero levels unless silence is what that session contains.
