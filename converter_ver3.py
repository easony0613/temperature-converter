'''Version1: display the GUI'''
from tkinter import *

class Converter:
    def __init__(self):

        # initialising variables(such as the feedback variables)
        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_haserror = StringVar()
        self.var_haserror.set("no")
        
         
        # Common variables
        button_font = ("Arial", "12", "bold")
        button_fg = "white"

        # set up the GUI frame
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
        self.temp_error = Label(self.temp_frame, text="", fg = "red")
        self.temp_error.grid(row=3)

        # conversion, help, history/export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        # width is the width of the button
        self.to_celsius_botton = Button(self.button_frame, text="To degree C", bg="blue", fg=button_fg, font=button_font,width=12, command=self.to_celsius)
        self.to_celsius_botton.grid(row=0, column=0, padx=5, pady=5)

        self.to_fahrenheit_button = Button(self.button_frame, text="To degree F", bg="red", fg=button_fg, font=button_font, width=12)
        self.to_fahrenheit_button.grid(row=0, column=1, padx=5, pady=5)

        self.help_button = Button(self.button_frame, text="Help/info", bg="orange", fg=button_fg, font=button_font, width=12)
        self.help_button.grid(row=1, column=0, padx=5, pady=5)

        self.history_button = Button(self.button_frame, text="History/export", bg="green", fg=button_fg, font=button_font, width=12, state=DISABLED)
        self.history_button.grid(row=1, column=1)

    def check_temp(self, min_value):

        has_error = "no"
        error = f"Please enter a number that is more than {min_value}"

        try:
            response = self.temp_entry.get()
            response = float(response)

            if response < min_value:
                has_error = "yes"
            
        except ValueError:
            has_error = "yes"
    
        if has_error == "yes":
            self.temp_error.config(text=error, fg="red")

        else: 
            self.temp_error.config(text="You are OK", fg="blue")

            self.history_button.config(state=NORMAL)


    def to_celsius(self):
        self.check_temp(-459)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()