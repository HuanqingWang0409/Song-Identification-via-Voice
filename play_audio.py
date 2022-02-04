
import os
import re
import wave

import numpy as np
import pyaudio

class voice():
    def loaddata(self, filepath):
        if type(filepath) != str:
            print('the type of filepath must be string')
        p1 = re.compile('\.wav')
        if p1.findall(filepath) is None:
            print('the suffix of file must be .wav')
        try:
            f = wave.open(filepath, 'rb')
            params = f.getparams()
            self.nchannels, self.sampwidth, self.framerate, self.nframes = params[:4]
            str_data = f.readframes(self.nframes)
            self.wave_data = np.fromstring(str_data, dtype=np.short)
            self.wave_data.shape = -1, self.sampwidth
            self.wave_data = self.wave_data.T
            f.close()
            self.name = os.path.basename(filepath)
            return True
        except:
            print('File Error')

    def fft(self, frames=40):
        block = []
        fft_blocks = []
        self.high_point = []
        blocks_size = self.framerate / frames
        for i in range(0, len(self.wave_data[0]) - blocks_size, blocks_size):
            block.append(self.wave_data[0][i:i + blocks_size])
            fft_blocks.append(np.abs(np.fft.fft(self.wave_data[0][i:i + blocks_size])))
            self.high_point.append((np.argmax(fft_blocks[-1][:40]),
                                    np.argmax(fft_blocks[-1][40:80]) + 40,
                                    np.argmax(fft_blocks[-1][80:120]) + 80,
                                    np.argmax(fft_blocks[-1][120:180]) + 120,
                                    ))

    def play(self, filepath):
        chunk = 1024
        wf = wave.open(filepath, 'rb')
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        while True:
            data = wf.readframes(chunk)
            if data == "": break
            stream.write(data)
        stream.close()
        p.terminate()


if __name__ == '__main__':
    p = voice()
    p.play('record.wav')









