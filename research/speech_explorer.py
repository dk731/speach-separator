import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.io import wavfile

#
#
# load own speach sample
samplerate, data = wavfile.read("../rec/own-hitch-read.wav")
