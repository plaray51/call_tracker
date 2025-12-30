import tkinter as tk
from tkinter import ttk
import json
import os

SAVE_FILE = "call_tracker.json"
PAY_PER_CALL = 3.67
MINUTES_PER_CALL = 10

def load_data():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return {"calls": 0}

def save_data():
    with open(SAVE_FILE, "w") as f:
        json.dump({"calls": calls.get()}, f)

def format_time(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60

    if hours == 0:
        return f"{minutes} minutes"
    if hours == 1:
        return f"1 hour {minutes} minutes"
    return f"{hours} hours {minutes} minutes"

def update_display():
    value = calls.get()
    calls_entry.delete(0, tk.END)
    calls_entry.insert(0, str(value))

    money = value * PAY_PER_CALL
    total_minutes = value * MINUTES_PER_CALL

    money_label.config(text=f"Money earned: ${money:.2f}")
    time_label.config(text=f"Time worked: {format_time(total_minutes)}")

    save_data()

def increment():
    calls.set(calls.get() + 1)
    update_display()

def decrement():
    if calls.get() > 0:
        calls.set(calls.get() - 1)
        update_display()

def manual_update(event=None):
    try:
        value = int(calls_entry.get())
        if value >= 0:
            calls.set(value)
    except:
        pass
    update_display()

data = load_data()

root = tk.Tk()
root.title("Call Tracker")
root.geometry("340x280")

style = ttk.Style()
style.theme_use("clam")

calls = tk.IntVar(value=data["calls"])

main = ttk.Frame(root, padding=20)
main.pack(expand=True, fill="both")

title = ttk.Label(main, text="Call Tracker", font=("Segoe UI", 16))
title.pack(pady=10)

calls_entry = ttk.Entry(main, justify="center", font=("Segoe UI", 14))
calls_entry.pack(pady=8)
calls_entry.bind("<Return>", manual_update)

buttons = ttk.Frame(main)
buttons.pack(pady=8)

ttk.Button(buttons, text="Add Call", command=increment).pack(side="left", padx=6)
ttk.Button(buttons, text="Remove Call", command=decrement).pack(side="left", padx=6)

money_label = ttk.Label(main, font=("Segoe UI", 12))
money_label.pack(pady=6)

time_label = ttk.Label(main, font=("Segoe UI", 12))
time_label.pack(pady=6)

update_display()

root.mainloop()
