import librosa
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import streamlit as st

# import pandas as pd
# import plotly.express as px

@st.cache()
def process_signal_PCA(filename:str):

    # Load the audio file
    y, sr = librosa.load(filename)

    # Split the audio into 3-second segments
    segment_length = 3 * sr  # 3 seconds in samples
    segment_starts = np.arange(0, len(y) - segment_length + 1, segment_length)
    segment_ends = segment_starts + segment_length
    segments = [y[start:end] for start, end in zip(segment_starts, segment_ends)]

    # Calculate the MFEs for each segment
    MFEs = [librosa.feature.melspectrogram(y=segment, sr=sr) for segment in segments]

    # Stack the MFCC arrays into a single array
    MFEs_stack = np.stack(MFEs)

    # Reduce the dimensionality of the MFCCs using PCA
    pca = PCA(n_components=2)
    MFEs_pca = pca.fit_transform(MFEs_stack.reshape(-1, 40))

    return MFEs_pca

@st.cache()
def process_signal_tSNE(filename:str):

    # Load the audio file
    y, sr = librosa.load(filename)

    # Split the audio into 3-second segments
    segment_length = 3 * sr  # 3 seconds in samples
    segment_starts = np.arange(0, len(y) - segment_length + 1, segment_length)
    segment_ends = segment_starts + segment_length
    segments = [y[start:end] for start, end in zip(segment_starts, segment_ends)]

    MFEs = [librosa.feature.melspectrogram(y=segment, sr=sr) for segment in segments]

    # Stack the MFCC arrays into a single array
    MFEs_stack = np.stack(MFEs)

    # Reduce the dimensionality of the MFCCs using t-SNE
    tsne = TSNE(n_components=2)
    MFEs_tsne = tsne.fit_transform(MFEs_stack.reshape(-1, 40))

    return MFEs_stack


