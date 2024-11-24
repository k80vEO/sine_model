#file stuff
#will connect buttons from view to model
#so button functionality
from guistuff import *
from tkinter import filedialog

#importing a file
def get_file():
    file_path = filedialog.askopenfilename()
    #title="", filetypes=[(.wav), ()]
    return file_path
    #if file_path:
        #hiii

