import math
import matplotlib.pyplot as plt
from file_manager import *

filename = "pouet3.wav"
threshold = 300
nthreshold = -300

def normalize_samples(samples, max_value):
    normalized_samples = []
    max_sample = 0
    for sample in samples:
        if abs(sample) > max_sample:
            max_sample = abs(sample)
    for sample in samples:
        normalized_sample = sample * max_value / max_sample
        normalized_samples.append(normalized_sample)
    return normalized_samples

# lecture du fichier wav
wav_samples = wave_file_read_samples(filename)

if not wav_samples:
    print("ERREUR: Aucun sample à la lecture du fichier wav")
    exit(0)
# normaliser


def get_values_over_thresholds(normalized_samples):
    logs = []
    for i in normalized_samples:
        if i > threshold:
            logs.append(f"Too High: {i}")
        elif i < nthreshold:
            logs.append(f"Too low: {i}")
    return logs

normalized_samples = normalize_samples(wav_samples, 1000)
logs_over = get_values_over_thresholds(normalized_samples)


with open("log_file_over.txt", 'w') as f:
    for log in logs_over:
        f.write(log + "\n")
    f.close()

def get_values_drops(normalized_samples):
    logs_drop = []
    for i in range(len(normalized_samples) - 1):
        if normalized_samples[i+1] - normalized_samples[i] > 10:
            logs_drop.append(f"Value Drop: {normalized_samples[i]}, sample {i}")
    return logs_drop

logs_drop = get_values_drops(normalized_samples)

with open("log_file_drop.txt", 'w') as f:
    for log in logs_drop:
        f.write(log + "\n")
    f.close()

plt.plot(normalized_samples)
plt.axhline(y=threshold, color="r")
plt.axhline(y=nthreshold, color="r")

plt.show()
