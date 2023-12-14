# -*- coding: utf -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_row', None)
pd.set_option('display.width', 1000)
data_incidents = pd.read_excel("./incident.xlsx", index_col='Ouvert', parse_dates=True)

di2 = data_incidents.loc[data_incidents.loc[:, 'Groupe d\'affectation'] == 'L2 BI Support GRP']
di2 = di2.drop(['Catégorie', 'Sous-catégorie', 'Service', 'CI affecté', 'Priorité', 'État', 'Escalade', 'Groupe d\'affectation'], axis=1)

print("--------DI ---------")
print(data_incidents.describe())
print("--------DI2---------")
print(di2.describe())
print("-----------------")
print(di2)


handle = open("./results.txt", "w")
handle.write(str(di2))

handle.close()
