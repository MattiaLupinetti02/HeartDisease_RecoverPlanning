max_underweight = 18.5
max_normal_weight = 25
max_obese_I = 34
max_obese_II = 40
max_overweight = 29
genHealth_domain = ['Poor', 'Fair', 'Good', 'Very Good', 'Excellent']
BMI_value_domain = list(range(0, 50, 1))
physical_health_domain = list(range(0, 31, 1))
mental_health_domain = list(range(0, 31, 1))
sleep_time_domain = list(range(1, 12, 1))
boolean_domain = [False, True]
age_category_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
ageCategory_domain = ['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80 or older']
old_age_category = ['65-69', '70-74', '75-79', '80 or older'] # according to WHO
race_domain = ['white', 'black', 'asian', 'American Indian/Alaskan Native', 'Other']
diabetic_domain = ["No", "Yes", "borderline diabetes", "Yes (during pregnancy)"]
BMI_flags = ['is_overweight', 'BMI_obese_I', 'BMI_obese_II', 'BMI_obese_III', 'bmi_gt_28']
state_flags = ['is_depressed', 'is_sickly']
bin_features = ['Smoking', 'AlcoholDrinking', 'Stroke', 'DiffWalking', 'Asthma', 'KidneyDisease', 'SkinCancer', 'PhysicalActivity']
features = [
    'BMI', 'Smoking', 'AlcoholDrinking', 'Stroke', 'PhysicalHealth', 
    'MentalHealth', 'DiffWalking', 'Sex', 'AgeCategory', 'Race', 
    'Diabetic', 'PhysicalActivity', 'GenHealth', 'SleepTime', 
    'Asthma', 'KidneyDisease', 'SkinCancer'
]

def is_old(val):
    if val > 8:
        return True
    
def is_sleepless(val):
    if val < 7:
        return True
    return False

def booleanTranslator(val):
    if val >= 1:
        return True
    else:
        return False

def is_sickly(val1, val2):
    if val1 > val2:
        return True
    else:
        return False

def is_depressed(val1, val2):
    if val1 > val2:
        return True
    else:
        return False

def is_gt_28(val):
    if val > 28:
        return True
    return False

def is_obese_rd(val):
    if val > 40:
        return True
    else:
        return False

def is_obese_nd(val):
    if val > 35 and val <= 40:
        return True
    else:
        return False

def is_obese_st(val):
    if val > 30 and val <= 35:
        return True
    else:
        return False

def is_overweight(val):
    if val > 25 and val <= 30:
        return True
    else:
        return False

def is_normal_weight(val):
    if val > 18.5 and val <= 25:
        return True
    else:
        return False

def setFlags(val, flag, val2=None):
    if is_gt_28(val) and flag == "bmi_gt_28":
        return True
    if is_overweight(val) and flag == "is_overweight":
        return True
    if is_obese_st(val) and flag == "BMI_obese_I":
        return True
    if is_obese_nd(val) and flag == "BMI_obese_II":
        return True
    if is_obese_rd(val) and flag == "BMI_obese_III":
        return True
    return False

def get_bmi(height, weight):
    return weight / (height ** 2)

def get_overweight(bmi, height):
    w_patient = bmi * (height**2)
    model_w = (height ** 2) * 25
    return w_patient - model_w
