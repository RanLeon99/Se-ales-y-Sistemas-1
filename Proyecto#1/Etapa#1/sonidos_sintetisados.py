#!/usr/bin/python3

import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from scipy.signal import hann

# Cargar los datos del archivo de audio
sample_rate, signal = wavfile.read('violin-C5.wav')

# Aplicar una ventana Hann a la señal
window = hann(len(signal))
signal = signal * window

# Calcular la transformada de Fourier de la señal original
t = np.arange(signal.shape[0])
freq = np.fft.fftfreq(t.shape[-1]) * sample_rate
sp = np.fft.fft(signal)

# Filtrar el espectro eliminando las frecuencias por debajo de 500 Hz
cutoff_freq = 500
sp[freq < cutoff_freq] = 0

# Aplicar la inversa de la transformada de Fourier para generar el nuevo sonido sintetizado
new_signal = np.fft.ifft(sp).real.astype(np.int16)

# Calcular la transformada de Fourier del nuevo archivo de audio
t_new = np.arange(new_signal.shape[0])
freq_new = np.fft.fftfreq(t_new.shape[-1]) * sample_rate
sp_new = np.fft.fft(new_signal)

# Filtrar el espectro eliminando las frecuencias por debajo de 500 Hz
sp_new[freq_new < cutoff_freq] = 0

# Guardar el nuevo archivo de audio
wavfile.write('new_violin-C5.wav.wav', sample_rate, new_signal)

# Graficar el espectro del nuevo archivo de audio sintetizado
plt.figure()
plt.plot(freq_new, abs(sp_new.real))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Spectrum of sintetizado violin-C5.wav')
plt.xlim((0, 2000))
plt.grid()

# Mostrar los gráficos
plt.show()