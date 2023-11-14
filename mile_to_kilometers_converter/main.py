import tkinter as tk
from tkinter import END

window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


def miles_to_km(miles):
    return str(round(int(miles) * 1.609))


def update_km():
    kilometers_output.config(text=miles_to_km(miles_input.get()))


miles_input = tk.Entry(width=5)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)

miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

equals_label = tk.Label(text="is equal to")
equals_label.grid(column=0, row=1)

kilometers_output = tk.Label(text="0")
kilometers_output.grid(column=1, row=1)

kilometers_label = tk.Label(text="Km")
kilometers_label.grid(column=2, row=1)

calculate_button = tk.Button(text="Calculate", command=update_km)
calculate_button.grid(column=1, row=2)

window.mainloop()