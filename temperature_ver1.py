from tkinter import *

class Converter:

    def __init__(self):
        # setting up the GUI frame
        self.temp_frame = Frame()
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame, text="Temperature Converter", font= ("Arial 16 bold"))
        self.temp_heading.grid(row=0)

        instruction = "Please enter a temperature below and then press one of the buttons to convert it from Centigrade to Fahrenheit "
        self.temp_instruction = Label(self.temp_frame, text=instruction, wraplength=200, width=40)
        self.temp_instruction.grid(row=1)



# Main routine
root = Tk() 
root.title("Temperature converter")
Converter()
root.mainloop()