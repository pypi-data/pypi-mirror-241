import numpy as np


def audio_classifier_threshold(spectrogram, frequency):
    """
    classify that the input spectrogram is human voice, music, or other kind of voice based on the frequency
    that maximum amplitude happened and comparing with the frequency range of each category.

    Args:
        frequency: 1_D array, array of all frequency
        spectrogram: 2-D array, spectrogram of audio file

    Returns:
        voice type:  string, specifies the category name
    """

    humane_range = (300, 4000)
    music_range = (20, 10000)

    minimum_frequency_index = np.argmax(np.max(spectrogram, axis=1))
    minimum_frequencies = frequency[minimum_frequency_index]

    if (minimum_frequencies > humane_range[0]) & (minimum_frequencies < humane_range[1]):
        voice_type = "speech"
    else:
        voice_type = "music"

    return voice_type
