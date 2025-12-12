import tkinter as tk
from tkinter import ttk
from domainManager import race_domain, ageCategory_domain
from ViewManager import initialize_label, create_checkbox, create_entry, create_combobox, nextView
from root_controller import root
from abitudini_paziente_controller import f2

input_names_f1 = ["Name", "Surname", "Height", "Weight", "Ethnicity", "Age", "Gender", "PhysicalActivity"]
f1 = ttk.Frame(root, padding="20")

# Grid configuration
num_rows, num_cols = 9, 4
for i in range(num_rows):
    f1.rowconfigure(i, weight=1)
for j in range(num_cols):
    f1.columnconfigure(j, weight=1)

view1_title = ttk.Label(f1, text='Patient Personal Data', font=('Helvetica', 16))
view1_title.grid(row=0, column=1, padx=10, pady=10, sticky=tk.EW)
initialize_label(input_names_f1, f1)
initialize_label(["*Enter height in meters"], f1, 10, 0)

entries = {}
for j in range(4):
    if input_names_f1[j] == "Height" or input_names_f1[j] == "Weight":
        create_entry(f1, input_names_f1[j], j + 1, check=True, digit=True)
    else:
        create_entry(f1, input_names_f1[j], j + 1)

ethnicity_cb = create_combobox(f1, race_domain, 5)
age_cb = create_combobox(f1, ageCategory_domain, 6)
sex_cb = create_combobox(f1, ["male", "female"], 7)
checkbox_var = tk.IntVar()
create_checkbox(f1, checkbox_var, "Physical Activity", 8)

nextView_button = tk.Button(f1, text="Next", command=lambda: (nextView(f1, f2, input_names_f1)))
nextView_button.grid(row=9, column=4, sticky=tk.SE)

f1.grid(row=0, column=0, padx=20, pady=20)