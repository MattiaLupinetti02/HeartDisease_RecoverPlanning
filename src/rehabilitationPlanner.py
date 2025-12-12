from domainManager import setFlags, get_bmi, get_overweight, is_sickly, is_old, is_depressed, is_gt_28, is_obese_st, is_obese_nd, is_obese_rd, is_overweight, is_sleepless, max_normal_weight, max_obese_I, max_overweight, genHealth_domain, boolean_domain, BMI_value_domain, physical_health_domain,  ageCategory_domain, race_domain, sleep_time_domain ,BMI_flags, bin_features,mental_health_domain
from stripsProblem import Strips, STRIPS_domain, Planning_problem
from stripsForwardPlanner import Forward_STRIPS
from searchMPP import SearcherMPP
import numpy as np

class RehabilitationPlanner(object):
    def __init__(self, patient: dict, g_patient: dict, height: float, weight: int) -> None:
        self.height = height
        self.weight = weight
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
        self.g_patient = np.array([g_patient[feature] for feature in self.feature_indices])  
        self.STRIPS_domain_feature = {'BMI_obese_I': boolean_domain, 'BMI_obese_II': boolean_domain, 'BMI_obese_III': boolean_domain,
                                      'BMI': BMI_value_domain, 'bmi_gt_28': boolean_domain, 'is_overweight': boolean_domain,
                                      'is_depressed': boolean_domain, 'is_sickly': boolean_domain, 'is_sleepless': boolean_domain,
                                      'is_old': boolean_domain, 'bariatric_surgery': boolean_domain,
                                      'Smoking': boolean_domain, 'AlcoholDrinking': boolean_domain,
                                      'Stroke': boolean_domain, 'PhysicalHealth': physical_health_domain,
                                      'MentalHealth': mental_health_domain, 'DiffWalking': boolean_domain,
                                      'Sex': boolean_domain, 'AgeCategory': ageCategory_domain, 'Race': race_domain,
                                      'Diabetic': boolean_domain, 'PhysicalActivity': boolean_domain,
                                      'SleepTime': sleep_time_domain, 'GenHealth': genHealth_domain,
                                      'Asthma': boolean_domain, 'KidneyDisease': boolean_domain,
                                      'SkinCancer': boolean_domain}
        self.bmi = get_bmi(height, weight)
        self.initial_patient = self.initialize_patient(patient, g_patient, BMI_flags, bin_features)
        self.goal_patient = self.initialize_goal_patient(g_patient, BMI_flags, bin_features)

        self.actions = [
            Strips('bariatric_surgery', {'BMI_obese_III': True, 'bariatric_surgery': False},
                   {'BMI': self.initialize_BMI_effects(self.goal_patient['BMI']),
                    'BMI_obese_III': is_obese_rd(self.bmi),
                    'BMI_obese_II': is_obese_nd(self.bmi),
                    'BMI_obese_I': is_obese_st(self.bmi),
                    'bariatric_surgery': True}),

            Strips('bariatric_surgery_with_comorbidity', {'is_overweight': False, 'BMI_obese_II': True, 'Diabetic': True, 'bariatric_surgery': False},
                   {'Diabetic': True, 'bariatric_surgery': True,
                    'BMI_obese_II': False, 'BMI_obese_I': True,
                    'BMI': self.initialize_BMI_effects(self.goal_patient['BMI'])}),

            Strips('pharmacological_treatment_Saxenda_liraglutide_post_bariatric_surgery_and_hypocaloric_diet_1', 
                   {'BMI_obese_II': True, 'bariatric_surgery': True},
                   {'BMI': self.initialize_BMI_effects(self.goal_patient['BMI']),
                    'BMI_obese_II': is_obese_nd(self.bmi),
                    'BMI_obese_I': is_obese_st(self.bmi)}),

            Strips('pharmacological_treatment_Saxenda_liraglutide_obese_II', {'BMI_obese_II': True},
                   {'BMI': self.initialize_BMI_effects(self.goal_patient['BMI']),
                    'BMI_obese_II': is_obese_nd(self.bmi),
                    'BMI_obese_I': is_obese_st(self.bmi),
                    'bmi_gt_28': is_gt_28(self.bmi),
                    'is_overweight': is_overweight(self.bmi)}),

            Strips('pharmacological_treatment_Saxenda_liraglutide_post_bariatric_surgery_and_hypocaloric_diet_2', 
                   {'BMI_obese_I': True, 'bariatric_surgery': True},
                   {'BMI': self.initialize_BMI_effects(self.goal_patient['BMI']),
                    'BMI_obese_I': is_obese_st(self.bmi),
                    'bmi_gt_28': is_gt_28(self.bmi),
                    'is_overweight': is_overweight(self.bmi)}),

            Strips('stop_AlcoholDrinking', {'AlcoholDrinking': True}, {'AlcoholDrinking': False}),

            Strips('stop_smoking', {'Smoking': True}, {'Smoking': False}),

            Strips('pharmacological_treatment_Saxenda_liraglutide', {'BMI_obese_I': True},
                   {'BMI': self.initialize_BMI_effects(self.goal_patient['BMI']),
                    'BMI_obese_I': is_obese_st(self.bmi),
                    'bmi_gt_28': is_gt_28(self.bmi),
                    'is_overweight': is_overweight(self.bmi)}),

            Strips('pharmacological_treatment_Saxenda_liraglutide_with_comorbidity', 
                   {'bmi_gt_28': True, 'Diabetic': True, 'is_overweight': True},
                   {'BMI': self.initialize_BMI_effects(self.goal_patient['BMI']),
                    'bmi_gt_28': is_gt_28(self.bmi),
                    'is_overweight': is_overweight(self.bmi)}),

            Strips('rehabilitation', {'DiffWalking': True}, {'DiffWalking': False}),

            Strips('physical_activity', {'DiffWalking': False, 'PhysicalActivity': False},
                   {'PhysicalActivity': True,
                    'BMI': self.initialize_BMI_effects(self.goal_patient['BMI']),
                    'is_overweight': is_overweight(self.bmi)}),

            Strips('mental_therapy', {'is_depressed': True, 'MentalHealth': self.initial_patient['MentalHealth']},
                   {'is_depressed': False, 'MentalHealth': self.goal_patient['MentalHealth']}),

            Strips('physical_therapy', {'is_sickly': True},
                   {'is_sickly': False, 'PhysicalHealth': self.goal_patient['PhysicalHealth']}),

            Strips('Asthma_therapy', {'Asthma': True}, {'Asthma': False}),

            Strips('increase_hours_of_sleep', {'is_sleepless': True},
                   {'is_sleepless': is_sleepless(self.goal_patient['SleepTime']), 'SleepTime': self.goal_patient['SleepTime']}),

            Strips('pharmacological_treatment_liraglutide_overweight_with_comorbidity',
                   {'is_overweight': True, 'is_old': True, 'Diabetic': True},
                   {'BMI': self.initialize_BMI_effects(self.goal_patient['BMI']), 'is_overweight': False}),

            Strips('improve_lifestyle1',
                   {'BMI_obese_II': True, 'DiffWalking': False, 'is_old': False, 'physical_activity': False, 'GenHealth': 'Good'},
                   {'BMI': self.initialize_BMI_effects(self.goal_patient['BMI']),
                    'BMI_obese_II': is_obese_nd(self.bmi),
                    'BMI_obese_I': is_obese_st(self.bmi),
                    'physical_activity': True}),  # obese II in good health

            Strips('improve_lifestyle2',
                   {'BMI_obese_II': True, 'DiffWalking': False, 'is_old': False, 'physical_activity': False, 'GenHealth': 'Very Good'},
                   {'BMI': self.initialize_BMI_effects(self.goal_patient['BMI']),
                    'BMI_obese_II': is_obese_nd(self.initialize_BMI_effects(self.bmi)),
                    'BMI_obese_I': is_obese_st(self.initialize_BMI_effects(self.bmi)),
                    'physical_activity': True}),  # obese II in very good health

            Strips('improve_lifestyle3', 
                   {'BMI_obese_II': True, 'DiffWalking': False, 'is_old': False, 'physical_activity': False, 'GenHealth': 'Excellent'},
                   {'BMI_obese_II': is_obese_nd(self.initialize_BMI_effects(self.goal_patient['BMI'])),
                    'BMI_obese_I': is_obese_st(self.bmi),
                    'physical_activity': True, 'BMI': self.bmi}),

            Strips('improve_hypocaloric_diet', {'is_overweight': True, 'Diabetic': False},
                   {'BMI': self.initialize_BMI_effects(self.goal_patient['BMI']),
                    'BMI_obese_II': is_obese_nd(self.bmi),
                    'BMI_obese_I': is_obese_st(self.bmi),
                    'physical_activity': True, 'bmi_gt_28': is_gt_28(self.bmi)})
        ]

        self.rehabilitation_planning = Planning_problem(STRIPS_domain(self.STRIPS_domain_feature, self.actions), self.initial_patient, self.goal_patient)

    def initialize_patient(self, patient: np, g_patient: np, BMI_flags: list, bin_features: list) -> dict:
        """Initialize the patient by converting features represented by 1 and 0 into boolean values and adding flags useful for planning 

        Args:
            patient (np): original patient values
            g_patient (np): Values that the patient needs to reach to avoid the risk of heart diseases
            BMI_flags (list): Flags representing the BMI levels to initialize
            bin_features (list): patient's binary features 

        Returns:
            dict: returns a dict that represents a patient in a planning problem
        """
        
        initial_patient = {}
        
        for k in patient.keys():
            if k in bin_features:
                initial_patient[k] = bool(patient[k])
            else:
                initial_patient[k] = patient[k]
        for i in range(0, len(BMI_flags)):
            initial_patient[BMI_flags[i]] = setFlags(initial_patient['BMI'], BMI_flags[i])
        
        initial_patient['is_depressed'] = is_depressed(patient['MentalHealth'], g_patient['MentalHealth'])
        initial_patient['is_sickly'] = is_sickly(patient['PhysicalHealth'], g_patient['PhysicalHealth'])
        initial_patient['is_sleepless'] = is_sleepless(patient['SleepTime'])
        initial_patient['is_old'] = is_old(initial_patient['AgeCategory'])
        initial_patient['bariatric_surgery'] = False        
        
        return initial_patient

    def initialize_goal_patient(self, g_patient: dict, BMI_flags: list, bin_features: list) -> dict:
        """Initialize the goal of patient by converting features represented by 1 and 0 into boolean values and adding flags useful for planning 

        Args:
            g_patient (np): Values that the patient needs to reach to avoid the risk of heart diseases
            BMI_flags (list): Flags representing the BMI levels to initialize
            bin_features (list): patient's binary features 

        Returns:
            dict: returns a dict that represents the goal of the patient in a planning problem
        """
        goal_patient = dict()
        for k in g_patient.keys():
            if k in bin_features:
                goal_patient[k] = bool(g_patient[k])
            else:
                goal_patient[k] = g_patient[k]
        
        for i in range(0, len(BMI_flags)):
            goal_patient[BMI_flags[i]] = setFlags(goal_patient['BMI'], BMI_flags[i])
        
        goal_patient['is_depressed'] = is_depressed(goal_patient['MentalHealth'], g_patient['MentalHealth'])
        goal_patient['is_sickly'] = is_sickly(goal_patient['PhysicalHealth'], g_patient['PhysicalHealth'])
        goal_patient['is_sleepless'] = is_sleepless(goal_patient['SleepTime'])
        goal_patient['is_old'] = is_old(goal_patient['AgeCategory'])
        
        return goal_patient
    
    
    def bmi_post_bariatric_surgery(self) -> float: 
        """Following an intervention, a patient loses between 50% and 70% of the excess weight; we return the BMI case in the worst scenario

        Returns:
            int: new BMI value
        """
        self.bmi = get_bmi(self.height, (self.weight - get_overweight(self.bmi, self.height) / 2))
        return self.bmi
    
    
    
    def initialize_BMI_effects(self, BMI_goal) -> float:
        """Initialize BMI values in the effects of each action in the STRIPS problem for a specific patient

        Args:
            BMI_goal (float): BMI value to reach

        Returns:
            float: Depending on the BMI level, an intermediate or final goal to achieve is returned
        """

        if is_obese_rd(self.bmi) and is_obese_rd(BMI_goal):
            self.bmi = BMI_goal
            return BMI_goal
        elif is_obese_rd(self.bmi):
            return self.bmi_post_bariatric_surgery()
        if is_obese_nd(self.bmi) and is_obese_nd(BMI_goal):
            self.bmi = BMI_goal
            return BMI_goal
        elif is_obese_nd(self.bmi):
            if self.initial_patient['Diabetic']:
                return self.bmi_post_bariatric_surgery()
            else:
                self.bmi = max_obese_I
            return max_obese_I
        if is_obese_st(self.bmi) and is_obese_st(BMI_goal):
                self.bmi = BMI_goal
                return BMI_goal
        elif is_obese_st(self.bmi):
            self.bmi = max_overweight
            return max_overweight
        if is_overweight(self.bmi) and is_overweight(BMI_goal):
            self.bmi = BMI_goal
            return BMI_goal
        elif is_overweight(self.bmi):
            self.bmi = max_normal_weight
            return max_normal_weight
        self.bmi = BMI_goal
        
        return BMI_goal

    
    def get_plan(self):     
        """returns the plans to reach the goals

        Returns:
            list: list of plans
        """
        searcher = SearcherMPP(Forward_STRIPS(self.rehabilitation_planning)) # A* with MPP
        searcher.search()
        return searcher.solution, searcher.actions, searcher.states
