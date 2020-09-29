# HP-Fanfictions

Das Projekt umfasst einen Vergleich zwischen Harry Potter Fanfictions und der Original HP-Reihe. Dabei werden vor allem die Figuren der Texte analysiert und miteinander verglichen. 
beihaltet LFS Dateien: Download mit Befehl *git lsf fetch*

## Ordnerstruktur: 

### datasets: 
    beinhaltet die Datensätze HP Fanfictions und Original HP als csv-Dateien

### Fanfictions.zip:
    beinhaltet alle Harry Potter Fanfictiontexte

### Originaltexte:
    beinhaltet alle 7 HP-Bände als txt-Dateien

### Kwic:
     beinhaltet generierte csv-Dateien mit POS und Polaritäten sowie Kontext pro Figur
     beinhaltet Bilder zu Figuren und Interaktionen nach Original und Fanfic aufgeteilt

### Network: 
    beinhaltet alle Dateien und Bilder, die in der Netzwerkanalyse erstellt wurden

### Sentiment:
    beinhaltet alle Bilder zu Sentiment Analyse und Kollokationen

## Dateien:

#### helpyy.py: 
    Funktionen für POS

#### 01_fanfiction_get_data.ipynb:
    zieht alle Harry Potter Fanfictions in einen Ordner

#### 02_fanfiction_get_metadata.ipynb:
    generiert Metadaten aus Fanfictiontexten und Originaltexten

#### 03_visualize_metadata.ipynb:
    visualisiert Metadaten

#### 04_Netzweranalyse.ipynb:
    beinhaltet Netzwerkanalyse von Fanfic und Original sowie Vergleich von Metriken

#### 05_Concordance_Matrix.ipynb:
    Erstellen von KWICs für Original und Fanfic + POS Tagging

#### 06_visualize_POS.ipynb:  
    beinhaltet Figurenanalyse und Interaktionen zwischen Paaren

#### 07_Sentiment_TextBlob.ipynb:
    beinhaltet Sentiment Analyse und Kollokationen



```python

```
