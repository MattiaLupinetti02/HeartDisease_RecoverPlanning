import numpy as np
import matplotlib.pyplot as plt

# Dati di esempio
labels = ['RandomUnderSampler', 'RandomOverSampler', 'SMOTE', 'ADASYN', 'SMOTEENN']  # Etichette delle categorie

gradientBoostingClassifier = [0.77, 0.892, 0.776, 0.776, 0.88]  # Dati per il primo gruppo
decisionTreeClassifier = [0.66, 0.877, 0.672, 0.668, 0.859]  # Dati per il secondo gruppo
extraTreesClassifier = [0.738, 0.896, 0.735, 0.737, 0.886]  # Dati per il terzo gruppo
LGBMClassifier = [0.778, 0.899, 0.778, 0.778, 0.887]  # Dati per il quarto gruppo
randomForestClassifier = [0.754, 0.908, 0.754, 0.75, 0.892]  # Dati per il quinto gruppo
kNeighborsClassifier = [0.713, 0.899, 0.713, 0.713, 0.899]  # Dati per il sesto gruppo
logisticRegression = [0.758, 0.875, 0.758, 0.75, 0.866]  # Dati per il settimo gruppo
XGBClassifier = [0.767, 0.902, 0.767, 0.767, 0.887]  # Dati per l'ottavo gruppo

# Impostazione dei parametri delle barre
x = np.arange(len(labels))  # La posizione delle etichette sulle ascisse
width = 0.10  # Larghezza delle barre
spacing = 0.03  # Spaziatura aggiuntiva tra le barre

fig, ax = plt.subplots(figsize=(12, 8))  # Imposta la dimensione del grafico

# Creazione delle barre con offset e spaziatura
bar1 = ax.bar(x - 3*width - 3*spacing, gradientBoostingClassifier, width, label='Gradient Boosting')
bar2 = ax.bar(x - 2*width - 2*spacing, decisionTreeClassifier, width, label='Decision Tree')
bar3 = ax.bar(x - width - spacing, extraTreesClassifier, width, label='Extra Trees')
bar4 = ax.bar(x, LGBMClassifier, width, label='LGBM')
bar5 = ax.bar(x + width + spacing, randomForestClassifier, width, label='Random Forest')
bar6 = ax.bar(x + 2*width + 2*spacing, kNeighborsClassifier, width, label='K Neighbors')
bar7 = ax.bar(x + 3*width + 3*spacing, logisticRegression, width, label='Logistic Regression')
bar8 = ax.bar(x + 4*width + 4*spacing, XGBClassifier, width, label='XGBClassifier')

# Aggiunta delle etichette e del titolo
ax.set_xlabel('Algoritmi di bilanciamento')
ax.set_ylabel('Punteggi')
ax.set_title('Precision per modelli e dataset bilanciati')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc='lower right')  # Posiziona la legenda in alto a sinistra

# Aggiunta dei valori sopra le barre (opzionale)
def autolabel(bars):
    """Aggiunge i valori sopra le barre"""
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.3f}',  # Formatta con 3 cifre decimali
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 punti di offset verticale
                    textcoords="offset points",
                    ha='center', va='bottom',fontsize=7)

autolabel(bar1)
autolabel(bar2)
autolabel(bar3)
autolabel(bar4)
autolabel(bar5)
autolabel(bar6)
autolabel(bar7)
autolabel(bar8)

# Mostra il grafico
plt.show()
