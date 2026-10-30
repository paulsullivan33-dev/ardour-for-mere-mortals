#!/usr/bin/env python3
"""Measure an exported Ardour mix: format, levels, zero-crossing pitch check.
Stdlib only. Usage: check-mix.py FILE.wav"""
import math, struct, sys, wave

path = sys.argv[1]
w = wave.open(path, "rb")
n_ch, sw, rate, n_frames = w.getnchannels(), w.getsampwidth(), w.getframerate(), w.getnframes()
raw = w.readframes(n_frames)
fmt = {1: "b", 2: "h", 4: "i"}[sw]
samples = struct.unpack("<%d%s" % (n_frames * n_ch, fmt), raw)
full = float(2 ** (8 * sw - 1))
print(f"file: {path}")
print(f"format: {rate} Hz, {n_ch} channel(s), {8*sw}-bit PCM, {n_frames} frames = {n_frames/rate:.3f} s")
for ch in range(n_ch):
    data = samples[ch::n_ch]
    peak = max(abs(s) for s in data) / full
    rms = math.sqrt(sum((s / full) ** 2 for s in data) / len(data))
    crossings = sum(1 for a, b in zip(data, data[1:]) if (a < 0) != (b < 0))
    est_hz = crossings / 2.0 / (len(data) / rate)
    print(f"channel {ch+1}: peak {peak:.4f} ({20*math.log10(peak):.2f} dBFS), "
          f"RMS {rms:.4f} ({20*math.log10(rms):.2f} dBFS), zero crossings {crossings} -> ~{est_hz:.1f} Hz")
