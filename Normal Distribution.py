from datasets import load_dataset
import librosa
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
import pandas as pd

# Load Common Voice dataset for Uzbek language
dataset = load_dataset("mozilla-foundation/common_voice_12_0", "uz")

# Распределение нормального распределения (Normal Distribution)
# Генерация нормального распределения и построение графика
def generate_normal_samples(N):
    samples = np.random.normal(size=N)
    sns.histplot(samples, kde=True)
    plt.title("Normal Distribution")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()

# Построение графика нормального распределения
generate_normal_samples(1000)
