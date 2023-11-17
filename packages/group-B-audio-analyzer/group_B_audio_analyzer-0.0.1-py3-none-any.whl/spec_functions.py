import numpy as np
import matplotlib.pyplot as plt

def wiener_filter(array):
	with open('wiener_parameters.npy', 'rb') as f:
	    h = np.load(f)
	return np.convolve(array, h, mode="same")
	

def get_spectrogram(
    array, sample_rate=44100
):  # INPUTS: 1D ARRAY, the default sample rate is 44.1kHz, the standard for a WAV file
    spec, freq, t, image = plt.specgram(
        wiener_filter(array), Fs=sample_rate
    )

    return [spec, freq, t]


def plot_spectrogram(array, sample_rate=44100):
    spec, freq, t, image = plt.specgram(
        wiener_filter(array), Fs=sample_rate
    )

    plt.show()


"""

INPUT
npfile->  1D array

spec = get_spectrogram(npfile)

print(spec[0])
print(spec[1])
print(spec[2])

plot_spectrogram(npfile)

"""
