#EJEMPLO DE GRABADORA DE SONIDO CON "pyaudio".
#IMPORTAMOS LIBRERIAS NECESARIAS
import pyaudio
import wave
import matplotlib.pyplot as plt
import numpy as np
import pyaudio
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import struct
from scipy.fftpack import fft
import sys
import time
from scipy.io import wavfile
import simpleaudio as sa
import os
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np

class AudioStream(object):
    def __init__(self):
    #DEFINIMOS PARAMETROS
        self.FORMAT=pyaudio.paInt16
        self.CHANNELS=2
        self.RATE=44100
        self.CHUNK=1024
        self.duracion=5
        self.archivo="grabacion.wav"
        self.pause = False
        #INICIAMOS "pyaudio"
        self.audio=pyaudio.PyAudio()
        #INICIAMOS GRABACIÓN
        self.stream=self.audio.open(format=self.FORMAT,channels=self.CHANNELS,
                    rate=self.RATE, input=True,
                    frames_per_buffer=self.CHUNK)
        
        
        self.llamar_menu()

    #MÉTODO que ejecuta el menú
    def llamar_menu(self):
        while True:
	    # Mostramos el menu
	        self.menu()
	    # solicituamos una opción al usuario
	        opcionMenu = input("inserta un numero valor >> ")
	        if opcionMenu=="1":
		        self.init_grabar()
	        elif opcionMenu=="2":
		        self.reproducir()
	        elif opcionMenu=="3":
		        self.init_plots()
	        else:
		        break
                
    
    #DEFINICIÓN MENÚ
    def menu(self):
	    os.system('cls') # NOTA para windows tienes que cambiar clear por cls
	    print ("Selecciona una opción")
	    print ("\t1 -   Grabar Audio")
	    print ("\t2 - Reproducir Audio")
	    print ("\t3- Graficas")
	    print ("\tpresiona cualquier tecla para salir")


    #MÉTODO para grabar el audio
    def init_grabar(self):
        print("grabando...")
        frames=[]

        for i in range(0, int(self.RATE/self.CHUNK*self.duracion)):
            data=self.stream.read(self.CHUNK)
            frames.append(data)
        print("grabación terminada")
    
        #DETENEMOS GRABACIÓN
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

        #CREAMOS/GUARDAMOS EL ARCHIVO DE AUDIO
        waveFile = wave.open(self.archivo, 'wb')
        waveFile.setnchannels(self.CHANNELS)
        waveFile.setsampwidth(self.audio.get_sample_size(self.FORMAT))
        waveFile.setframerate(self.RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
        time.sleep(2)


    #MÉTODO PARA REPRODUCIR
    def reproducir(self):
        print('reproduciendo...')
        wave_obj = sa.WaveObject.from_wave_file(self.archivo)
        play_obj = wave_obj.play()
        play_obj.wait_done()
    
    def init_plots(self):
        print("graficando")
        self.RATE, data = wav.read(self.archivo)
        fft_out = fft(data)
        
        plt.plot(data, np.abs(fft_out))
        plt.show()
        time.sleep(2)
        
if __name__ == '__main__':
    AudioStream()