from datasets import load_dataset
import librosa
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
import pandas as pd

# Load Common Voice dataset for Uzbek language
dataset = load_dataset("mozilla-foundation/common_voice_12_0", "uz")

import librosa.display

# Спектрограмма MFCC (MFCC Spectrogram for Audio)
# Извлечение признаков MFCC и построение спектрограммы для одного примера
def extract_features(path):
    y, sr = librosa.load(path)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(mfccs, x_axis='time')
    plt.colorbar()
    plt.title('MFCC')
    plt.tight_layout()
    plt.show()

# Построение спектрограммы для первого аудиофайла
sample_features = extract_features(dataset['train'][0]['path'])
