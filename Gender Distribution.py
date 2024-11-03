from datasets import load_dataset
import librosa
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
import pandas as pd

# Load Common Voice dataset for Uzbek language
dataset = load_dataset("mozilla-foundation/common_voice_12_0", "uz")

# Расчёт распределения пола
gender_dist = dataset['train'].to_pandas()['gender'].value_counts()

# Распределение пола (Gender Distribution)
plt.figure(figsize=(7, 5))
sns.barplot(x=gender_dist.index, y=gender_dist.values)
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Frequency")
plt.show()
