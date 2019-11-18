import numpy as np
import librosa
import os, re

def generate_spectrograms(in_folder, out_folder, regex):
    for actor_folder in os.listdir(in_folder):
        in_path = os.path.join(in_folder, actor_folder)
        out_path = os.path.join(out_folder, actor_folder)
        os.makedirs(out_path, exist_ok=True)

        for in_file in os.listdir(in_path):
            if regex.match(in_file):
                print(os.path.join(in_path, in_file))

                signal, sr = librosa.load(os.path.join(in_path, in_file), sr =44100)
                spectrogram = librosa.stft(signal, n_fft=512)

                magnitude = np.abs(spectrogram)
                phase = np.angle(spectrogram)
                spectrogram = np.concatenate((magnitude,phase), axis=0)

                np.savetxt(os.path.join(out_path, in_file.split('.')[0] + '.txt'), spectrogram, fmt='%.6f')

def ravdess():
    in_folder = 'ravdess-emotional-speech-audio'
    out_folder = 'spectrograms/ravdess'
    regex = re.compile('.+.wav')
    generate_spectrograms(in_folder, out_folder, regex)

def savee():
    in_folder = 'AudioData'
    out_folder = 'spectrograms/savee'
    regex = re.compile('[a-z]+0[1-3].wav')
    generate_spectrograms(in_folder, out_folder, regex)

def main():
    ravdess()
    savee()

if __name__=='__main__':
    main()


