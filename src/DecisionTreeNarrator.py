import tkinter as tk
from tkinter import ttk
import time

# Class responsible for narrating the transitions between states in a decision tree
class DecisionTreeNarrator:
    def __init__(self, states, actions):
        self.states = states
        self.actions = actions
        self.action_phrases = {
            # Dictionary mapping actions to their corresponding descriptive phrases
            "increase_hours_of_sleep": "The patient is increasing the hours of sleep, which will significantly\nreduce the risk of cardiovascular diseases.\n",
            "physical_therapy": "Improving one's health over a long period of time significantly\nreduces the likelihood of heart disease.\n",
            "rehabilitation": "The patient has started the rehabilitation program.\nBeing able to walk is the first step towards significant improvement\n",
            "pharmacological_treatment_Saxenda_liraglutide": "The patient has started pharmacological treatment with Saxenda or liraglutide.\n",
            "mental_therapy": "An improvement of the trade of the mental health would surely be a\nfactor\nfor the patient's health.\n",
            "physical_activity": "It is advisable for the patient to engage in physical activity.\nA person who practices physical activity has a\nmuch healthier and more tolerant cardiovascular\nsystem.\n",
            "stop_smoking": "It is advisable for the patient to stop smoking, as smoking is one\nof the main risk factors.\n",
            "chirurgia_bariatrica": "For a patient with Grade III Obesity, it is advisable to undergo\nbariatric surgery.\n",
            "chirurgia_bariatrica_con_comorbidita": "In the presence of comorbidities such as diabetes, we\nrecommend\nbariatric surgery even for patients with Grade\nII obesity.\n",
            "pharmacological_treatment_Saxenda_liraglutide_post_bariatric_surgery_and_hipocaloric_diet_1": "Following bariatric surgery, we administer a weight-loss\ndrug treatment like Saxenda  or liraglutide combined\nwith a hypocaloric diet.\n",
            "pharmacological_treatment_Saxenda_liraglutide_obese_II": "It is advisable to administer pharmacological obesity\ntreatment with Saxenda based on liraglutide for a patient\nwith Grade II obesity.\n",
            "stop_AlcoholDrinking": "For a high-risk patient, it is advisable to consume alcohol\nmoderately or abstain from it completely.\n",
            "pharmacological_treatment_Saxenda_liraglutide": "For a patient with Grade II obesity, it is advisable to administer\npharmacological  treatment with Saxenda or paraglutide to\nreduce weight andbringthe patient's BMI to overweight status.\n",
            "pharmacological_treatment_Saxenda_liraglutide_con_comorbidita": "Even if the patient does not have a particularly high BMI, they\nare still overweight with a BMI greater than or\nequal to 28 and comorbidities such as diabetes. It is advisable to administer pharmacological treatment, particularly Saxenda or liraglutide.\n",
            "Asthma_therapy": "Since asthma is a risk factor and the patient is at risk of\ncardiovascular diseases, it is advisable to keep this\ncondition under control with dedicated treatments.\n",
            "improve_lifestyle1": "The patient is healthy and young, so even though they have Grade\nII obesity, they can combine physical activity with\npharmacological therapies and a specific hypocaloric diet.\n",
            "improve_lifestyle2": "The patient is healthy and young, so even though they have Grade\nII obesity, they can combine physical activity with\npharmacological therapies and a specific hypocaloric diet.\n",
            "improve_lifestyle3": "The patient is healthy and young, so even though they have Grade\nII obesity, they can combine physical activity with\npharmacological therapies and a specific hypocaloric diet.\n",
            "improve_lifestyle_dieta_ipocalorica": "The patient is overweight (given the BMI), so a specific\nhypocaloric diet is advisable.\n"
        }

    # Method to describe the transition from one state to another based on an action
    def describe_transition(self, from_state, to_state, action):
        description = self.action_phrases.get(action, f"Action '{action}' not described") + " "
        changes = []

        # Check for differences between the from_state and to_state
        for key in to_state:
            if from_state.get(key) != to_state[key]:
                changes.append(f"{key} has changed from {from_state.get(key)} to {to_state[key]}")

        # Add the detected changes to the description
        if changes:
            description += "As a result, " + ", ".join(changes) + ".\n"
        else:
            description += "There were no significant changes.\n"

        return description

    # Method to describe a sequence of state transitions
    def describe_sequence(self):
        descriptions = []
        for i in range(1, len(self.states)):
            from_state = self.states[i - 1]
            to_state = self.states[i]
            action = self.actions[i - 1]
            description = self.describe_transition(from_state, to_state, action)
            descriptions.append(description)
        return descriptions

# Class responsible for visualizing the decision tree and its narration in a GUI
class DecisionTreeVisualizer:
    def __init__(self, parent, states, actions):
        self.parent = parent
        self.states = states
        self.actions = actions
        self.narrator = DecisionTreeNarrator(states, actions)
        self.setup_ui()

    # Method to setup the user interface
    def setup_ui(self):
        # Creating the main frame
        self.main_frame = ttk.Frame(self.parent, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configuring rows and columns
        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        # Creating the Text widget for narration
        self.text_widget = tk.Text(self.main_frame, wrap='word', state='disabled', bg='white', font=('Helvetica', 12))
        self.text_widget.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Adding the vertical scrollbar
        self.v_scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.text_widget.yview)
        self.v_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        # Configuring the Text widget to use the scrollbar
        self.text_widget.configure(yscrollcommand=self.v_scrollbar.set)

        # Starting the narration
        self.animate_narration()

    # Method to animate the narration by describing the sequence of state transitions
    def animate_narration(self):
        descriptions = self.narrator.describe_sequence()
        self.display_text(descriptions, 0, 0)

    # Method to display the text character by character with a delay
    def display_text(self, descriptions, desc_index, char_index):
        if desc_index < len(descriptions):
            description = descriptions[desc_index]
            if char_index < len(description):
                self.text_widget.configure(state='normal')
                self.text_widget.insert(tk.END, description[char_index])
                self.text_widget.see(tk.END)
                self.text_widget.configure(state='disabled')
                # Call the method again after 50 milliseconds to display the next character
                self.parent.after(50, self.display_text, descriptions, desc_index, char_index + 1)
            else:
                # Call the method again after 1000 milliseconds to display the next description
                self.parent.after(1000, self.display_text, descriptions, desc_index + 1, 0)
        else:
            self.text_widget.configure(state='disabled')
