import numpy as np
from scipy import signal
from scipy.optimize import least_squares
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
from .white_noise import whitenoise_creator, put_white_noise
from .read_wav import wav2np


def model(h, y):
    """
    Convolution between the Wiener filter and some input signal

    Parameters:
    -----------
    h : numpy array
        parameters of the wiener filter
    y : numpy array
        noisy input signal to be filtered

    Returns:
    --------
    numpy array
        output of the wiener filter, result of the convolution between noisy signal and wiener filter

    Examples:
    ---------
    data_path1 = "../data_source/music/music-01.wav"
    music_fil1 = wav2np(data_path1)
    data_path2 = "../data_source/other/other-01.wav"
    music_fil2 = wav2np(data_path2)
    data_path3 = "../data_source/speech/speech-01.wav"
    music_fil3 = wav2np(data_path3)
    x1 = np.concatenate((music_fil1, music_fil2, music_fil3))

    n_param = 10  # Number of parameters of the Wiener filter
    h0 = np.random.uniform(-10, 10, n_param)
    y = put_white_noise(x1)
    res = least_squares(fun, h0, args=(x1, y), verbose=1)
    x2 = model(res.x, y)

    print("Parameters of the Weiner filter = {}. ".format(res.x))
    dif1 = np.sum(np.abs(y - x1))
    print("Absolute difference between noisy and noiseless signal = {}.".format(dif1))
    dif2 = np.sum(np.abs(x2 - x1))
    print("Absolute difference between filtered and noiseless signal = {}.".format(dif2))
    print("Improvement = {}.".format(dif1 / dif2))

    with open('wiener_parameters.npy', 'wb') as f:
        np.save(f, res.x)

    # Plotting noiseless, noisy and filtered signals
    fig, axs = plt.subplots(1, 3, sharey=True)
    axs[0].plot(x1)
    axs[1].plot(y)
    axs[2].plot(x2)
    plt.show()    
    """
    x2 = np.convolve(y, h, mode="same")
    return x2


def fun(h, x, y):
    """
    Difference between noisy and noiseless signal
    """
    return model(h, y) - x