import pyaudio
import wave
CHUNK = 1024
SAMPLE_FORMAT = pyaudio.paInt16
CHANNELS = 2
FS = 44100
secs = 3
# TODO: test it and try to implement in ansychronous solution 
p = pyaudio.PyAudio()
stream = p.open(format=SAMPLE_FORMAT, 
                channels=CHANNELS,
                rate=FS,
                frames_per_buffer=CHUNK,
                input=True)
frames = [stream.read(CHUNK) for i in range(0, int(FS / CHUNK * secs))]

stream.stop_stream()
stream.close()
p.terminate()


wf = wave.open("output.wav", 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()
#print(p.get_default_host_api_info())
