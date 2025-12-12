\documentclass{article}
\usepackage{graphicx} % Required for inserting images
\usepackage{hyperref}
\usepackage{float}


\title{Hearth Disease recover planner }
\author{Francesco Buffalmano 279132, Mattia Lupinetti 278712}
\date{June 2024}

\begin{document}

\maketitle

\section{ Abstract}
In questo lavoro, presentiamo un Pianificatore di Recupero dalle Malattie Cardiache basato su tecniche avanzate di machine learning. Il sistema è progettato per assistere i professionisti della salute nel monitoraggio e nella pianificazione del recupero dei pazienti affetti da malattie cardiache. Il nucleo del nostro software è un modello di machine learning supervisionato di classificazione il quale predirrà se un paziente è a rischio di malattie cardiache.
Il Pianificatore di Recupero dalle Malattie Cardiache rappresenta  uno strumento  per migliorare i risultati clinici e la qualità della vita dei pazienti.



\section{Introduction}

Le malattie cardiache rappresentano una delle principali cause di mortalità a livello globale, richiedendo interventi medici tempestivi e piani di recupero personalizzati per migliorare la prognosi dei pazienti. La complessità nella gestione delle malattie cardiache deriva dalla necessità di monitorare un vasto numero di variabili cliniche e di rispondere in modo adeguato alle specifiche esigenze di ciascun paziente.

La malattia cardiaca (malattia del cuore) è un insieme di patologie legate alle malattie cardiovascolari, manifestate da una violazione del normale funzionamento del cuore. Può essere causata da danni all'epicardio, pericardio, miocardio, endocardio, apparato valvolare del cuore e ai vasi sanguigni del cuore.
La malattia cardiaca può durare a lungo in forma latente, senza manifestarsi clinicamente. Insieme a vari tumori, queste malattie rappresentano oggi la principale causa di morte prematura nei paesi sviluppati.
Il funzionamento ininterrotto del sistema circolatorio, composto dal cuore come pompa muscolare e da una rete di vasi sanguigni è una condizione necessaria per il normale funzionamento del corpo.
Secondo il National Heart, Lung and Blood Institute di Framingham (USA), i fattori più importanti nello sviluppo delle malattie cardiovascolari negli esseri umani sono l'obesità, lo stile di vita sedentario e il fumo.
In questo contesto, l'uso delle tecnologie di machine learning offre nuove opportunità per sviluppare strumenti avanzati che supportano i professionisti della salute nella pianificazione del recupero e nel miglioramento dei risultati clinici.
Questo progetto introduce un Pianificatore di Recupero dalle Malattie Cardiache basato su tecniche avanzate di machine learning, con l'obiettivo di fornire previsioni accurate e assistenza personalizzata ai pazienti. Il nucleo del sistema è costituito da un modello di KNeighborsClassifier, noto per la sua robustezza e la capacità di gestire dataset complessi con numerose variabili. La scelta di KNeighborsClassifier è motivata dalla sua efficienza nell'elaborare dati eterogenei e dalla sua resistenza al rischio di overfitting, garantendo così previsioni affidabili.
In sintesi, questo strumento non solo supporta i professionisti della salute nella pianificazione del recupero dei pazienti, ma contribuisce anche a migliorare la qualità della vita dei pazienti attraverso una gestione più efficace e personalizzata del loro percorso di recupero.


\section{Materials and Methods}
\subsection{Librerie}
Nel seguente frammento di codice vengono mostrate le librerie utilizzate. In particolare:
\begin{itemize}
     
