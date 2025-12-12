import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Heart Disease Rehab Planner")
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
rel_height, rel_width = int(height * 0.75), int(width * 0.4)
position_right, position_down = (width - rel_width) // 2, (height - rel_height) // 2
root.geometry(f"{rel_width}x{rel_height}+{position_right}+{position_down}")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.resizable(False, False)