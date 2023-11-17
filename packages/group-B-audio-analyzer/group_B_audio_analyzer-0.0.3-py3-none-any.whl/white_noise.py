import numpy as np
import matplotlib.pyplot as plt


def whitenoise_creator(min=0, max=1, size=1000):
    """produce whitenoise with an specified size

    Args:
        min (int): minimum noise. Defaults to 0.
        max (int): maximum noise. Defaults to 1.
        size (int): size of white noise array. Defaults to 1000.

    Returns:
        array: white noise sequence
    """    
    
    
    white_noise = np.random.uniform(min, max, size)

    return white_noise


def put_white_noise(input):
    """put the white noise on the input array

    Args:
        input (array): the audio sequence array

    Returns:
        array: audio sequence plus the white noise
    """   
    
    length = len(input)
    delta = (np.max(input) - np.min(input)) / 10
    output = input + (whitenoise_creator(0, 1, length) - 0.5) * delta
    return output
