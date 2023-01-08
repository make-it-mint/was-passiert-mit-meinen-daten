import pandas as pd
import numpy as np

import os

while True:
    

    filename = input('CSV Dateiname eingeben:')
    
    filepath = f"{os.getcwd()}/data/{filename}"

    if os.path.isfile(filepath):
        table = pd.read_csv(filepath)
        break
    else:
        print("Datei konnte nicht gefunden werden. Versuch es bitte erneut.")
        print("Bitte, Umfrageergebnisse in 'data' Ordner vom Repository ablegen und NUR den Dateinamen angeben.\nBeispiel: meine_umfrage.csv\n")
    

print(table.head)