from datasets import load_dataset
import librosa
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
import pandas as pd

# Load Common Voice dataset for Uzbek language
dataset = load_dataset("mozilla-foundation/common_voice_12_0", "uz")

# Расчёт распределения возраста
age_dist = dataset['train'].to_pandas()['age'].value_counts()

# Распределение возрастов (Age Distribution)
plt.figure(figsize=(7, 5))
sns.barplot(x=age_dist.index, y=age_dist.values)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
