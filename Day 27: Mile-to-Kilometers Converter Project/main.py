from tkinter import *


def calculate_kilometers():
    distance_in_miles = float(miles_input.get())
    distance_in_km = round(distance_in_miles * 1.60934, 2)
    km_output.config(text=f"{distance_in_km}")


window = Tk()
window.title("Mile to km converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)

miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

km_output = Label(text="0")
km_output.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

calculate_button = Button(text="Calculate", command=calculate_kilometers)
calculate_button.grid(column=1, row=2)

window.mainloop()