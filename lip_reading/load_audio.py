import librosa
import numpy as np

audio_path = 'lip_reading/test.mp3'
y, sr = librosa.load(audio_path, sr=16000)

mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
mfccs = np.mean(mfccs.T, axis=0)