import numpy as np
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

def wav2np(path_file, skiped_samples = 1):
    """
    INPUT:
        path_file       -> path to the wav file
        skiped_samples  -> skip samples to minimize the size of the numpy array

    path_file = "./data/speech-01.wav"
    skiped_samples = 50
    npfile = wav2np(path_file, skiped_samples)
    print(len(npfile))

    plt.plot(npfile)
    plt.show()
    """    
    wav_file = read(path_file)
    return np.array(wav_file[1], dtype=float)[::skiped_samples]
