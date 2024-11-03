from datasets import load_dataset
import librosa
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
import pandas as pd

# Load Common Voice dataset for Uzbek language
dataset = load_dataset("mozilla-foundation/common_voice_12_0", "uz")

# Создание облака слов
texts = [row['sentence'] for row in dataset['train']]
text_lengths = [len(text.split()) for text in texts]
all_text = " ".join(texts)
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_text)

# Облако слов (Word Cloud for frequent words)
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud for Frequent Words")
plt.show()
