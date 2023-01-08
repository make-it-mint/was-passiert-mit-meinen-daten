import pandas as pd
import numpy as np

import os


print("Bitte, Umfrageergebnisse in 'data' Ordner vom Repository ablegen")

filename = input('CSV Dateiname eingeben:')

table = pd.read_csv(f"{os.getcwd()}/data/{filename}.csv")

print(table.head)