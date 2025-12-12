# Heart Disease Recovery Planner

**Authors**: Francesco Buffalmano (279132), Mattia Lupinetti (278712)  
**Date**: June 2024

## Abstract

In this work, we present a Heart Disease Recovery Planner based on advanced machine learning techniques. The system is designed to assist healthcare professionals in monitoring and planning the recovery of patients suffering from cardiac diseases. The core of our software is a supervised machine learning classification model which will predict whether a patient is at risk of cardiac disease.

The Heart Disease Recovery Planner represents a tool to improve clinical outcomes and patients' quality of life.

## Introduction

Heart diseases represent one of the leading causes of mortality globally, requiring timely medical interventions and personalized recovery plans to improve patient prognosis. The complexity in managing cardiac diseases stems from the need to monitor a vast number of clinical variables and respond adequately to the specific needs of each patient.

Cardiac disease (heart disease) is a set of pathologies related to cardiovascular diseases, manifested by a disruption of normal heart function. It can be caused by damage to the epicardium, pericardium, myocardium, endocardium, heart valve apparatus, and blood vessels of the heart.

Cardiac disease can remain latent for a long time without clinical manifestation. Along with various tumors, these diseases represent today the main cause of premature death in developed countries.

The uninterrupted functioning of the circulatory system, composed of the heart as a muscular pump and a network of blood vessels, is a necessary condition for the normal functioning of the body.

According to the National Heart, Lung and Blood Institute in Framingham (USA), the most important factors in the development of cardiovascular diseases in humans are obesity, sedentary lifestyle, and smoking.

In this context, the use of machine learning technologies offers new opportunities to develop advanced tools that support healthcare professionals in recovery planning and improving clinical outcomes.

This project introduces a Heart Disease Recovery Planner based on advanced machine learning techniques, with the goal of providing accurate predictions and personalized assistance to patients. The core of the system consists of a KNeighborsClassifier model, known for its robustness and ability to handle complex datasets with numerous variables. The choice of KNeighborsClassifier is motivated by its efficiency in processing heterogeneous data and its resistance to the risk of overfitting, thus ensuring reliable predictions.

In summary, this tool not only supports healthcare professionals in planning patient recovery but also contributes to improving patients' quality of life through more effective and personalized management of their recovery path.

## Materials and Methods

### Libraries Used

The following code snippet shows the libraries used. In particular:

- **pickle** - library that allows saving and loading a pre-trained model
- **pandas, numpy** - libraries that allow data manipulation (in particular, the first allows us to create data structures like DataSet and Series, the second allows us to manipulate arrays and perform complex mathematical operations)
- **sklearn (scikit-learn)** - library that presents various machine learning models, allows selection of the best features, calculates their importance
- **Imbalanced-learn (imblearn)** - Python library designed to address the problem of classification in imbalanced datasets
- **xgboost, lightgbm** - other machine learning models
- **Tkinter** - a standard Python library used to create graphical user interfaces (GUI). It is an interface for the Tk GUI toolkit, which is widely used and well-supported.

### Dataset

For our Heart Disease Recovery Planner, we used the "Heart Disease" dataset available on Kaggle. This dataset includes a series of clinical variables relevant for the diagnosis and prognosis of cardiac diseases, such as age, gender, cholesterol levels, blood pressure, and results of various diagnostic tests. Our goal was to create a machine learning model that could accurately predict the risk of cardiac diseases and support patient recovery planning.