\item pickle - libreria che consente di salvare e caricare un modello preaddestrato
\item pandas, numpy - librerie che consentono di manipolare i dati (in particolare la prima ci consente di creare strutture dati come DataSet e Series, la seconda ci permette di manipolare array ed effettuare operazioni matematico complesse.
\item sklearn (scikit-learn) - libreria che presenta vari modelli di machine learning, permette la scelta delle features migliori, ne calcola l’importanza.
\item Imbalanced-learn (imblearn) - libreria Python progettata per affrontare il problema della classificazione in dataset con classi sbilanciate
\item  xgboost, lightgbm - altri modelli di machine learning.
\item Tkinter - una libreria standard di Python utilizzata per creare interfacce grafiche utente (GUI). È un'interfaccia per il toolkit GUI Tk, che è ampiamente utilizzato e ben supportato.
\end{itemize}

\subsection{Dataset}
Per il nostro Pianificatore di Recupero dalle Malattie Cardiache, abbiamo utilizzato il dataset "Heart Disease" disponibile su Kaggle. Questo dataset comprende una serie di variabili cliniche rilevanti per la diagnosi e la prognosi delle malattie cardiache, come età, sesso, livelli di colesterolo, pressione sanguigna e risultati di vari test diagnostici. Il nostro obiettivo era creare un modello di machine learning che potesse prevedere con precisione il rischio di malattie cardiache e supportare la pianificazione del recupero dei pazienti.
Il dataset utilizzato è disponibile su Kaggle all'indirizzo: \href{https://www.kaggle.com/code/georgyzubkov/heart-disease-exploratory-data-analysis}{Kaggle}.
Questo dataset contiene informazioni dettagliate su vari aspetti clinici dei pazienti, inclusi i seguenti attributi:

\begin{itemize}
 \item HeartDisease - malattia cardiaca, tratto di interesse.
  \item BMI - un valore che consente di valutare il grado di corrispondenza tra la massa corporea di una persona e la sua altezza, e quindi giudicare indirettamente se la massa è insufficiente, normale o eccessiva. È importante per determinare le indicazioni per il trattamento.
 \item Smoking - il fumo è un fattore di rischio importante per le malattie cardiovascolari. Quando si inhala il fumo di una sigaretta, la reazione del sistema cardiovascolare segue immediatamente: entro un minuto, la frequenza cardiaca inizia a salire, aumentando del 30\% entro dieci minuti dal fumo. Questa cattiva abitudine aumenta anche la pressione sanguigna, i livelli di fibrinogeno e piastrine, aumentando il rischio di coaguli sanguigni.
 \item AlcoholDrinking - l'alcol causa non solo disturbi temporanei nel funzionamento del cuore, ma anche disturbi permanenti. Il dolore al cuore dopo l'assunzione di alcol non è l'unico problema di salute associato al consumo di alcol.
 \item Stroke - l'ictus ischemico si verifica 4 volte più spesso dell'emorragico. Una delle principali cause di questa sofferenza è la malattia cardiaca, che compromette il suo funzionamento, con conseguente disturbo del flusso sanguigno nelle arterie e riduzione dell'apporto di sangue al cervello. Un'altra causa di ictus nelle malattie cardiache è il tromboembolismo, quando si formano coaguli nelle cavità del cuore (più frequentemente con l'insufficienza cardiaca) - coaguli di sangue.
 \item PhysicalHealth - quanti giorni al mese hai avvertito cattiva salute fisica.
 \item MentalHealth - quanti giorni al mese hai avvertito cattiva salute mentale.
 \item DiffWalking - difficoltà a salire le scale.
 \item Sex - genere di una persona.
 \item AgeCategory - categoria di età dei soggetti.
 \item Diabetic - diabete.
 \item PhysicalActivity - adulti che hanno dichiarato di aver praticato attività fisica o esercizio fisico durante gli ultimi 30 giorni al di fuori del loro lavoro regolare.
 \item GenHealth - stato di benessere generale.
 \item SleepTime - numero di ore di sonno.
 \item Asthma - asma.
\item KidneyDisease - malattia renale.
\item Skin Cancer - cancro della pelle. 
\end{itemize}
Le variabili numeriche sono BMI, PhysicalHealth, MentalHealth, SleepTime. Il resto è categorico.

\subsection{Dataset sbilanciato}
Per garantire che il modello di machine learning potesse apprendere in modo efficace da tutte le classi presenti nel dataset, abbiamo applicato un preprocessamento dettagliato, incluso il bilanciamento delle classi tramite l'algoritmo di RandomOverSampler. Questo passaggio è stato essenziale per affrontare la natura sbilanciata del dataset, dove alcune classi erano significativamente più rappresentate rispetto ad altre.
\begin{figure}[H]
        \centering
        \includegraphics[width=1.2\linewidth]{__results___17_1.png}
        \caption{Siamo di fronte ad un campione sbilanciato, dove la maggioranza delle persone sono sane (circa il 90\%).}
        \label{Siamo di fronte ad un campione sbilanciato, dove la maggioranza delle persone sono sane.}
    \end{figure}


\begin{figure}[H]
    \centering
    \includegraphics[width=1.2\linewidth]{__results___28_0.png}
    \caption{HeartDisease}
    \label{fig:enter-label}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=1.2\linewidth]{__results___28_1.png}
    \caption{Smoking}
    \label{fig:enter-label}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=1.2\linewidth]{__results___28_2.png}
    \caption{AlcholDrinking}
    \label{fig:enter-label}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=1.2\linewidth]{__results___28_3.png}
    \caption{DiffWalking}
    \label{fig:enter-label}
