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
            [type]: [description]
        """
        
    
        
        
        # obliczenie transformaty
        x = np.fft.fft(recording)
        x_mag = np.abs(x)
        # wyliczenie kroku w przestzreni częstotliwości 
        freq_step = SoundProcessing.SAMPLE_FREQ / len(x_mag) 
        # wyciągnięcie wartości bezwzględnej 
         
        # Wyciągnięcie częstotliwości  
        f = np.linspace(0, SoundProcessing.SAMPLE_FREQ - freq_step, len(x_mag))
        
        return f, x_mag
    
    @staticmethod
    def count_desired_frequency(freqs, sig_mag) -> float:
        """Looks for frequency that has the biggest pin (is the frequency we are looking for)

        Args:
            freqs ([type]): [description]
            sig_mag ([type]): [description]

        Returns:
            float: [description]
        """
        max_magnitude = np.amax(sig_mag)
        max_freq_index = np.where(sig_mag == max_magnitude)
        print(max_freq_index)
        print(freqs[-1])
        max_freqs = freqs[max_freq_index[0]]
        return max_freqs
        


