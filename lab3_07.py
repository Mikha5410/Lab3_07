import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy as np
import tabulate

#УСТАНОВИТЬ openpyxl

spin = 0.5
plank = 6.62607015e-34
magneton=5.0507837461e-27

cols=[1,2,3]
data = pd.read_excel('lab7.xlsx', sheet_name = 'Lab7', usecols = cols)
data.head()

current = data['I'].tolist()
current = list(map(float, current))

Nfrequency = data['f'].tolist()
Nfrequency = list(map(float, Nfrequency))

field = data['Bo'].tolist()
field = list(map(float, field))


frequency = []
for val in range (len(current)):
    frequency += [Nfrequency[val]*1000]

Gamma = []
Momentum = []
Otn_Momentum = []

for val in range( len(frequency) ):
    Gamma += [frequency[val]/field[val]]
    Momentum += [Gamma[val]*plank*spin]

SrMomentum = np.mean(Momentum)
Otn_Momentum = SrMomentum/magneton


SquareMomentumMinusSrMomentum = []
MomentumMinusSrMomentum = []

for val in range (len(frequency)):
    MomentumMinusSrMomentum += [Momentum[val] - SrMomentum]
    SquareMomentumMinusSrMomentum += [MomentumMinusSrMomentum[val]**2]

SumSquareMomentumMinusSrMomentum = sum(SquareMomentumMinusSrMomentum)
sigma = np.sqrt(SumSquareMomentumMinusSrMomentum/(10*9))

################################################################################
teta= 1.1 # коэффициент Стьюдента для доверительной вероятность 0.68 и 10 измерений
################################################################################

Pogreshnost = (sigma * teta)/magneton




table = pd.DataFrame({'I' : current,
                   'f' : frequency,
                   'B0': field,
                   'Gamma': Gamma,
                   'Momentum' : Momentum,
                   'Otnos Momentum' : Otn_Momentum,
                   'Pogreshnost' :  Pogreshnost
                     })
print(table.to_markdown())

print(f"\U000003BC = {Otn_Momentum:.3f} \u00B1 {Pogreshnost:.3f}")