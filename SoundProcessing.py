import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
import scipy
class SoundProcessing:

    SAMPLE_FREQ = 44100
    def __init__(self) -> None:
        
        pass
    
    @staticmethod
    def count_fft( recording: list) -> list :
        """ count Fast Fourier Transform using numpy's fft

        Args:
            recording (list): recorded sound that is to be processed

        Returns:
            list, list: signal magnitude, frequency range 
        """
        
        # obliczenie transformaty
        #recording = signal.savgol_filter(recording, 51, 3)
        x = np.fft.fft(recording)
        x_mag = np.abs(x)
        # wyliczenie kroku w przestzreni częstotliwości 
        freq_step = SoundProcessing.SAMPLE_FREQ / len(x_mag) 
        # wyciągnięcie wartości bezwzględnej 
         
        # Wyciągnięcie częstotliwości  - 1 sposób
        f = np.linspace(0, SoundProcessing.SAMPLE_FREQ - freq_step, len(x_mag))
        # Wyciągnięcie częstotliwości  - 2 sposób - korzystanie z funkcji 
       # f = np.fft.fftfreq(len(x), freq_step)* SoundProcessing.SAMPLE_FREQ
        # we are interested of returning fft of (sample frequency < 2) range - Nyquist freqyency
        return f[:len(f)//2], x_mag[:len(f)//2]
    
    @staticmethod
    def count_desired_frequency(freqs, sig_mag) -> float:
        """Looks for frequency that has the biggest pin (is the frequency we are looking for)

        Args:
            freqs (list): frequencies 
            sig_mag (list): signal frequencies magnitudes used to find the frequency with the largest pitch

        Returns:
            float: frequency that is played on instrument's string
        """
        max_magnitude = np.amax(sig_mag)
        max_freq_index = np.where(sig_mag == max_magnitude)
   
        
        max_freqs = freqs[max_freq_index[0]]
        return max_freqs
        