\end{figure}


\begin{figure}[H]
    \centering
    \includegraphics[width=1.2\linewidth]{__results___28_5.png}
    \caption{Sex}
    \label{fig:enter-label}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=1.2\linewidth]{__results___28_6.png}
    \caption{AgeCategory}
    \label{fig:enter-label}
\end{figure}


\begin{figure}[H]
    \centering
    \includegraphics[width=1.2\linewidth]{__results___28_7.png}
    \caption{Race}
    \label{fig:enter-label}
\end{figure}


    

\subsection{Componenti fondamentali}
Un componente fondamentale del nostro piano di recupero è il calcolo di uno stato finale del paziente da raggiungere attraverso un preciso planning in cui i suoi parametri, secondo il modello, lo rendono il paziente fuori pericolo.
Per ottenere tale stato modifichiamo le feutures che la matrice di correlazione del nostro dataset ritiene più impattanti per il valore del nostro goal: HearthDisease.
\begin{figure}[H]
    \centering
    \includegraphics[width=1.0\linewidth]{__results___45_2.png}
    \caption{Matrce di correlazione del dataset originale}
    \label{fig:enter-label}
\end{figure}
 Per calcolare uno o più goal abbiamo creato la classe recoverCalculator:

\begin{figure}[H]
    \centering
    \includegraphics[width=1.5\linewidth]{recoverCalculator1.png}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=1.5\linewidth]{recoverCalculator2.png}
\end{figure}
\begin{figure}[H]
    \centering
    \includegraphics[width=1.5\linewidth]{recoverCalculator3.png}
\end{figure}
\begin{figure}[H]
    \centering
    \includegraphics[width=1.35\linewidth]{recoverCalculator4.png}
\end{figure}
Nel metodo calculate\_goals() modifichiamo i parametri del paziente legati allo stile di vita o a malattie da cui il paziente può guarire (ci siamo quindi astenuti dal modoficare features come "SkinCancer", "KidneyDisease" o "Diabetic").

In seguito al calcolo dei goal c'è bisogno di creare un planning problem la cui soluzione sarà trovata da un algoritmo di ricerca, nel nostro caso un algoritmo di ricerca MPP (Maximal Pattern Search):

\begin{figure}[H]
    \centering
    \includegraphics[width=1.35\linewidth]{rehub1.png}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=1.35\linewidth]{rehub2.png}
\end{figure}
\begin{figure}[H]
    \centering
    \includegraphics[width=1.35\linewidth]{rehub3.png}
