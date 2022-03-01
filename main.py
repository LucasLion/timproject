import math
import matplotlib.pyplot as plt
from file_manager import *

filename = "pouet3.wav"
threshold = 100

def normalize_samples(samples, max_value):
    normalized_samples = []
    max_sample = 0
    for sample in samples:
        if abs(sample) > max_sample:
            max_sample = abs(sample)
    for sample in samples:
        normalized_sample = sample * 1000 / max_sample
        normalized_samples.append(normalized_sample)
    print(normalized_samples)
    return normalized_samples

# lecture du fichier wav
wav_samples = wave_file_read_samples(filename)

if not wav_samples:
    print("ERREUR: Aucun sample à la lecture du fichier wav")
    exit(0)
# normaliser
normalized_samples = normalize_samples(wav_samples, threshold)

logs = []
for i in normalized_samples:
    if -threshold < i < threshold:
        logs.append(f"Value Drop: {i}")
    else:
        logs.append('ok')

with open("log_file.txt", 'w') as f:
    for log in logs:
        f.write(log + "\n")
    f.close()

wav_samples_abs = [abs(sample) for sample in wav_samples]
normalized_samples_abs = [abs(sample) for sample in normalized_samples]
sq = math.sqrt(144)
plt.plot(normalized_samples)
# plt.plot(logs)
# plt.axhline(y=threshold, color="r")
plt.show()
