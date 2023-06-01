#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import wave

def visualize(path: str):

    raw = wave.open(path)
    signal = raw.readframes(-1)
    signal = np.frombuffer(signal, dtype ="int16")

    f_rate = raw.getframerate()

    time = np.linspace(
        0,
        len(signal) / f_rate,
        num = len(signal)
    )

    plt.figure(1)
    plt.title("violin-C5")
    plt.xlabel("Time")
    plt.plot(time, signal)
    plt.show()

if __name__ == "__main__":
    visualize('violin-C5.wav')
