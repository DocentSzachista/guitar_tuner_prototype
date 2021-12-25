import numpy as np
from scipy import signal
class SoundProcessing:
    SAMPLE_FREQ = 44100
    def __init__(self) -> None:
        
        pass
    
    @staticmethod
    def process_signal( recording)->int:
        #pobieranie wielkości nagrania
        N=recording.shape[0]
        tukey_window=signal.tukey(N,0.01,True)
        #liczenie transformaty sygnału poddanego oknu Tukey'a
        #signal_fft=np.fft.rfft(recording[:,0]*tukey_window)
        signal_fft=np.fft.rfft(recording[:,0])
        signal_abs=abs(signal_fft) #czesc rzeczywista sygnalu
        #szukanie składowej częstotliwości o największym module widma - doszukiwanie się częstotliwości struny gitary
        maxModule= np.max(signal_abs)
        maxModuleIndex= np.where(signal_abs == maxModule)
        #stworzenie tablicy składowych częstotliwości
        freq_step= SoundProcessing.SAMPLE_FREQ/N
        freq_tab=np.arange(signal_abs.shape[0])
        freq_tab=freq_tab*freq_step
        #Zwracamy najwyższą składową częstotliwość 
        print(signal_abs)
        return freq_tab[maxModuleIndex[0]]