import tkinter as tk
from tkinter import ttk, Frame
from domainManager import ageCategory_domain, genHealth_domain, race_domain, get_bmi, boolean_domain, bin_features, race_domain, diabetic_domain, features

data = {} 

def preView(old, new, views):
    """ Function to switch to the previous view """
    views[new].grid_forget()
    views[old].grid(row=0, column=0, padx=1, pady=1, sticky=(tk.W, tk.E, tk.N, tk.S))

def getData():
    return data

def nextView(old_view: Frame, new_view: Frame, old_input_names: list):
    """Function to switch to the next view"""
    widgets = old_view.winfo_children()
    widgets = [widget for widget in widgets if not isinstance(widget, (ttk.Label, tk.Button))]
    data.update(dict(
                    zip(old_input_names,
                                    [
                                        widget['value'] if isinstance(widget, ttk.Radiobutton)
                                        else widget.instate(['selected']) if isinstance(widget, ttk.Checkbutton)
                                        else widget.get()
                                        for widget in widgets
                                    ])))
    old_view.grid_forget()
    new_view.grid(row=0, column=0, padx=1, pady=1, sticky='nsew')

def initialize_label(list_label, frame, r=None, c=None):
    """Function to initialize labels"""
    if r is None or c is None:
        for j, label_text in enumerate(list_label):
            label = ttk.Label(frame, text=label_text, font=('Helvetica', 10))
            label.grid(row=j + 1, column=0, padx=20, pady=15, sticky=tk.EW)
    else:
        if len(list_label) == 1:
            label = ttk.Label(frame, text=list_label[0], font=('Helvetica', 8))
            label.grid(row=r, column=c, padx=20, pady=15, sticky=tk.EW)

def isDot(c):
    c = str(c)
    return len(c) == 1 and c == '.'

dot = False

def validate_input(event):
    """Validate Entry input to allow only digits and one decimal point."""
    entry = event.widget
    current_text = str(entry.get())
    if current_text.count('.') > 1 or (not current_text[-1].isdigit() and not isDot(current_text[-1])):
        entry.delete(len(current_text) - 1, tk.END)
    return False

def create_entry(frame, name, row, check=None, char=None, digit=None):
    """Function to create text input"""
    entries = {}
    entry = ttk.Entry(frame)
    if check:
        if digit:
            entry.bind("<KeyRelease>", validate_input)
    entry.grid(row=row, column=1, padx=5, pady=5, sticky=tk.EW)
    entries[name] = entry
    return entries

def create_combobox(frame, values, row):
    """Function to create combobox"""
    cb = ttk.Combobox(frame, values=values)
    cb.set(values[0])
    cb.grid(row=row, column=1, padx=5, pady=5, sticky=tk.EW)
    return cb

def create_checkbox(frame, var, text, row):
    """Function to create checkbox"""
    ckb = ttk.Checkbutton(frame, variable=var, text=text)
    ckb.grid(row=row, column=1, padx=5, pady=5, sticky=tk.EW)
    return ckb

def initializeData(data):
    """Initialize patient data for the model"""
    model_f = ['Race', 'Diabetic', 'AgeCategory', 'GenHealth', 'Sex']  
    input_f = ['Ethnicity', 'Diabetic', 'Age', 'GenHealth', 'Gender']
    domains = [race_domain, diabetic_domain, ageCategory_domain, genHealth_domain, ["male", "female"]]
    k = 0
    for i, j in zip(model_f, input_f):
        data[i] = domains[k].index(data[j])
        if j != 'Diabetic' and j != 'GenHealth':
            data.pop(j)
        k += 1
    data["BMI"] = int(get_bmi(float(data["Height"]), float(data["Weight"])))
    data.update({i: boolean_domain.index(data[i]) for i in bin_features})
    additional_keys = [key for key in data.keys() if key not in features]
    ordered_data = {key: float(data[key]) for key in features if key in data}
    ordered_data.update({key: (data[key]) for key in additional_keys})
    data = ordered_data
    return data
