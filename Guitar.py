import sounddevice as sd
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
fs=44100
duration = 1  # seconds
#const frequencies#
E=330.0
B=249.6
G=196.0
D=146.8
A=110.0
E_MINOR=82.4
#przedział plus minus w jakiej będzie gicio mieć częstotliwość gitary docelowo ma być 1.5+
optimalValue=1.5
def static():
    f=10
    overSample=40
    phase=0
    fs=overSampRate*f # sampling frequency
    t=np.arange(0,nCyl*1/f-1/fs,1/fs) 
    g=np.sin(2*np.pi*f*t+phase) # replace with cos if a cosine wave is desired
    return (t,g)
    
def record():
    #nagraj i zwróć sygnał
    #za pomocą funkcji .rec z biblioteki sounddevice .rec(długość nagrania, częstotliwość próbkowania, ilość kanałów, typ pobranych zmiennych ) - zwraca tablicę numpy
    myrecording = sd.rec(duration * fs, samplerate=fs, channels=1,dtype='float64')
    sd.wait(duration)
    return myrecording

def countfft(recording):
    #pobieranie wielkości nagrania
    N=recording.shape[0]
    tukey_window=signal.tukey(N,0.01,True)
    #liczenie transformaty sygnału poddanego oknu Tukey'a
    signal_fft=np.fft.rfft(recording[:,0]*tukey_window)
    signal_abs=abs(signal_fft) #czesc rzeczywista sygnalu
    #szukanie składowej częstotliwości o największym module widma - doszukiwanie się częstotliwości struny gitary
    maxModule= np.max(signal_abs)
    maxModuleIndex= np.where(signal_abs == maxModule)
    #stworzenie tablicy składowych częstotliwości
    freq_step=fs/N
    freq_tab=np.arange(signal_abs.shape[0])
    freq_tab=freq_tab*freq_step
    return freq_tab[maxModuleIndex[0]]
def compare(freq):
    #funkcja porównująca w jakim przedziale jest dana struna
    if(freq>E_MINOR-optimalValue and freq<E_MINOR+optimalValue):
        print(freq ,"Corresponds to e string")
    elif(freq>E_MINOR+optimalValue and freq<A-optimalValue):
        print(freq, "You are in space between e and A string")
    
    elif(freq>A-optimalValue and freq<A+optimalValue):
        print(freq ,"Corresponds to A string")
    elif(freq>A+optimalValue and freq<D-optimalValue):
        print(freq, "You are in space between A and D string")
    
    elif(freq>D-optimalValue and freq<D+optimalValue):
        print(freq ,"Corresponds to D string")
    elif(freq>D+optimalValue and freq<G-optimalValue):
        print(freq, "You are in space between D and G string")
    
    elif(freq>G-optimalValue and freq<G+optimalValue):
        print(freq ,"Corresponds to G string")
    elif(freq>G+optimalValue and freq<B-optimalValue):
        print(freq, "You are in space between G and B string")
    
    elif(freq>B-optimalValue and freq<B+optimalValue):
        print(freq ,"Corresponds to B string")
    elif(freq>B+optimalValue and freq<E-optimalValue):
        print(freq, "You are in space between B and E string")
    
    elif(freq>E-optimalValue and freq<E+optimalValue):
        print(freq ,"Corresponds to E string")
    elif(freq>E+optimalValue):
        print(freq, "You are in space outside of E string turn, back") 
print ("Do you want to record a sound? Y/N")
x=input()

if x=='Y' or x=='y':
    while True:
        recording=record()
        guitar_string_freq=countfft(recording)      
        compare(guitar_string_freq[0])        
else:
    print("no recording")
