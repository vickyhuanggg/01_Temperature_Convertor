from tkinter import *
from functools import partial #To prevent unwanted windows
import re
import random

class Converter:
    def __init__(self):
        #Formatting variables...
        background_color = "light blue"

        # In actual program this is blank and is populated with user calculations
        self.all_calc_list = ['5 degrees F is -15 degrees C',
                             '6 degrees F is -14.4 degrees C',
                             '7 degrees F is -13.9 degrees C',
                             '8 degrees F is -13.3 degrees C',
                             '9 degrees F is -12.8 degrees C']
        # self.all_calc_list = []

        #Converter Main Screen GUI...
        self.converter_frame = Frame(width=300, height=300, bg=background_color)
        self.converter_frame.grid()

        #Temperature Conversion Heading (row 0)
        self.temp_converter_label=Label(self.converter_frame,text="Temperature Converter", font=("Arial", "16", "bold"), bg=background_color, padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        #history Button (row1)
        self.history_button = Button(self.converter_frame, text="History", font=("Arial", "14"), padx=10, pady=10, command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=1)

        if len(self.all_calc_list) == 0:
            self.history_button.config(state=DISABLED)


    def history(self, calc_history):

        History(self, calc_history)

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="Please enter a number in the box "
                                     "and then push one of the buttons "
                                     "to convert the number to either "
                                     "degrees C or degrees F.\n\n"
                                     "The Calculation History area show "
                                     "up to seven past calculations "
                                     "(most recent at the toop). \n\nYou can "
                                     "also export your full calculation "
                                     "history to a text file if desired.")

class History:
    def __init__(self, partner, calc_history):
        background = "#a9ef99"  # Pale green

        #disable history button
        partner.history_button.config(state=DISABLED)

        #sets up child window(ie:history box)
        self.history_box = Toplevel()

        #if users press cross at top, closes history and 'realeases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))
        #set up child GUI Frame
        self.history_frame = Frame(self.history_box, width=300, bg=background)
        self.history_frame.grid()
        #Set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="Calculation History", font = "arial 19 bold", bg=background)
        self.how_heading.grid(row=0)
        #history text(label, row 1)
        self.history_text = Label(self.history_frame, text="Here are your most recent "
                                  "calculations. Please use the "
                                  "export button to create a text "
                                  "file of all your calculations for "
                                  "this session", font="arial 10 italic", fg="maroon",
                                  justify=LEFT, width=40, bg=background, wrap=250, padx=10, pady=10)
        self.history_text.grid(row=1)

        # History Output goes here..(row 2)
        # Generate string from list of calculations...
        history_string = ""
        if len(calc_history) >= 7:
            for item in range(0,7):
                history_string += calc_history[len(calc_history) - item - 1]+"\n"

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) - calc_history.index(item) - 1]+"\n"
                self.history_text.config(text="Here is your calculation "
                                         "history. You can use the "
                                         "export button to save this "
                                         "data to a text file if "
                                         "desired.")

        # Label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string,
                               bg=background,font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)


        # Export / Dismiss Buttons Frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady =10)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 12 bold", command=lambda: self.export(calc_history))
        self.export_button.grid(row=0, column=0)

        # Dismiss button (
        self.dismiss_btn = Button(self.export_dismiss_frame, text="Dismiss", width=10, highlightbackground=background , font="Arial 12 bold", command=partial(self.close_history, partner))
        self.dismiss_btn.grid(row=0, column=1)

    def close_history(self, partner):
        # put history button back to normal...

        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self, calc_history):
        Export(self, calc_history)



class Export:
    def __init__(self, partner, calc_history):

        background = "#a9ef99"

        # disable export button
        partner.export_button.config(state=DISABLED)

        # sets up child window(ie:export box)
        self.export_box = Toplevel()

        #if users press cross at top, closes export and 'realeases' export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))
        #set up child GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()
        #Set up Export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions", font ="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)
        #Export insturctioins(label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename "
                                 "in the box below "
                                 "and pree the Save "
                                 "button to save your "
                                 "calculation history "
                                 "to a text file.",
                                 justify=LEFT, width=40, bg=background, wrap=250)
        self.export_text.grid(row=1)

        # Warning text (label,row 2)
        self.export_text = Label(self.export_frame, text="If the filename "
                                 "you enter below "
                                 "already exists, "
                                 "its contents will "
                                 "be replaced with "
                                 "your calculation "
                                 "history", justify=LEFT, bg="#ffafaf", fg="maroon", font="Arial 10 italic", wrap=225, padx=10,pady=10)
        self.export_text.grid(row=2,pady=10)

        # Filename Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20, font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3,pady=10)

        #Error Message Labels
        self.save_error_label = Label(self.export_frame, text="", fg="maroon", bg=background)
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel Buttons(row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  command=partial(lambda: self.save_history(partner, calc_history)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)


    def save_history(self, partner, calc_history):
        # Regular expression to check filename is valid
        valid_char = "[A-Za-z0-9]"
        has_error = "no"

        filename = self.filename.entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"

            else:
                problem = ("(no {}'s allowed".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # Display error message
            self.save_error_label.config(text="Invalid filename -{}".format(problem))
            # change the entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()
        else:
            # If there are no errors, generate text file and then clost
            # add .txt suffix!
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")
            # add new line at end of each item
            for item in calc_history:
                f.write(item + "\n")

            # close file
            f.close()

            # close dialogue
            self.close_export(partner)


    def close_export(self, partner):
        #put export button back to normal...

        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

class Help:
    def __init__(self, partner):
        background ="orange"

        #disable help button
        partner.help_button.config(state=DISABLED)

        #sets up child window(ie:help box)
        self.help_box = Toplevel()

        #if users press cross at top, closes help and 'realeases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))
        #set up child GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()
        #Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions", font ="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)
        #Help text(label, row 1)
        self.help_text = Label(self.help_frame, text="", justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        #Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, highlightbackground="orange", font="arial 10 bold", command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        #put help button back to normal...

        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


#main routine
if __name__ =="__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()

