
from Notations import Printer
from Recorder import Recorder
from SoundProcessing import SoundProcessing
from Notations import Plotter


def main():
    print ("Do you want to record a sound? Y/N")
    x=input()

    if x=='Y' or x=='y':
        recorder = Recorder()
        
        while True:
            recording=recorder.record()[:,0]
            #recorder.play(recording)    
            freqs, samples=SoundProcessing.count_fft(recording)
            frequency=SoundProcessing.count_desired_frequency(freqs, samples)
            print(frequency)
            Plotter.plot_fft(freqs, samples )       
          #  Printer.print_range(guitar_string_freq[0])
           
    else:
        print("no recording")
        
if __name__ == '__main__':
    main()