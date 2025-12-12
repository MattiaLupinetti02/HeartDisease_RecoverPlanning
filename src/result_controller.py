import tkinter as tk
from tkinter import ttk
from root_controller import root
from ViewManager import getData, initializeData
from recoverCalculator import Recover_Calculator
from rehabilitationPlanner import RehabilitationPlanner
from domainManager import features
from DecisionTreeNarrator import DecisionTreeVisualizer

d = None
model = "./model_resampled/LGBMClassifier_heart_2020_cleaned_RandomOverSampler.pkl"

# Function to add a new tab to the notebook
def add_tab(notebook, actions, states):
    tab_name = f"Tab {notebook.index('end') + 1}"
    frame = ttk.Frame(notebook)
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    notebook.add(frame, text=tab_name)
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    DecisionTreeVisualizer(frame, states.copy(), actions)

def on_enter(event):
    global d
    if d is None:
        d = getData()
        print(d)
        d = initializeData(d)
        height = d.pop("Height")
        weight = d.pop("Weight")

        view_title = ttk.Label(result, text=f'Patient diagnosis: {d["Name"]} {d["Surname"]}', font=('Helvetica', 16))
        view_title.grid(row=0, column=0, padx=10, pady=10, sticky=tk.EW)
        d.pop("Name")
        d.pop("Surname")
        recover = Recover_Calculator(d, model)
        goals = recover.get_new_status()
        diagnosis_text = "Response is positive" if goals else "Negative"
        diagnosis_label = ttk.Label(result, text=diagnosis_text, font=('Helvetica', 15, 'bold'))
        diagnosis_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.EW, columnspan=2)
        if goals is not None:
            notebook = ttk.Notebook(result)
            notebook.grid(row=3, column=0, padx=20, pady=15, sticky='nsew')
            for i in goals:
                calculator = RehabilitationPlanner(d, dict(zip(features, i)), float(height), float(weight))
                sol, actions, states = calculator.get_plan()
                states = [i.assignment for i in states]
                states = [{k: v for k, v in state.items() if k in features} for state in states]
                states.reverse()
                actions = [i.name for i in actions]
                add_tab(notebook, actions, list(states))

result = ttk.Frame(root, padding="20")
result.bind("<Visibility>", on_enter)
result.rowconfigure(3, weight=1)
result.columnconfigure(0, weight=1)
