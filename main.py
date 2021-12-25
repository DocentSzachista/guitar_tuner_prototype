
from Notations import Printer
from Recorder import Recorder
from SoundProcessing import SoundProcessing


def main():
    print ("Do you want to record a sound? Y/N")
    x=input()

    if x=='Y' or x=='y':
        recorder = Recorder()
        
        while True:
            recording=recorder.record()
            recorder.play(recording)    
            guitar_string_freq=SoundProcessing.process_signal(recording)      
            #print(guitar_string_freq[0])
            Printer.print_range(guitar_string_freq[0])
            #compare(guitar_string_freq[0])        
    else:
        print("no recording")
        
if __name__ == '__main__':
    main()