\end{figure}
\begin{figure}[H]
    \centering
    \includegraphics[width=1.35\linewidth]{rehub5.png}
\end{figure}
\begin{figure}[H]
    \centering
    \includegraphics[width=1.35\linewidth]{rehub6.png}
\end{figure}
\begin{figure}[H]
    \centering
    \includegraphics[width=1.35\linewidth]{rehub7.png}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=1.35\linewidth]{rehub8.png}
\end{figure}
\begin{figure}[H]
    \centering
    \includegraphics[width=1.35\linewidth]{rehub9.png}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=1.35\linewidth]{rehub10.png}
\end{figure}
\begin{figure}[H]
    \centering
    \includegraphics[width=1.35\linewidth]{rerhub11.png}
\end{figure}

Il BMI dei paziente viene classificato, il livello del BMI momentaneo induce a uno specifico trattamento.
In base al BMI può essere distinta in:
-obesità di I grado (BMI 30-35) 
-obesità di II grado (BMI 35-40)
-obesità di III grado (severa) (BMI>40)
I livelli estremi di BMI sono trattati da farmaci.
FARMACI OBESITÀ:
\begin{itemize}

 \item Orlistat:
    – pazienti obesi con un BMI superiore a 30 kg/m2
    – pazienti con BMI superiore a 28 kg/m2 ma con concomitanti fattori di rischio, in associazione ad una dieta moderatamente ipocalorica.
\item Liraglutide;
    - è stata autorizzata anche nel trattamento dell’obesità, ma alla dose di 3 mg/die in pazienti adulti con un BMI≥30 kg/m2 o tra 27 e 30 kg/m2 con comorbidità   correlate al peso (iperglicemia o diabete tipo 2, ipertensione arteriosa, dislipidemia, apnee notturne).
\end{itemize}
.

FONTE:
Dott. Massimiliano Andrioli

\section{Experiments and Results}
\subsection{Valutazione del Modello}
Il modello è stato valutato utilizzando una serie di metriche chiave:
\begin{itemize}
\item Accuratezza: La proporzione di previsioni corrette su tutte le previsioni effettuate, è una misura complessiva della correttezza del modello, ma può non essere adeguata in presenza di classi sbilanciate
\item Precisione: La proporzione di vere positività su tutte le previsioni positive,  è utile quando è importante ridurre al minimo i falsi positivi, ad esempio in problemi dove gli errori positivi hanno costi elevati.
\item Richiamo (Recall): La proporzione di vere positività su tutte le effettive positività, è utile quando è importante ridurre al minimo i falsi negativi, ad esempio in problemi dove perdere un caso positivo può avere conseguenze gravi.
\item F1-score: La media armonica della precisione e del richiamo.
\end{itemize}
Quelli che seguono sono le percentuali di accuratezza, precisione, recall e F1 su i seguenti modelli: 

\subsubsection{KNeighborsClassifier}
\begin{itemize}
\item   model: KNeighborsClassifier()
\item Accuracy score: 0.9025328330206379
\item Precission score: 0.3203463203463203
\item Recall score: 0.07740585774058577
\item F1-score: 0.12468407750631845
\end{itemize}

\subsubsection{LogisticRegression}
\begin{itemize}
\item model: LogisticRegression()
\item Accuracy score: 0.9115697310819262
\item Precission score: 0.5423728813559322
\item Recall score: 0.08926080892608089
\item F1-score: 0.1532934131736527
\end{itemize}

\subsubsection{XGBClassifier}
\begin{itemize}
\item model: XGBClassifier
\item Accuracy score: 0.9121013133208256
\item Precission score: 0.5580448065173116
\item Recall score: 0.09553695955369595
\item F1-score: 0.16314379279547486
\end{itemize}

