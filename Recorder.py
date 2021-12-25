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
