import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = combo_unit.get()

        if unit == "Celsius":
            f = (temp * 9/5) + 32
            k = temp + 273.15
            result.set(f"Fahrenheit: {f:.2f} °F\nKelvin: {k:.2f} K")
        elif unit == "Fahrenheit":
            c = (temp - 32) * 5/9
            k = c + 273.15
            result.set(f"Celsius: {c:.2f} °C\nKelvin: {k:.2f} K")
        elif unit == "Kelvin":
            c = temp - 273.15
            f = (c * 9/5) + 32
            result.set(f"Celsius: {c:.2f} °C\nFahrenheit: {f:.2f} °F")
        else:
            result.set("Please select a valid unit.")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("1000x800")
root.resizable(False, False)

tk.Label(root, text="Enter Temperature:").pack(pady=15)
entry_temp = tk.Entry(root, width=40)
entry_temp.pack()

tk.Label(root, text="Select Unit:").pack(pady=15)
combo_unit = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_unit.pack()

tk.Button(root, text="Convert", command=convert_temperature).pack(pady=20)

result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 12), fg="red").pack(pady=20)

root.mainloop()