\subsubsection{ExtraTreesClassifier}
\begin{itemize}
\item model: ExtraTreesClassifier()
\item Accuracy score: 0.8931519699812382
\item Precission score: 0.30462633451957294
\item Recall score: 0.1492329149232915
\item F1-score: 0.20032763866136205
\end{itemize}
\subsection{Conlusioni Valutazione del modello}
Possiamo notare facilmente che l'Accuracy score è molto elevata per tutti i modelli ma essendo questa un'applicazione medica poniamo l'accento sulle metriche riguardanti le previsioni positive: nelle prestazioni dei modelli sul dataset originale la precision e la recall non superano mai il 56\% e il 16\% quindi nel caso migliore avremo una precision di pochi punti superiore al 50\% ma con un altissimo tasso di falsi negativi che è esattamente il caso che più vorremmo evitare in un'applicazione di carattere medico. Constatato ciò abbiamo deciso di applicare sul dataset le seguenti classi della libreria \texttt{imblearn}:

\subsubsection{RandomUnderSampler}
\textbf{Descrizione:}\\
RandomUnderSampler è una tecnica di bilanciamento dei dati che agisce riducendo casualmente il numero di campioni dalla classe maggioritaria nel dataset. Questo approccio è utile quando si desidera ridurre l'eccesso di campioni della classe dominante per equilibrare il dataset.

\textbf{Funzionamento:}
\begin{enumerate}
    \item Seleziona casualmente un sottoinsieme dei campioni dalla classe maggioritaria.
    \item Mantiene solo i campioni selezionati nella nuova versione del dataset.
    \item È semplice da implementare ma potrebbe portare a una perdita di informazioni se i campioni importanti vengono eliminati.
\end{enumerate}

\subsubsection{RandomOverSampler}
\textbf{Descrizione:}\\
RandomOverSampler è un'altra tecnica di bilanciamento che opera aumentando casualmente il numero di campioni della classe minoritaria nel dataset. Questo metodo è efficace per migliorare la rappresentanza delle classi meno frequenti.

\textbf{Funzionamento:}
\begin{enumerate}
    \item Seleziona casualmente campioni dalla classe minoritaria.
    \item Replica questi campioni per aumentare il numero di istanze della classe minoritaria.
    \item Può portare a un aumento del rischio di overfitting se non viene controllato adeguatamente.
\end{enumerate}

\subsubsection{SMOTE (Synthetic Minority Over-sampling Technique)}
\textbf{Descrizione:}\\
SMOTE è una tecnica di sovracampionamento progettata per affrontare il problema della classe minoritaria creando nuovi campioni sintetici anziché replicare quelli esistenti. Utilizza l'interpolazione tra i campioni della classe minoritaria per generare nuovi esempi.

\textbf{Funzionamento:}
\begin{enumerate}
    \item Identifica i campioni della classe minoritaria vicini nel feature space.
    \item Crea nuovi campioni sintetici tra i campioni esistenti della classe minoritaria.
    \item Migliora la rappresentazione della classe minoritaria senza duplicare i campioni esistenti, riducendo il rischio di overfitting.
\end{enumerate}

\subsubsection{SMOTE-ENN (SMOTE + Edited Nearest Neighbors)}
\textbf{Descrizione:}\\
SMOTE-ENN è una combinazione di SMOTE e un'operazione di editing dei campioni della classe maggioritaria. Questo metodo non solo sovracampiona la classe minoritaria ma elimina anche i campioni della classe maggioritaria che sono vicini ai campioni della classe minoritaria.

\textbf{Funzionamento:}
\begin{enumerate}
    \item Utilizza SMOTE per generare campioni sintetici della classe minoritaria.
    \item Applica Edited Nearest Neighbors (ENN) per eliminare i campioni della classe maggioritaria che sono classificati in modo errato vicino ai campioni della classe minoritaria.
    \item Aiuta a ridurre il rumore introdotto da campioni sintetici non rappresentativi.
\end{enumerate}

