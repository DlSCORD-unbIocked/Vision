import librosa
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_io as tfio
from g2p_en import G2p

audio_path = 'lip_reading/test.mp3'
y, sr = librosa.load(audio_path, sr=16000)

mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
mfccs = np.mean(mfccs.T, axis=0)

model = hub.KerasLayer("https://tfhub.dev/google/nonsemantic-speech-benchmark/trill/3")

waveform = tf.convert_to_tensor(y, dtype=tf.float32)
waveform = tf.reshape(waveform, [1, -1])

embeddings = model(waveform)

transcription = "placeholder for transcribed text"

g2p = G2p()

phonemes = g2p(transcription)
print("Phonemes: ", phonemes)
