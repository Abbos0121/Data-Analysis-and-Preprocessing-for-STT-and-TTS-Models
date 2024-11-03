
from datasets import load_dataset
import librosa
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
import pandas as pd

# Load Common Voice dataset for Uzbek language
dataset = load_dataset("mozilla-foundation/common_voice_12_0", "uz")

durations = [librosa.get_duration(filename=row['path']) for row in dataset['train']]

#Распределение длительностей аудио (Distribution of Audio Durations)
plt.figure(figsize=(10, 6))
sns.histplot(durations, bins=50, kde=True)
plt.title("Distribution of Audio Durations")
plt.xlabel("Duration (seconds)")
plt.ylabel("Frequency")
plt.show()