\subsubsection{ADASYN (Adaptive Synthetic Sampling)}
\textbf{Descrizione:}\\
ADASYN è una tecnica di sovracampionamento che genera campioni sintetici per la classe minoritaria con una distribuzione proporzionale alla densità locale dei campioni vicini.

\textbf{Funzionamento:}
\begin{enumerate}
    \item Calcola la densità locale dei campioni minoritari.
    \item Genera campioni sintetici per la classe minoritaria con una densità proporzionale alla densità locale.
    \item Crea un bilanciamento più fine rispetto a SMOTE in aree del feature space dove la densità dei campioni è variabile.
\end{enumerate}

Lo script python utilizzato per bilanciare i dataset è data\_resampler.py
e salvano i nuovi dataset in ./data/
\subsubsection{data\_resampler.py}
\begin{figure}[H]
    \centering
    \includegraphics[width=1.3\linewidth]{data_resampler1.png}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=1.2\linewidth]{data_resampler2.png}
\end{figure}


\subsubsection{Test in seguito al bilanciamento}
Infine, abbiamo confrontato le prestazioni del nostro modello con i test sui modelli presenti nel notebook da cui abbiamo prelevato il dataset:
in seguito al bilanciamento dei dati, come riportato nel file \texttt{prestazione\_modelli.txt}, abbiamo ottenuto un notevole miglioramento delle prestazioni. Poniamo l'accento sulle metriche quali il richiamo (Recall) e la precision come metriche principali per valutare le prestazioni dei modelli. Questo perché, nel contesto delle malattie cardiache, è fondamentale porre la massima attenzione nell'identificare il maggior numero di casi positivi.



\begin{figure}[H]
    \centering
    \includegraphics[width=1.3\linewidth]{model_test_1.png}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=1.2\linewidth]{model_test2.png}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=1.2\linewidth]{model_test3.png}
\end{figure}
\begin{figure}[H]
    \centering
    \includegraphics[width=1.2\linewidth]{model_test4.png}
\end{figure}
I risulitati di Precision, Recall e F1 sono riportati di seguito: 

\begin{figure}[H]
    \centering
    \includegraphics[width=\linewidth]{istogramma_precision.png}
    \caption{Istogramma precision}
    \label{fig:precision}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=\linewidth]{istogramma_f1.png}
    \caption{Istogramma F1}
    \label{fig:f1}
\end{figure}

I punteggi migliori sono stati raggiunti da modelli che hanno effettuato la fase di training su dataset bilanciati con le classi SMOTEEN e RandomOverSampler, specialmente i modelli allenati con quest ultimo raggiungono percentuali molto simili sia di precision-scoree di recall-score, ne conseguono valori di F1-score molto simili.
Il modello che infine abbiamo scelto KNeighborsClassifier addestrato sul dataset bilanciato attraverso la classe RandomOverSampler che ha un'ottima precision-score (90\%) e un altrettanto ottima recall-score (89\%) questi punteggi permettono una F1-score che si attesta sul 90\% 

\section{Conclusion}
Per avviare il programma eseguendo lo script main.py.  
\subsection{Interfaccia}
Per interfacciarsi con il programma di planning abbiamo creato una semplice interfaccia grafica che permette di creare il profilo del paziente e avere un responso testuale in pochi semplici passi:
\subsubsection{Creazione scheda paziente}
\begin{figure}[H]
    \centering
    \includegraphics[width=\linewidth]{inter_1.png}
\end{figure}
\subsubsection{Abitudini paziente}
\begin{figure}[H]
    \centering
    \includegraphics[width=\linewidth]{interf_2.png}
\end{figure}
\subsubsection{Patologie paziente}
\begin{figure}[H]
    \centering
    \includegraphics[width=\linewidth]{interf_3.png}
\end{figure}
\subsubsection{Responso}
\begin{figure}[H]
    \centering
    \includegraphics[width=\linewidth]{interf_4.png}
\end{figure}
\end{document}
