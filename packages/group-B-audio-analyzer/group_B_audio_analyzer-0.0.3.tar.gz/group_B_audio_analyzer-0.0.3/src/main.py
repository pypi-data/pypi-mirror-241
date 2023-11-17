import spec_functions
import read_wav
import audio_classifier
import sys


def main(audio_path):
    """

    Args:
        audio_path: string Path to audio file

    Returns:
        audio_type: string Classified type of the audio in file

    """
    audio_wave = read_wav.wav2np(audio_path)
    spectrogram, frequency, time = spec_functions.get_spectrogram(audio_wave)
    audio_type = audio_classifier.audio_classifier_threshold(spectrogram, frequency)

    return audio_type


if __name__ == "__main__":
    main(sys.argv[1])