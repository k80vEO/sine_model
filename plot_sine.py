#matplotlib inline
#this code uses information provided on the L26 participation code and
#from a youtube video posted by Nelson Darwin Pak Tech
#https://www.youtube.com/watch?v=_M27BKcoWeM
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

#plt.figure(figsize=(6,6))
xvalues = np.arange(0, 12, 0.1)
#plt.subplot(2, 2, 1)
yvalues = np.sin(xvalues)
#plt.plot(xvalues, yvalues, color='blue')
#plt.xlabel('$x$')
#plt.ylabel('$sin(x)$')

#plt.grid(True)
#plt.show()

#plt.set_title('Sine Function')
#plt.tight_layout()
#plt.subplots_adjust(top=0.90)