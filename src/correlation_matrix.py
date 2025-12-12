import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

dataPath = "./data/"
target = "HeartDisease"
resampled_data = [
    "heart_2020_cleaned_RandomOverSampler(random_state=42, sampling_strategy='minority').csv",
    "heart_2020_cleaned_RandomUnderSampler(random_state=42, sampling_strategy='majority').csv",
    "heart_2020_cleaned_SMOTE(random_state=42, sampling_strategy='minority').csv",
    "heart_2020_cleaned_ADASYN(random_state=42, sampling_strategy='minority').csv",
    "heart_2020_cleaned_SMOTEENN(random_state=42, sampling_strategy='minority').csv"
]

for d in resampled_data:
    train = pd.read_csv(dataPath + d)
    correlation = train.corr()
    k = 18
    cols = correlation.nlargest(k, target)[target].index
    cm = np.corrcoef(train[cols].values.T)
    mask = np.triu(np.ones_like(cm))
    

    f, ax = plt.subplots(figsize=(20, 18))  
    
    sns.heatmap(cm, mask=mask, vmax=.8, linewidths=0.01, square=True, annot=True, cmap='viridis',
                linecolor="white", xticklabels=cols.values, annot_kws={'size':8}, yticklabels=cols.values,
                cbar_kws={'shrink': .6})  
    
    plt.show()
