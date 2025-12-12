import tkinter as tk
from tkinter import ttk
from domainManager import genHealth_domain
from ViewManager import initialize_label, create_checkbox, create_entry, create_combobox, nextView, preView
from root_controller import root
from patologie_paziente_controller import f3

input_names_f2_fields = ['Smoking', 'AlcoholDrinking', 'SleepTime', 'PhysicalHealth', 'MentalHealth', 'GenHealth']

input_names_f2 = [
    "Are you a smoker?", "Do you drink alcohol?", "How many hours\ndo you sleep on\naverage?",
    "How many days\nthis month did you\nhave poor\nphysical health?",
    "How many days\nthis month did you\nhave poor\nmental health?",
    "How do you currently\nrate your health?"
]

f2 = ttk.Frame(root, padding="20")
view2_title = ttk.Label(f2, text='Patient Habits', font=('Helvetica', 16))
view2_title.grid(row=0, column=1, padx=10, pady=10, sticky=tk.EW)
initialize_label(input_names_f2, f2)

checkbox_var_smoke = tk.IntVar()
create_checkbox(f2, checkbox_var_smoke, "", 1)

checkbox_var_alcohol = tk.IntVar()
create_checkbox(f2, checkbox_var_alcohol, "", 2)

sleepTime_cb = create_combobox(f2, list(range(0, 13)), 3)
phHealth_cb = create_combobox(f2, list(range(0, 31)), 4)
mtHealth_cb = create_combobox(f2, list(range(0, 31)), 5)
genHealth_cb = create_combobox(f2, genHealth_domain, 6)

nextView_button = tk.Button(f2, text="Next", command=lambda: nextView(f2, f3, input_names_f2_fields))
nextView_button.grid(row=9, column=3, padx=5, pady=5, sticky=tk.SE)
