import matplotlib.pyplot as plt
import spec_functions
import read_wav
import audio_classifier
from os import walk
import numpy as np

speach_file = next(walk("../data_source/speech"), (None, None, []))[2]  # [] if no file
speach_file = ["../data_source/speech/" + s for s in speach_file]

music_file = next(walk("../data_source/music"), (None, None, []))[2]  # [] if no file
music_file = ["../data_source/music/" + s for s in music_file]

# other_file = next(walk("../data_source/other"), (None, None, []))[2]  # [] if no file
# other_file = ["../data_source/other/" + s for s in other_file]

filename = speach_file + music_file #+ other_file


type_map = {'speech': 0,
            'music': 1,
            'other': 2}


result = []
correct_classifying = 0
for file in filename:

    audio_wave = read_wav.wav2np(file)
    spectrogram, frequency, time = spec_functions.get_spectrogram(audio_wave)
    audio_type = audio_classifier.audio_classifier_threshold(spectrogram, frequency)
    if audio_type == file.split('/')[-1][:-7]:
        correct_classifying += 1
    result.append(type_map[audio_type])


print(correct_classifying)
