from tokenize import Name
import pandas as pd
from string import ascii_uppercase as asc



BOM = pd.read_csv('BOM.txt', sep=',', names=["ID","SIGNAL","NAN"])
BOM.pop('NAN')

BOM = BOM.sort_values(by = 'ID')
BOM =BOM.assign(INI = 0)
BOM = BOM.assign(NOM = 0)


for n in range(BOM.shape[0]):
    cad1 = BOM.ID[n]
    cad1 = str(cad1[0])
    BOM.INI.loc[n] = cad1
    aux = str(BOM.SIGNAL[n])
    c = int(aux.find(','))
    c1 = slice(c)
    c2 = str(aux[c1])
    BOM.NOM.loc[n] = c2


    
x = BOM['INI'].unique()
y = BOM['NOM'].unique()



p = open('NOM.txt','w')
p.truncate(0)

line_NoSo = 0
for N in range(x.size):
    line_NoSo += 1
    p.write(x[N])
    p.write(',')
    p.write(y[N])
    p.write('\n')












               
