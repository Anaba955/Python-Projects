from tkinter import *


def calculate():
    km_result.config(text=round(float(kilo_input.get())*1.60934, 1))
    print(round(int(kilo_input.get())*1.60934, 1))


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=40, pady=40)


kilo_input = Entry(width=10)
kilo_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result = Label(text="0")
km_result.grid(column=1, row=1)
km_result.config(padx=40, pady=20)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

submit_button = Button(text="Calculate", command=calculate)
submit_button.grid(column=2, row=1)


window.mainloop()
