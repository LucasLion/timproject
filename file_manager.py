import wave


WAV_FORMAT_N_CHANNELS = 1  # mono
WAV_FORMAT_N_FRAMERATE = 44100
WAV_FORMAT_N_SAMPLE_WIDTH = 2  # 16bits

# byteLS -> [i] (Octet poids faible "least signifianct")
# byteMS -> [i+1] (Octet poids fort "most signifianct")
def get_16bits_sample_from_bytes(byteLS, byteMS):
    unsigned = byteLS + byteMS*256
    signed = unsigned
    if unsigned > 23767:
        signed = unsigned - 65536
    return signed

def get_16bits_samples_from_bytes(bytes):
    samples = []
    for i in range(0, len(bytes)-1, 2):
        sample = get_16bits_sample_from_bytes(bytes[i], bytes[i+1])
        samples.append(sample)
    return samples

def wave_file_read_samples(filename):
    wr = wave.open(filename, mode="rb")
    if wr.getnchannels() != WAV_FORMAT_N_CHANNELS:  # mono
        print("ERREUR: Utilisez un fichier mono")
        return None

    if wr.getsampwidth() != WAV_FORMAT_N_SAMPLE_WIDTH:
        print("ERREUR: Utilisez un fichier de 16 bits")
        return None

    if wr.getframerate() != WAV_FORMAT_N_FRAMERATE:
        print("ERREUR: Utilisez un framerate de 44100hz")
        return None

    nframes = wr.getnframes()
    frames_as_bytes = wr.readframes(nframes)

    #convertir les samples
    samples = get_16bits_samples_from_bytes(frames_as_bytes)
    wr.close()
    return samples


