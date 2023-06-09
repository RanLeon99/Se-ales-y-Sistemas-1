#!/usr/bin/python3

import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
plt.style.use('seaborn-dark')

sample_rate, middle_c = wavfile.read('violin-C5.wav') # cargar los datos del archivo de audio

#calcular la transformada de Fourier del archivo de audio
t = np.arange(middle_c.shape[0])
freq = np.fft.fftfreq(t.shape[-1])*sample_rate
sp = np.fft.fft(middle_c) 


## Graficar el espectro
plt.plot(freq, abs(sp.real))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Spectrum of violin-C5.wav')
plt.xlim((0, 2000))
plt.grid()

# Mostrar
plt.show()