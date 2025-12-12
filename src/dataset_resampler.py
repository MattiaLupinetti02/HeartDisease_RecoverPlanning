    
import numpy as np
from sklearn.model_selection import train_test_split
import numpy as np
from imblearn.over_sampling import RandomOverSampler,SMOTE, ADASYN
from imblearn.under_sampling import RandomUnderSampler
from imblearn.combine import SMOTEENN
import pandas as pd
import pickle
from sklearn.preprocessing import OrdinalEncoder
from domainManager import features

categorical_features=['HeartDisease']
categorical_features.append(features)
resampling_methods = [
    RandomUnderSampler(sampling_strategy='majority', random_state=42),
    SMOTE(sampling_strategy='minority', random_state=42),
    ADASYN(sampling_strategy='minority', random_state=42),
    SMOTEENN(sampling_strategy='minority', random_state=42),
    RandomOverSampler(sampling_strategy='minority', random_state=42)
]

def convert_data(data,categorical_f,target,split=False):
    enc = OrdinalEncoder()
    enc.fit(data[categorical_f])
    data[categorical_f] = enc.transform(data[categorical_f])
    if split: 
        y = data[target]
        data.drop(target,axis=1,inplace=True)
        X_train, X_test, y_train, y_test=train_test_split(data,y,test_size=0.1,random_state=42)    
        return X_train, X_test, y_train, y_test
    return data

def dataResampler(X,y, methods,target):
    i = 0
    data = dict()  
    for m in methods:
            X,y = m.fit_resample(X, y)
            X[target] = y
            data.update({i:X})
            df = pd.DataFrame(X)
            df.to_csv('./data/heart_2020_cleaned_' + str(m)+'.csv')
            i = i + 1
    return data
      
target = "HeartDisease"

data = pd.read_csv("./data/heart_2020_cleaned.csv")

data = convert_data(data,categorical_features,target, split=False)
y = data[target]
data.drop(target,axis=1,inplace=True)
data = dataResampler(data,y,resampling_methods,target)