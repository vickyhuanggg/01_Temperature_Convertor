from tkinter import *
from functools import partial #To prevent unwanted windows
import random

class Converter:
    def __init__(self):
        #Formatting variables...
        background_color = "light blue"

        #Converter Main Screen GUI...
        self.converter_frame = Frame(width=300, height=300, bg=background_color)
        self.converter_frame.grid()

        #Temperature Conversion Heading (row 0)
        self.temp_converter_label=Label(text="Temperature Converter", font=("Arial", "16", "bold"), bg=background_color, padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

#main routine
if __name__ =="__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
