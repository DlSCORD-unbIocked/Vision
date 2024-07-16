import librosa
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_io as tfio
from g2p_en import G2p
import os


'''
@inproceedings{peplinski21_interspeech,
  author={Jacob Peplinski and Joel Shor and Sachin Joglekar and Jake Garrison and Shwetak Patel},
  title={{FRILL: A Non-Semantic Speech Embedding for Mobile Devices}},
  year=2021,
  booktitle={Proc. Interspeech 2021},
  pages={1204--1208},
  doi={10.21437/Interspeech.2021-2070}
}
}'''

#y = audio signal (numpy array) and sr = sample rate

current_dir = os.getcwd()

audio_path = os.path.join(current_dir, "test.wav")

try:
    y, sr = librosa.load(audio_path, sr=16000)
except FileNotFoundError:
    print("Audio file not found. Please check the path and try again.")
    exit(1)
except Exception as e:
    print("An error occurred while reading the audio file: ", e)
    exit(1)

mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
mfccs = np.mean(mfccs.T, axis=0)

model = hub.KerasLayer("https://tfhub.dev/google/nonsemantic-speech-benchmark/trill/3")

waveform = tf.convert_to_tensor(y, dtype=tf.float32)
waveform = tf.reshape(waveform, [1, -1])

embeddings = model(waveform)['embedding']

transcript_path = os.path.join(current_dir, "transcript.txt")

try:
    with open(transcript_path, 'r') as file:
        text = file.read()
except FileNotFoundError:
    print("Transcript file not found. Please check the path and try again.")
    exit(1)
except Exception as e:
    print(f"An error occurred while reading the transcript file: {e}")
    exit(1)

g2p = G2p()

phonemes = g2p(text)

print(phonemes)