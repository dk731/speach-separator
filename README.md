# Real-Time Voice Isolation from Noisy Environments Using X-Vector Embeddings and Spectrogram Processing

This project explores the potential for real-time filtration of an individual's voice from an arbitrary audio signal, leveraging the person's voice signature. The approach employs x-vector embeddings as voice signatures, owing to their demonstrated utility in unique voice feature extraction, ease of use, and small footprint. These embeddings are coupled with spectrogram representations of the audio input to capture contextual data and reduce latency, optimizing the model for real-time processing.

A model was constructed using a Convolutional Neural Network (CNN) with a mix of dense layers to process the spectrogram input, reducing dimensionality and capturing voice patterns. The model's output is a single column of the spectrogram, representing the filtered voice.

The model was trained on the Common Voice Corpus 1 English dataset, with over 20,000 unique speakers, using a custom audio loader to mix each audio sample with different types of noise, thus simulating a variety of real-world scenarios. The training process was performed on GPU accelerated environment.

The efficacy of this model could have significant implications for the field of audio processing, opening up new possibilities for voice isolation in noisy environments.
