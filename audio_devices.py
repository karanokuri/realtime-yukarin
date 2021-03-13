from pprint import pprint
import pyaudio

def audio_devices():
    audio_instance = pyaudio.PyAudio()
    for i in range(audio_instance.get_device_count()):
        pprint(audio_instance.get_device_info_by_index(i))
        print()

if __name__ == '__main__':
    audio_devices()
