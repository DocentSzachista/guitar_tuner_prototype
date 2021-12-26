from enum import Enum
from matplotlib import pyplot as plt
class Notations(Enum):
    """ Enum holding frequencies for given notations 
    
    """
    E=330.0
    B=249.6
    G=196.0
    D=146.8
    A=110.0
    E_MINOR=82.4

class Printer:
    """[summary]
    Class with printing utilities used in debug 
    
    """
    #przedział plus minus w jakiej będzie gicio mieć częstotliwość gitary docelowo ma być 1.5+
   
    @staticmethod
    def print_range(sound_main_frequency: float, OPT_VALUE = 1.5 ):
        """Print to which notation given frequency fits 

        Args:
            sound_main_frequency (float): Frequency to be compared
            OPT_VALUE (float, optional): Offset value that helps to 
            measure to which notation measured frequency fits. 
            Defaults to 1.5.
        """
       
            #funkcja porównująca w jakim przedziale jest dana struna
        if(sound_main_frequency>Notations.E_MINOR.value-OPT_VALUE 
       and sound_main_frequency<Notations.E_MINOR.value+OPT_VALUE):
            
            print(f" Value {sound_main_frequency}Corresponds to {Notations.E_MINOR} string")
            
        elif(sound_main_frequency>Notations.E.value+OPT_VALUE 
         and sound_main_frequency<Notations.A.value-OPT_VALUE):
            
            print(f" Value {sound_main_frequency} Corresponds between to {Notations.A} and {Notations.E} string")
            
        elif(sound_main_frequency>Notations.A.value-OPT_VALUE 
         and sound_main_frequency<Notations.A.value+OPT_VALUE):
        
            print(f" Value {sound_main_frequency} Corresponds to {Notations.A} string")
            
        
        elif(sound_main_frequency>Notations.A.value+OPT_VALUE 
         and sound_main_frequency<Notations.D.value-OPT_VALUE):
            
            print(sound_main_frequency, "You are in space between A and D string")
        
        elif(sound_main_frequency>Notations.D.value-OPT_VALUE 
         and sound_main_frequency<Notations.D.value+OPT_VALUE):
            
           print(f" Value {sound_main_frequency} Corresponds to {Notations.D} string")
        
        elif(sound_main_frequency>Notations.D.value+OPT_VALUE 
         and sound_main_frequency<Notations.G.value-OPT_VALUE):
            
            print(sound_main_frequency, "You are in space between D and G string")
        
        elif(sound_main_frequency>Notations.G.value-OPT_VALUE 
         and sound_main_frequency<Notations.G.value+OPT_VALUE):
            
            print(f" Value {sound_main_frequency} Corresponds to {Notations.G} string")
        
        elif(sound_main_frequency>Notations.G.value+OPT_VALUE 
         and sound_main_frequency<Notations.B.value-OPT_VALUE):
            
            print(sound_main_frequency, "You are in space between G and Notations.B.value string")
        
        elif(sound_main_frequency>Notations.B.value-OPT_VALUE 
         and sound_main_frequency<Notations.B.value+OPT_VALUE):
            
          print(f" Value {sound_main_frequency} Corresponds to {Notations.B} string")
          
        elif(sound_main_frequency>Notations.B.value+OPT_VALUE 
         and sound_main_frequency<Notations.E.value-OPT_VALUE):
            
            print(sound_main_frequency, "You are in space between Notations.B.value and Notations.E.value string")
        
        elif(sound_main_frequency>Notations.E.value-OPT_VALUE 
         and sound_main_frequency<Notations.E.value+OPT_VALUE):
            
            print(f" Value {sound_main_frequency} Corresponds to {Notations.E} string")
        
        elif(sound_main_frequency>Notations.E.value+OPT_VALUE):
            
            print(sound_main_frequency, "You are in space outside of Notations.E.value string turn, back") 

class Plotter:
    """ Utility class holding methods to make plots of data samples 
    """
    @staticmethod
    def plot_fft(frequencies_range : list,  samples : list) -> None:
        """Plots data of Fast Fourier Transform

        Args:
            frequencies_range (list): list of frequencies in range of 0 to fs/2 
            samples (list): samples magnitude
        """
        fig, ax = plt.subplots()
        ax.set_title("FFT")
        ax.set_xlabel("frequency [Hz]")
        ax.set_ylabel("samples magnitude")
       
        ax.stem(frequencies_range, samples, '.-')
        plt.show()
        
        
        
        
