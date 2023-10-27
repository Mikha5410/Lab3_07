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


Square_Deviation = []
Deviation = []

for val in range (len(frequency)):
    Deviation += [Momentum[val] - SrMomentum]
    Square_Deviation += [Deviation[val]**2]

Sum_Deviation = sum(Square_Deviation)
sigma = np.sqrt(Sum_Deviation/(10*9))

################################################################################
teta= 1.1 # коэффициент Стьюдента для доверительной вероятность 0.68 и 10 измерений
################################################################################

Pogreshnost = (sigma * teta)/magneton

def precision_round(number, digits):
    power = "{:e}".format(number).split('e')[1]
    return round(number, -(int(power) - digits))


for val in range(len(frequency)):
    frequency[val] = precision_round(frequency[val],2)
    field[val] = precision_round(field[val],2)
    Momentum[val] = precision_round(Momentum[val],3)
    Gamma[val] = precision_round(Gamma[val],3)


table = pd.DataFrame({'I, А' : current,
                   'f, Гц' : frequency,
                   'B\u2080, Тл': field,
                   '\u03B3': Gamma,
                   '\u03BC, Дж*Тл\u207B\u00B9' : Momentum

                     })
print(table.to_markdown())
print(f"\u0394\u03BC\u2099 = {Pogreshnost:.3f}")
print(f"\u03BC\u2099 = {Otn_Momentum:.3f} \u00B1 {Pogreshnost:.3f}")