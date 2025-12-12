import tkinter as tk
from tkinter import ttk
from ViewManager import create_checkbox, create_combobox, initialize_label, nextView
from result_controller import result
from root_controller import root
from domainManager import diabetic_domain

input_names_f3 = ["Stroke", "Asthma", "DiffWalking", "KidneyDisease", "SkinCancer", "Diabetic"]

f3 = ttk.Frame(root, padding="20")

view2_title = ttk.Label(f3, text='Patient Pathologies', font=('Helvetica', 16))
view2_title.grid(row=0, column=1, padx=10, pady=10, sticky=tk.EW)

initialize_label(input_names_f3, f3)

checkbox_var_stroke = tk.IntVar()
create_checkbox(f3, checkbox_var_stroke, "", 1)

checkbox_var_asthma = tk.IntVar()
create_checkbox(f3, checkbox_var_asthma, "", 2)

checkbox_var_diffWalking = tk.IntVar()
create_checkbox(f3, checkbox_var_diffWalking, "", 3)

checkbox_var_kidneyDisease = tk.IntVar()
create_checkbox(f3, checkbox_var_kidneyDisease, "", 4)

checkbox_var_skinCancer = tk.IntVar()
create_checkbox(f3, checkbox_var_skinCancer, "", 5)

sleepTime_cb = create_combobox(f3, diabetic_domain, 6)

nextView_button = tk.Button(f3, text="Next", command=lambda: nextView(f3, result, input_names_f3))
nextView_button.grid(row=9, column=3, padx=5, pady=5, sticky=tk.SE)
