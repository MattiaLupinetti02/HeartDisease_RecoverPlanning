import pandas as pd
import numpy as np
from modelLoader import load_model
from domainManager import is_normal_weight

class Recover_Calculator(object):
    
    def __init__(self, patient: dict, modelFileName: str):
        self.feature_indices = {
            "BMI": 0,
            "Smoking": 1,
            "AlcoholDrinking": 2,
            'Stroke': 3,
            "PhysicalHealth": 4,
            "MentalHealth": 5,
            "DiffWalking": 6,
            'Sex': 7,
            'AgeCategory': 8,
            'Race': 9,
            'Diabetic': 10,
            "PhysicalActivity": 11,
            'GenHealth': 12,
            "SleepTime": 13,
            "Asthma": 14,
            'KidneyDisease': 15,
            'SkinCancer': 16    
        }
        self.patient = np.array([patient[feature] for feature in self.feature_indices])
        self.model = load_model(modelFileName)            
        if self.has_heartDisease(self.patient):
            self.new_status, self.new_values = self.calculate_goals(self.patient)
        else:
            self.new_status = None
             
    def make_patient_test(self, patient_array):
        return pd.DataFrame([patient_array], columns=[feature for feature in self.feature_indices])

    def has_heartDisease(self, patient: np):
        return bool(self.model.predict(self.make_patient_test(patient)))
    
    def calculate_goals(self, patient):
        """
        The method modifies the boolean features and the numerical features
        in non-increasing order of their correlation with the target,
        and checks if the change in lifestyle or disease 
        state removes the patient from danger. 
        If so, adds the patient's data to the list of solutions. 
        
        Args:
            patient (ndarray): initial patient status

        Returns:
            list : patient version 
        """
        healthy_patients = []
        new_vals = {}
        health_trends = {"PhysicalHealth", "MentalHealth"}
        range_bin = {"DiffWalking", "Smoking", "PhysicalActivity", "Asthma"}
        test = patient.copy()

        for feature in range_bin:
            index = self.feature_indices[feature]
            if feature == "PhysicalActivity": 
                if test[index] == 0:
                    test[index] = 1
            else:
                test[index] = 0
            if self.has_heartDisease(test):
                new_vals[feature] = test[index]
            elif test not in healthy_patients:
                healthy_patients.append(test)
        
        for feature in health_trends:
            index = self.feature_indices[feature]
            while test[index] > 0 and self.has_heartDisease(test):
                    test[index] -= 1
            if self.has_heartDisease(test):
                new_vals[feature] = test[index]
            elif test not in healthy_patients:
                healthy_patients.append(test)
        
        index = self.feature_indices["SleepTime"]
        while test[index] <= 7 and self.has_heartDisease(test):
            test[index] += 1
        if self.has_heartDisease(test):
            new_vals[feature] = test[index]
        elif test not in healthy_patients:
                healthy_patients.append(test)
                
        index = self.feature_indices["BMI"]
        while not is_normal_weight(test[index]) and self.has_heartDisease(test):
                    test[index] -= 1
        if self.has_heartDisease(test):
            new_vals[feature] = test[index]
        elif test not in healthy_patients:
                healthy_patients.append(test)    
        
        return healthy_patients, new_vals

    def get_new_status(self):
        return self.new_status
