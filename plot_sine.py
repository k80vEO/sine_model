#matplotlib inline
#this code uses information provided on the L26 participation code and
#from a youtube video posted by Nelson Darwin Pak Tech
#https://www.youtube.com/watch?v=_M27BKcoWeM
import numpy as np
from scipy.signal import welch
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import os
from pydub import AudioSegment

file = "sound.wav"  #placeholder file name
#function for converting to .wav
def convert_wav():
    split_name = os.path.splitext(file)
    extension = split_name[1]
    if(extension == '.m4a'):
        #convert to wav
        file.export("filename.wav", format = "wav")



xvalues = np.arange(0, 12, 0.1)
yvalues = np.sin(xvalues)







#plt.figure(figsize=(6,6))
#plt.subplot(2, 2, 1)

#plt.plot(xvalues, yvalues, color='blue')
#plt.xlabel('$x$')
#plt.ylabel('$sin(x)$')

#plt.grid(True)
#plt.show()

#plt.set_title('Sine Function')
#plt.tight_layout()
#plt.subplots_adjust(top=0.90)