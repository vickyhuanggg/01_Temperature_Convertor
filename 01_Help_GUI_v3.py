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
        self.temp_converter_label=Label(self.converter_frame,text="Temperature Converter", font=("Arial", "16", "bold"), bg=background_color, padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        #Help Button (row1)
        self.help_button = Button(self.converter_frame, text="help", font=("Arial", "14"), padx=10, pady=10, command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")

class Help:
    def __init__(self, partner):
        background ="orange"

        #disable help button
        partner.help_button.config(state=DISABLED)

        #sets up child window(ie:help box)
        self.help_box = Toplevel()

        #set up child GUI Frame
        self.help_frame = Frame (self.help_box, width=300, bg=background)
        self.help_frame.grid()
        #Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text = "Help / Instructions", font ="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)
        #Help text(label, row 1)
        self.help_text = Label(self.help_frame, text=)

        #Dismiss button (row 2)
#main routine
if __name__ =="__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
