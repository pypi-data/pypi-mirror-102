import numpy as np
import sounddevice as sd
def play():
    
    fs = 44100
    while True:
        data = np.random.uniform(-1, 1, fs)
        sd.play(data, fs)
if __name__=='__main__':
    play()
