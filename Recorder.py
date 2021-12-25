import numpy as np
import sounddevice as sd
class Recorder:
    
    def __init__(self) -> None:
        self._sampling_frequency = 44100
        self._dtype = 'float64'
        self._channels = 1
        
        
    def record(self, time = 2) -> list:
        
        # record given ammount of frames
        recording = sd.rec(int(self._sampling_frequency*time), self._sampling_frequency, self._channels, self._dtype)
        # wait until all frames are recorded
        sd.wait()
        
        # return them
        return recording

    def play(self, recorded, time=1) -> list:
        
        sd.play(recorded)
        sd.wait(time)




# from scipy.fft import fft, fftfreq

# # Number of sample points

# N = 600

# # sample spacing

# T = 1.0 / 800.0

# x = np.linspace(0.0, N*T, N, endpoint=False)

# y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)

# yf = fft(y)

# xf = fftfreq(N, T)[:N//2]

# import matplotlib.pyplot as plt

# plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))

# plt.grid()

# plt.show()