#!/usr/bin/python3


import scipy.io.wavfile as wav
import numpy as np

# Cargar las dos señales WAV
fs1, data1 = wav.read('piano-G5.wav')
fs2, data2 = wav.read('trumpet-G4.wav')

# Asegurarse de que las señales tengan la misma duración
min_len = min(len(data1), len(data2))
data1 = data1[:min_len]
data2 = data2[:min_len]

# Normalizar las señales para evitar la saturación de amplitud
data1_norm = data1 / np.max(np.abs(data1))
data2_norm = data2 / np.max(np.abs(data2))

# Realizar el overlay sumando las señales
data_overlay = data1_norm + data2_norm


# Guardar la señal resultante en un archivo WAV
wav.write('salida.wav', fs1, np.asarray(np.clip(data_overlay, -1, 1) * 32767, dtype=np.int16))
