'''Version1: display the GUI
version2: has error messages
version3: Celsius button enables history button as well as new error message has been updated
version4: The error message has now became a feedback message which act as a feedback to user if something goes wrong or it is alright
version5: the fahrenheit button functional added'''
from tkinter import *
from functools import partial # to prevent unwanted windows

class Converter:
    def __init__(self):

        # Common variables
        button_font = ("Arial", "12", "bold")
        button_fg = "white"

        # set up the GUI frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        # conversion, help, history/export buttons
        self.button_frame = Frame(padx=30, pady=30)
        self.button_frame.grid(row=0)

        # width is the width of the button
        self.history_button = Button(self.button_frame, text="History / Export", bg="#004C99", fg=button_fg, font=button_font, width=12, state=DISABLED, command=self.to_history)
        self.history_button.grid(row=1, column=1, padx=5, pady=5)

        # remove when integrating
        self.history_button.config(state=NORMAL)

    def to_history(self):
        HistoryExport(self)

class HistoryExport():

    def __init__(self, partner):
        # setup dialogue box and background colour
        self.history_box = Toplevel() # ig this is similar to root = Tk(). Making a new window but instead the window is created to the self.help_box within the class

        # disable the help button when clicked on
        partner.history_button.config(state=DISABLED)

        # if the users press cross at the top, closes help and releases help button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box, width=300, height=200)

        self.history_frame.grid()

        self.help_heading_label = Label(self.history_frame, text="History / Export", font=("Arial", "16", "bold"))
        
        self.help_heading_label.grid(row=0)

        history_text = '''Below are your recent calculations showing 3 / 3 calculations. All calculation are shown to the nearest degree'''

        self.text_instruction_label = Label(self.history_frame, text=history_text, width=45, justify="left", wraplength=300, padx=10, pady=10)

        self.text_instruction_label.grid(row=1)

        self.all_calc_label = Label(self.history_frame, text="calculations go here", padx=10, pady=10, bg="#ffe6cc", width=40, justify="left")

        self.all_calc_label.grid(row=2)

        save_text = '''Either choose a custom file name (and push <Export>) or simply push <Export> to save your calculations in a text file. If the filename already exists, it will be overwritten!'''

        self.save_instructions_label = Label(self.history_frame, text=save_text, wraplength=300, justify="left", width=40, padx=10, pady=10)
        
        self.save_instructions_label.grid(row=3)

        self.filename_entry = Entry(self.history_frame, font=("Arial", "14"), bg="white", width=25)

        self.filename_entry.grid(row=4)

        self.filename_error_label = Label(self.history_frame, text="Filename error goes here", fg="#9C0000", font=("Arial", "12", "bold"))

        self.filename_error_label.grid(row=5)

        self.button_frame = Frame(self.history_frame)

        self.button_frame.grid(row=6)

        self.export_button = Button(self.button_frame, font=("Arial", "12", "bold"), text="Export", bg="#004C99", fg="white", width=12)

        self.export_button.grid(row=0, column=0, padx=10, pady=10)

        self.dismiss_button = Button(self.button_frame, font=("Arial", "12", "bold"), text="Dismiss", bg="#CC6600", fg="white", width=12, command=partial(self.close_history, partner))

        self.dismiss_button.grid(row=0, column=1, padx=10, pady=10)

    # closes the history dialogue(used by the cross and the dismiss button) 
    def close_history(self, partner):
        # put help button back to normal
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()