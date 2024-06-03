'''Version1: display the GUI'''
from tkinter import *

class Converter:
    def __init__(self):
        # set up the GUI frame
        button_font = ("Arial", "12", "bold")
        button_fg = "white"
        self.temp_frame = Frame()
        self.temp_frame.grid()
        self.temp_heading = Label(self.temp_frame, text="Temperature Converter", font=("Arial", "16", "bold"))
        self.temp_heading.grid(row=0)

        # setting up the instruction
        instructions = "Please enter a temperature below and then press one of the buttons to convert it from centigrade to fahrenheit"
        self.temp_instruction = Label(self.temp_frame, text=instructions, wraplength=150, width=40)
        self.temp_instruction.grid(row=1)

        # entry box
        self.temp_entry = Entry(self.temp_frame, font=("Arial", "14"))
        self.temp_entry.grid(row=2, padx=10, pady=10)

        # error message
        error = "Please enter a number"
        self.temp_error = Label(self.temp_frame, text=error, fg = "red")
        self.temp_error.grid(row=3)

        # conversion, help, history/export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

            # width is the width of the button
        self.to_celsius_botton = Button(self.button_frame, text="To degree C", bg="blue", fg=button_fg, font=button_font,width=12)
        self.to_celsius_botton.grid(row=0, column=0, padx=5, pady=5)

        self.to_fahrenheit_button = Button(self.button_frame, text="To degree F", bg="red", fg=button_fg, font=button_font, width=12)
        self.to_fahrenheit_button.grid(row=0, column=1, padx=5, pady=5)

        self.help_button = Button(self.button_frame, text="Help/info", bg="orange", fg=button_fg, font=button_font, width=12)
        self.help_button.grid(row=1, column=0, padx=5, pady=5)

        self.history_button = Button(self.button_frame, text="History/export", bg="green", fg=button_fg, font=button_font, width=12, state=DISABLED)
        self.history_button.grid(row=1, column=1)



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()