The dataset used is available on Kaggle at: [Kaggle Heart Disease Dataset](https://www.kaggle.com/code/georgyzubkov/heart-disease-exploratory-data-analysis)

This dataset contains detailed information about various clinical aspects of patients, including the following attributes:

- **HeartDisease** - heart disease, feature of interest
- **BMI** - a value that allows evaluating the degree of correspondence between a person's body mass and their height, and thus indirectly judging whether the mass is insufficient, normal, or excessive. Important for determining treatment indications
- **Smoking** - smoking is an important risk factor for cardiovascular diseases. When cigarette smoke is inhaled, the cardiovascular system's reaction follows immediately: within a minute, the heart rate begins to rise, increasing by 30% within ten minutes of smoking. This bad habit also increases blood pressure, fibrinogen and platelet levels, increasing the risk of blood clots
- **AlcoholDrinking** - alcohol causes not only temporary disturbances in heart function but also permanent disorders. Heart pain after alcohol consumption is not the only health problem associated with alcohol consumption
- **Stroke** - ischemic stroke occurs 4 times more often than hemorrhagic stroke. One of the main causes of this suffering is heart disease, which impairs its functioning, resulting in disruption of blood flow in the arteries and reduced blood supply to the brain. Another cause of stroke in heart diseases is thromboembolism, when clots form in the cavities of the heart (more frequently with heart failure) - blood clots
- **PhysicalHealth** - how many days in a month you experienced poor physical health
- **MentalHealth** - how many days in a month you experienced poor mental health
- **DiffWalking** - difficulty climbing stairs
- **Sex** - person's gender
- **AgeCategory** - subjects' age category
- **Diabetic** - diabetes
- **PhysicalActivity** - adults who reported engaging in physical activity or exercise during the last 30 days outside their regular work
- **GenHealth** - general well-being status
- **SleepTime** - number of hours of sleep
- **Asthma** - asthma
- **KidneyDisease** - kidney disease
- **SkinCancer** - skin cancer

The numerical variables are BMI, PhysicalHealth, MentalHealth, SleepTime. The rest are categorical.

### Imbalanced Dataset

To ensure that the machine learning model could learn effectively from all classes present in the dataset, we applied detailed preprocessing, including class balancing via the RandomOverSampler algorithm. This step was essential to address the imbalanced nature of the dataset, where some classes were significantly more represented than others.

**Figure**: We are facing an imbalanced sample, where the majority of people are healthy (approximately 90%).

**Images showing class distributions**:
- HeartDisease distribution
- Smoking distribution  
- AlcoholDrinking distribution
- DiffWalking distribution
- Sex distribution
- AgeCategory distribution
- Race distribution

### Fundamental Components

A fundamental component of our recovery plan is the calculation of a final patient state to be achieved through precise planning in which their parameters, according to the model, make the patient out of danger.

To obtain this state, we modify the features that the correlation matrix of our dataset considers most impactful for the value of our goal: HeartDisease.

**Figure**: Correlation matrix of the original dataset

To calculate one or more goals, we created the recoverCalculator class:

**RecoverCalculator class code screenshots**:

In the calculate_goals() method, we modify patient parameters related to lifestyle or diseases from which the patient can recover (we therefore refrained from modifying features like "SkinCancer", "KidneyDisease", or "Diabetic").

Following the calculation of goals, there is a need to create a planning problem whose solution will be found by a search algorithm, in our case an MPP (Maximal Pattern Search) algorithm:

**Planning algorithm code screenshots**:

The patient's BMI is classified, and the current BMI level leads to specific treatment. Based on BMI, it can be distinguished into:
- Grade I obesity (BMI 30-35)
- Grade II obesity (BMI 35-40)  
- Grade III obesity (severe) (BMI>40)

Extreme BMI levels are treated with medications.

**OBESITY MEDICATIONS**:
- **Orlistat**: 
  - Obese patients with BMI over 30 kg/m²
  - Patients with BMI over 28 kg/m² but with concomitant risk factors, in association with a moderately hypocaloric diet
- **Liraglutide**:
  - Also authorized for obesity treatment, but at a dose of 3 mg/day in adult patients with BMI≥30 kg/m² or between 27 and 30 kg/m² with weight-related comorbidities (hyperglycemia or type 2 diabetes, arterial hypertension, dyslipidemia, sleep apnea)

**Source**: Dr. Massimiliano Andrioli

## Experiments and Results

### Model Evaluation

The model was evaluated using a series of key metrics:

- **Accuracy**: The proportion of correct predictions out of all predictions made, is an overall measure of model correctness, but may not be adequate in the presence of imbalanced classes
- **Precision**: The proportion of true positives out of all positive predictions, is useful when it's important to minimize false positives, for example in problems where positive errors have high costs
- **Recall**: The proportion of true positives out of all actual positives, is useful when it's important to minimize false negatives, for example in problems where missing a positive case can have serious consequences
- **F1-score**: The harmonic mean of precision and recall

The following are the percentages of accuracy, precision, recall and F1 for the following models:

#### KNeighborsClassifier
- Model: KNeighborsClassifier()
- Accuracy score: 0.9025328330206379
- Precision score: 0.3203463203463203  
- Recall score: 0.07740585774058577
- F1-score: 0.12468407750631845

#### LogisticRegression
- Model: LogisticRegression()
- Accuracy score: 0.9115697310819262
- Precision score: 0.5423728813559322
- Recall score: 0.08926080892608089
- F1-score: 0.1532934131736527

#### XGBClassifier
- Model: XGBClassifier
- Accuracy score: 0.9121013133208256
- Precision score: 0.5580448065173116
- Recall score: 0.09553695955369595
- F1-score: 0.16314379279547486

#### ExtraTreesClassifier
- Model: ExtraTreesClassifier()
- Accuracy score: 0.8931519699812382
- Precision score: 0.30462633451957294
- Recall score: 0.1492329149232915
- F1-score: 0.20032763866136205

### Model Evaluation Conclusions

We can easily notice that the Accuracy score is very high for all models but since this is a medical application, we focus on the metrics concerning positive predictions: in the models' performance on the original dataset, precision and recall never exceed 56% and 16%, so in the best case we have a precision slightly above 50% but with a very high rate of false negatives, which is exactly the case we would most want to avoid in a medical application.

Having noted this, we decided to apply the following classes from the `imblearn` library to the dataset:

#### RandomUnderSampler
**Description**:  
RandomUnderSampler is a data balancing technique that works by randomly reducing the number of samples from the majority class in the dataset. This approach is useful when you want to reduce the excess of samples from the dominant class to balance the dataset.

**Functioning**:
1. Randomly selects a subset of samples from the majority class
2. Maintains only the selected samples in the new version of the dataset
3. Simple to implement but could lead to loss of information if important samples are eliminated

#### RandomOverSampler
**Description**:  
RandomOverSampler is another balancing technique that operates by randomly increasing the number of samples from the minority class in the dataset. This method is effective for improving the representation of less frequent classes.

**Functioning**:
1. Randomly selects samples from the minority class
2. Replicates these samples to increase the number of instances of the minority class
3. Can lead to an increased risk of overfitting if not adequately controlled

#### SMOTE (Synthetic Minority Over-sampling Technique)
**Description**:  
SMOTE is an oversampling technique designed to address the problem of the minority class by creating new synthetic samples rather than replicating existing ones. It uses interpolation between minority class samples to generate new examples.

**Functioning**:
1. Identifies minority class samples that are close in the feature space
2. Creates new synthetic samples between existing minority class samples
3. Improves the representation of the minority class without duplicating existing samples, reducing the risk of overfitting

#### SMOTE-ENN (SMOTE + Edited Nearest Neighbors)
**Description**:  
SMOTE-ENN is a combination of SMOTE and an editing operation of majority class samples. This method not only oversamples the minority class but also eliminates majority class samples that are close to minority class samples.

**Functioning**:
1. Uses SMOTE to generate synthetic samples of the minority class
2. Applies Edited Nearest Neighbors (ENN) to eliminate majority class samples that are incorrectly classified near minority class samples
3. Helps reduce noise introduced by non-representative synthetic samples

#### ADASYN (Adaptive Synthetic Sampling)
**Description**:  
ADASYN is an oversampling technique that generates synthetic samples for the minority class with a distribution proportional to the local density of neighboring samples.

**Functioning**:
1. Calculates the local density of minority samples
2. Generates synthetic samples for the minority class with a density proportional to the local density
3. Creates a finer balance compared to SMOTE in areas of the feature space where sample density is variable

The Python script used to balance the datasets is `data_resampler.py` and saves the new datasets in `./data/`

**Data resampler code screenshots**:

### Tests Following Balancing

Finally, we compared the performance of our model with tests on the models present in the notebook from which we took the dataset: following data balancing, as reported in the file `prestazione_modelli.txt`, we obtained a significant improvement in performance.

We focus on metrics such as Recall and Precision as main metrics to evaluate model performance. This is because, in the context of heart disease, it is essential to pay maximum attention to identifying the greatest number of positive cases.

**Model testing code screenshots**:

The results of Precision, Recall and F1 are shown below:

**Figure**: Precision histogram

**Figure**: F1 histogram

The best scores were achieved by models that performed the training phase on datasets balanced with SMOTEEN and RandomOverSampler classes, especially models trained with the latter achieve very similar percentages of both precision-score and recall-score, resulting in very similar F1-score values.

The model we finally chose is KNeighborsClassifier trained on the dataset balanced through the RandomOverSampler class, which has an excellent precision-score (90%) and an equally excellent recall-score (89%). These scores allow an F1-score that stands at 90%.

## Conclusion

To start the program, run the `main.py` script.

### Interface

To interface with the planning program, we created a simple graphical interface that allows creating the patient profile and getting a textual response in a few simple steps:

**Patient profile creation screenshot**:

**Patient habits screenshot**:

**Patient pathologies screenshot**:

**Response screenshot**:

---

**Note**: This document is a Markdown conversion of the original LaTeX paper. For the complete document with all figures and formatting, please refer to the PDF version in the repository.
