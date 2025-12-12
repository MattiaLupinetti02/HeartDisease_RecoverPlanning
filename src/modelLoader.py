import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier


from sklearn.metrics import precision_score,recall_score
from sklearn.metrics import f1_score
import pickle

def save_model(filename,model):
    model_pkl_file = filename
    with open(model_pkl_file,'wb') as file:
        pickle.dump(model, file)
def load_model(filename):
    with open(filename, 'rb') as file:  
        model = pickle.load(file)
    return model