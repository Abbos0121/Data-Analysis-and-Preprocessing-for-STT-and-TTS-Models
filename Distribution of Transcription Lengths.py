from datasets import load_dataset
import librosa
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
import pandas as pd

# Load Common Voice dataset for Uzbek language
dataset = load_dataset("mozilla-foundation/common_voice_12_0", "uz")

# Расчёт длины транскрипций
texts = [row['sentence'] for row in dataset['train']]
text_lengths = [len(text.split()) for text in texts]

# Распределение длины транскрипций (Distribution of Transcription Lengths)
plt.figure(figsize=(10, 6))
sns.histplot(text_lengths, bins=50, kde=True)
plt.title("Distribution of Transcription Lengths")
plt.xlabel("Number of Words")
plt.ylabel("Frequency")
plt.show()
