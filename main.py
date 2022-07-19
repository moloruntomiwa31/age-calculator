import tkinter as tk
from tkinter import messagebox
from datetime import datetime
date = datetime.now()
CURRENT_YEAR = date.year


def calculator():
    birth_name = name_entry.get()
    birth_year = year_entry.get()
    birth_month = month_entry.get()
    birth_day = day_entry.get()
    if len(birth_name) == 0 or len(birth_year) == 0 or len(birth_month) == 0 or len(birth_day) == 0:
        messagebox.showerror("Oops", message="Please don't leave any space empty.")
        return
    if birth_year == "0" or int(birth_year) > 2022 or birth_day == "0":
        messagebox.showerror("Oops", message="Please check your inputs.")
        return
    else:
        current_age = CURRENT_YEAR - int(birth_year)
        messagebox.showinfo(title="Success!", message=f"Your age has been calculated! {name_entry.get} is {current_age} years old.")
        with open("save_file.txt", mode="a") as file:
            file.write(f"{birth_name} is {current_age} years of age.\n")
        name_entry.delete(0, "end")
        year_entry.delete(0, "end")
        month_entry.delete(0, "end")
        day_entry.delete(0, "end")
        return current_age


window = tk.Tk()
window.title("AGE CALCULATOR!")
window.minsize(300, 200)
window["bg"] = "grey"

# CANVAS
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
age_calculator = tk.PhotoImage(file="unnamed_age_calculator.png")
canvas.create_image(100, 100, image=age_calculator)
canvas.grid(column=1, row=1)

# LABELS
name = tk.Label(text="Name: ")
name.grid(column=0, row=2)
year = tk.Label(text="Year of Birth: ")
year.grid(column=0, row=3)
month = tk.Label(text="Month of Birth: ")
month.grid(column=0, row=4)
day = tk.Label(text="Day of Birth: ")
day.grid(column=0, row=5)

# ENTRY
name_entry = tk.Entry()
name_entry.focus()
name_entry.grid(column=1, row=2)
year_entry = tk.Entry()
year_entry.grid(column=1, row=3)
month_entry = tk.Entry()
month_entry.grid(column=1, row=4)
day_entry = tk.Entry()
day_entry.grid(column=1, row=5)

# BUTTON
button = tk.Button(text="Calculate Age", bg="red", command=calculator)
button.grid(column=1, row=6)
window.mainloop()
