# Task: Data Analysis and Preprocessing for STT and TTS Models

## Objective:

The candidate is required to analyze, preprocess, and extract insights from a Speech-to-Text (STT) and Text-to-Speech (TTS) dataset. The goal is to prepare the data for future model training and assess its quality and characteristics.

## Dataset:

    •	Use Common Voice for STT data.
    •	Use Firefox Common Voice dataset - specifically 'uz' section -- [hugginface](https://huggingface.co/datasets/mozilla-foundation/common_voice_12_0 )

## Requirements:

    1.	Data Exploration:
    •	Perform an initial exploration of the dataset:
    •	Analyze the distribution of audio file durations.
    •	Visualize the speaker demographics (age, gender, accent, etc.).
    •	Explore the text corpus (length of transcriptions, vocabulary size, common phrases).
    •	Generate basic visualizations:
    •	Histograms of audio duration.
    •	Word clouds for frequently occurring words in transcriptions.
    •	Spectrograms of random audio samples.
    2.	Data Quality Assessment:
    •	Identify any potential data issues:
    •	Missing transcriptions or audio files.
    •	Inconsistent or noisy transcriptions (e.g., wrong spelling or formatting).
    •	Audio files with poor sound quality (e.g., background noise, low volume).
    •	Provide suggestions on how to handle these issues (e.g., filtering out low-quality data, normalizing transcriptions).
    3.	Preprocessing:
    •	STT Task:
    •	Tokenize and clean text data (e.g., lowercase, remove special characters).
    •	Segment long audio files and align with transcriptions.
    •	Normalize audio (e.g., resampling, volume normalization).
    •	TTS Task:
    •	Clean and preprocess text for TTS (handle abbreviations, punctuation, and special characters).
    •	Segment text for speech synthesis (e.g., sentence-level segmentation).
    •	Provide phonemization or grapheme-to-phoneme conversion (if applicable).
    4.	Feature Extraction:
    •	STT Task: Extract relevant features from the audio files for potential model input (e.g., MFCC, Mel-spectrogram, Chroma features) using libraries like Librosa.
    •	TTS Task: Prepare text features for TTS, such as phonetic transcription (using libraries like g2p-en) and analyze the text for complexity (e.g., average word length, syllable count).
    5.	Error Analysis & Insights:
    •	Provide an analysis of the most common errors in the dataset (e.g., misaligned transcriptions, difficult-to-understand accents).
    •	Suggest data augmentation techniques that could be applied to improve future model performance (e.g., adding noise to audio, text paraphrasing).
    •	Provide insights into how speaker demographics (e.g., age, accent) might affect STT or TTS performance.
    6.	Bonus:
    •	Implement a simple data augmentation pipeline for the audio data (e.g., adding noise, time-stretching, pitch shifting).
    •	Suggest strategies for handling low-resource languages or accents (e.g., synthetic data generation).

## Submission:

    •	A Jupyter notebook or Python scripts with:
    •	Data exploration and visualizations.
    •	Preprocessing steps for both STT and TTS data.
    •	Error analysis and insights into the dataset quality.
    •	A brief report summarizing the approach, data quality assessment, and insights for improving data quality for future models.

## Additional Problems - simple

    1. Write a function to generate N samples from a normal distribution and plot the histogram. (Numpy, seaborn)
    2. Given a dataset of test_score, grade in different subjects and id in the dataset, write pandas code to return the cumulative percentage of students that received scores within the buckets of <50, <75, <90, <100. Dataset link -- [Dataset Link](https://www.kaggle.com/datasets/mexwell/student-scores)

# LEET CODE PROBLEMS

    1.	Two Sum (Easy): Problem ID 1
    2.	Group Anagrams (Medium): Problem ID 49
    3.	Valid Anagram (Easy): Problem ID 242
    4.	Median of Two Sorted Arrays (Hard): Problem ID 4
    5.	Top K Frequent Elements (Medium): Problem ID 347


