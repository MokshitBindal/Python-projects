from tkinter import *

FONT = ("Arial", 24, "bold")

def calculate():
    mile = float(input_box.get())
    km = round(mile * 1.609, 2)
    answer_label.config(text=f"{km}")
    

window = Tk()
window.title("Mile to Km Converter")
window.minsize(300,100)
window.config(padx=50,pady=50)

answer_label = Label(text="0")
answer_label.grid(row=2, column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=2,column=1)

km_label = Label(text="KM")
km_label.grid(row=2,column=3)

miles_label = Label(text="Miles")
miles_label.grid(row=1,column=3)

input_box = Entry(width=10)
input_box.grid(row=1, column=2)

button = Button(text="Calculate", command=calculate)
button.grid(row=3,column=2)


window.mainloop()