    
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score,recall_score,accuracy_score
from sklearn.metrics import f1_score
from sklearn.tree import DecisionTreeClassifier
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from modelLoader import save_model
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from domainManager import features

categorical_features=['HeartDisease']
categorical_features.append(features)
models = [
    GradientBoostingClassifier(n_estimators=100, random_state=42),
    DecisionTreeClassifier(),
    ExtraTreesClassifier(),
    LGBMClassifier(),
    RandomForestClassifier(),
    KNeighborsClassifier(), 
    LogisticRegression(max_iter=400000000), 
    XGBClassifier()
    ]
resampled_data = [
    "heart_2020_cleaned_RandomOverSampler(random_state=42, sampling_strategy='minority').csv",
    #"heart_2020_cleaned_RandomUnderSampler(random_state=42, sampling_strategy='majority').csv",
    "heart_2020_cleaned_SMOTE(random_state=42, sampling_strategy='minority').csv",
    "heart_2020_cleaned_ADASYN(random_state=42, sampling_strategy='minority').csv",
    "heart_2020_cleaned_RandomOverSampler(random_state=42, sampling_strategy='minority').csv",
    "heart_2020_cleaned_SMOTEENN(random_state=42, sampling_strategy='minority').csv"
]
def printResult(model, X_train, X_test, y_train, y_test,method,save=False):
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    print(f"viene utilizzato {method}")
    print(f"accuracy {accuracy_score(y_test,y_pred)}")
    print(f'model: {str(model)}')
    print(f'Accuracy_score: {accuracy_score(y_test,y_pred)}')
    print(f'Precission_score: {precision_score(y_test,y_pred)}')
    print(f'Recall_score: {recall_score(y_test,y_pred)}')
    print(f'F1-score: {f1_score(y_test,y_pred)}')
    print('-'*30, '\n')
    if save: 
        index_par_mod = str(model).find("(")
        index_par_method = str(method).find("(")
        end_str = "_"+str(method)[:index_par_method]+'.pkl'
        save_model("./model_resampled/"+str(model)[:index_par_mod]+end_str,model)
    
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

target = "HeartDisease"
data = pd.read_csv("./data/heart_2020_cleaned_RandomUnderSampler(random_state=42, sampling_strategy='majority').csv")
y = data[target]
data.drop(target,axis=1,inplace=True)
X_train, X_test, y_train, y_test =train_test_split(data,y,test_size=0.1,random_state=42)

for mod in models:
    printResult(mod,X_train, X_test, y_train, y_test,method="RandomUnderSampler",save=True)
X_test[target] = y_test 
df = pd.DataFrame(X_test)
df.to_csv("./data/test_set_"+"heart_2020_cleaned_RandomUnderSampler"+".csv")

# tutti i modelli addestrati con dataset bilanciati con lo stesso algoritmo vengono testati con lo stesso test set
for d in resampled_data:
    data = pd.read_csv("./data/"+d)
    y = data[target]
    data.drop(target,axis=1,inplace=True)
    X_train, X_test, y_train, y_test=train_test_split(data,y,test_size=0.1,random_state=42)
    
    index_parenthesis_resampled_data = str(d).find("(")
    X_test[target] = y_test 
    df = pd.DataFrame(X_test)
    df.to_csv("./data/test_set_"+str(d)[:index_parenthesis_resampled_data] +".csv")
    X_test.drop(target,axis=1,inplace=True)
    
    for mod in models:
        printResult(mod,X_train, X_test, y_train, y_test,method=d,save=True) 