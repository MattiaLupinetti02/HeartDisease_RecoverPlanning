from rehabilitationPlanner import RehabilitationPlanner
from recoverCalculator import Recover_Calculator
from domainManager import features
import pandas as pd
h = 1.80
def weight_calculator(bmi:list, height):
    return [b * (height * height) for b in bmi]

dataset = pd.read_csv("./data/test_set_heart_2020_cleaned_RandomOverSampler.csv",index_col=0)
dataset = dataset[(dataset["HeartDisease"]== 1.0)]
print(dataset)
bmi_list = dataset["BMI"]
#dataset.drop(["Unnamed: 0"])
#print(dataset)
pesi = weight_calculator(bmi_list,h)

"""

lista_test = [
{'BMI':32,'Smoking':1,'AlcoholDrinking':0,'Stroke':1,'PhysicalHealth':10,'MentalHealth':30,'DiffWalking':1,'Sex':1,'AgeCategory':8,'Race':0,'Diabetic':1,'PhysicalActivity':1,'GenHealth':0,'SleepTime':3.0,'Asthma':0,'KidneyDisease':0,'SkinCancer':0},


{'BMI':24,'Smoking':1,'AlcoholDrinking':0,'Stroke':0,'PhysicalHealth':30.0,'MentalHealth':30.0,'DiffWalking':1,'Sex':0,'AgeCategory':10,'Race':0,'Diabetic':0,'PhysicalActivity':1,'GenHealth':1,'SleepTime':8, 'Asthma':0,'KidneyDisease':0,'SkinCancer':1},   # pesi  69 ok

{'BMI':20,'Smoking':1,'AlcoholDrinking':0,'Stroke':0,'PhysicalHealth':3,'MentalHealth':0,'DiffWalking':0,'Sex':1,'AgeCategory':10,'Race':0,'Diabetic':0,'PhysicalActivity':0,'GenHealth':0,'SleepTime':10, 'Asthma':0,'KidneyDisease':0,'SkinCancer':0},        #       58 ok
{'BMI':35,'Smoking':1,'AlcoholDrinking':0,'Stroke':1,'PhysicalHealth':0,'MentalHealth':0,'DiffWalking':1,'Sex':1,'AgeCategory':11,'Race':0,'Diabetic':1,'PhysicalActivity':1,'GenHealth':1,'SleepTime':10, 'Asthma':0,'KidneyDisease':0,'SkinCancer':1},        #       101
{'BMI':32,'Smoking':1,'AlcoholDrinking':0,'Stroke':0,'PhysicalHealth':0,'MentalHealth':0,'DiffWalking':0,'Sex':0,'AgeCategory':11,'Race':0,'Diabetic':0,'PhysicalActivity':1,'GenHealth':2,'SleepTime':8, 'Asthma':1,'KidneyDisease':0,'SkinCancer':1},         #       92
{'BMI':32,'Smoking':1,'AlcoholDrinking':0,'Stroke':1,'PhysicalHealth':10,'MentalHealth':0,'DiffWalking':1,'Sex':0,'AgeCategory':11,'Race':0,'Diabetic':1,'PhysicalActivity':1,'GenHealth':0,'SleepTime':4, 'Asthma':0,'KidneyDisease':0,'SkinCancer':1},        #       92 
{'BMI':23,'Smoking':1,'AlcoholDrinking':1,'Stroke':0,'PhysicalHealth':0,'MentalHealth':7,'DiffWalking':1,'Sex':1,'AgeCategory':6,'Race':0,'Diabetic':0,'PhysicalActivity':1,'GenHealth':2,'SleepTime':6, 'Asthma':0,'KidneyDisease':0,'SkinCancer':0},          #       66
{'BMI':36,'Smoking':0,'AlcoholDrinking':0,'Stroke':0,'PhysicalHealth':3,'MentalHealth':0,'DiffWalking':0,'Sex':1,'AgeCategory':11,'Race':0,'Diabetic':0,'PhysicalActivity':1,'GenHealth':2,'SleepTime':10, 'Asthma':0,'KidneyDisease':0,'SkinCancer':0},        #       104
{'BMI':27,'Smoking':0,'AlcoholDrinking':0,'Stroke':0,'PhysicalHealth':30,'MentalHealth':0,'DiffWalking':0,'Sex':1,'AgeCategory':10,'Race':0,'Diabetic':1,'PhysicalActivity':0,'GenHealth':1,'SleepTime':8, 'Asthma':0,'KidneyDisease':0,'SkinCancer':0},        #       78
{'BMI':29,'Smoking':0,'AlcoholDrinking':0,'Stroke':0,'PhysicalHealth':0,'MentalHealth':0,'DiffWalking':0,'Sex':1,'AgeCategory':10,'Race':0,'Diabetic':1,'PhysicalActivity':0,'GenHealth':0,'SleepTime':7, 'Asthma':0,'KidneyDisease':0,'SkinCancer':0},         #       84
{'BMI':29,'Smoking':0,'AlcoholDrinking':0,'Stroke':1,'PhysicalHealth':20,'MentalHealth':10,'DiffWalking':0,'Sex':1,'AgeCategory':9,'Race':0,'Diabetic':1,'PhysicalActivity':1,'GenHealth':2,'SleepTime':7, 'Asthma':1,'KidneyDisease':0,'SkinCancer':0},        #       84 
]
"""


modelli = [ 
           "./model_resampled/KNeighborsClassifier_heart_2020_cleaned_RandomOverSampler.pkl",
           "./model_resampled/LGBMClassifier_heart_2020_cleaned_RandomOverSampler.pkl",
            "./model_resampled/XGBClassifier_heart_2020_cleaned_RandomOverSampler.pkl"
           ]

goal_per_modello = {"./model_resampled/KNeighborsClassifier_heart_2020_cleaned_RandomOverSampler.pkl":0,"./model_resampled/LGBMClassifier_heart_2020_cleaned_RandomOverSampler.pkl":0,"./model_resampled/XGBClassifier_heart_2020_cleaned_RandomOverSampler.pkl":0}

def print_soluzioni(lista_test, modelli, pesi, altezza ):
    for t in (lista_test):
        print("questo è il paziente")
        print(dict(zip(features,t)))
        for m in modelli:
            print(f"con il modello {m}")
            recupero = Recover_Calculator(t.copy(),m)
            goal = recupero.get_new_status()
            if  goal is not None:
                print("e' malato? "+ str(recupero.has_heartDisease(t.copy())))
                print("numero goal = " +str(len(goal)))

                if not goal:
                    print("non ha goal")    
                else:
                    for j in range(0,len(goal)):
                        calculator = RehabilitationPlanner(t.copy(),dict(zip(features, goal[j])), altezza,pesi[j])
                    
                    print("soluzione " , calculator.goal_patient,"\n")
                    
                    print("planning \n")
                    plan,actions, states = calculator.get_plan()
                    print(plan)
                    print("------------")
                    print(actions)
                    print("------------")
                    print(states)
                    
        print("___________________________________________________________________________________________________________________________")


def conta_goal(dataset,modelli):
    
    for index, row in dataset.iterrows():
        #print(t)
        #print(type(t))
        for m in modelli:
            #print(f"con il modello {m}")
            recupero = Recover_Calculator(dict(zip(features,row)),m)
            goal = recupero.get_new_status()
            if goal is not None:
                goal_per_modello[f"{m}"] = goal_per_modello[f"{m}"] + 1                             
    return goal_per_modello
print(conta_goal(dataset,modelli))
