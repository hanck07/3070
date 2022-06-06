from codecs import ignore_errors
from datetime import date
import os
import pandas as pd
import numpy as np
import openpyxl

#///////////////////////////////////////////////////Variables globales/////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////Variables globales/////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////Variables globales/////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////Variables globales/////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////Variables globales/////////////////////////////////////////////////////////////////////////////////

line_NoS = 0
line_NoE = 0
line_NoS1 = 0
line_NoE1 = 0

OUT0 = pd.DataFrame(columns= ['ID','PROBE','Device Test','Assembly 1','Type test','Presence','Polarity','Value','Status With Access', 'Porcent Access'])
OUTPORCENT = pd.DataFrame(columns=['Porcent'])
OUTDEVICE = pd.DataFrame(columns= ['Device/TEST'])
OUTTYPE = pd.DataFrame(columns= ['Type'])
CAP = IND = RES = CON = JUM = 0

#/////////////////////////////////////////////////////CONVERTIMOS UN ARCHIVO DE EXTENSION TBY TO TXT ///////////////////////////////////////////////////
#/////////////////////////////////////////////////////CONVERTIMOS UN ARCHIVO DE EXTENSION TBY TO TXT ///////////////////////////////////////////////////
#/////////////////////////////////////////////////////CONVERTIMOS UN ARCHIVO DE EXTENSION TBY TO TXT ///////////////////////////////////////////////////
#/////////////////////////////////////////////////////CONVERTIMOS UN ARCHIVO DE EXTENSION TBY TO TXT ///////////////////////////////////////////////////
#/////////////////////////////////////////////////////CONVERTIMOS UN ARCHIVO DE EXTENSION TBY TO TXT ///////////////////////////////////////////////////

#path = r'C:\git\MACRO_3070\TRY1.tby'
#newpath = r'C:\git\MACRO_3070\MACRO.txt'
#os.rename(path, newpath)

#////////////////////////////////////////////////////ABRIMOS EL ARCHIVO CON EXTENSIÓN TXT///////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////ABRIMOS EL ARCHIVO CON EXTENSIÓN TXT///////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////ABRIMOS EL ARCHIVO CON EXTENSIÓN TXT///////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////ABRIMOS EL ARCHIVO CON EXTENSIÓN TXT///////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////ABRIMOS EL ARCHIVO CON EXTENSIÓN TXT///////////////////////////////////////////////////////////////

Macro = open('MACRO.txt','r')
Aux = open('archivo.txt', 'w')

sMacro = Macro.read()
Aux.write(sMacro)
Macro.close()
Aux.close()

#////////////////////////////////////////FUNCIONES GLOBALES///////////////////////////////////////////////////////
#////////////////////////////////////////FUNCIONES GLOBALES///////////////////////////////////////////////////////
#////////////////////////////////////////FUNCIONES GLOBALES///////////////////////////////////////////////////////
#////////////////////////////////////////FUNCIONES GLOBALES///////////////////////////////////////////////////////
#////////////////////////////////////////FUNCIONES GLOBALES///////////////////////////////////////////////////////

#///////////////////////////Obtenemos la nomenclatura a utilizar en el archivo correspondiente////////////////////
#///////////////////////////Obtenemos la nomenclatura a utilizar en el archivo correspondiente////////////////////

def nomenclatura():

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
    
    BOM.to_csv('H1.csv',index=False)

    x = BOM['INI'].unique()
    print(x)
    y = BOM['NOM'].unique()
    print(y)

    p = open('NOM.txt','w')
    p.truncate(0)
    p.write('INI,NOM')
    p.write('\n')
    line_NoSo = 0
    for N in range(x.size):
        line_NoSo += 1
        p.write(x[N])
        p.write(',')
        p.write(y[N])
        p.write('\n')

#////////////////////////////////////////Obtener los Pin's Signal/////////////////////////////////////////////////
#////////////////////////////////////////Obtener los Pin's Signal/////////////////////////////////////////////////
def file_start():

    with open("archivo.txt","r") as temp_f:
        line_NoS = 0
        for linea in temp_f:
            line_NoS += 1
            linea = linea.rstrip()
            if "Component Pin's Signal" in linea:
                return(line_NoS)

def file_end():

    with open("archivo.txt","r") as temp_f:
        line_NoE = 0
        for linea in temp_f:
            line_NoE += 1
            linea = linea.rstrip()
            if "Number of components fully probed" in linea:
                return(line_NoE)

def file_Pin_Signal():
        p = open('PinSignal.txt','r+')
        p.truncate(0)
        with open("archivo.txt","r") as temp_f:
            line_NoSo = 0
            for linea in temp_f:
                line_NoSo += 1
                if(line_NoSo - 1 > x and line_NoSo < y):
                    linea = linea.rstrip()
                    p.writelines(linea)
                    p.write("\n")

def Structure_File():
    p = open('OutSignal.txt','w')
    p.truncate(0)
    p.write("ID,PIN,Signal,Signal,Probe")
    p.write("\n")
    with open("PinSignal.txt", 'r') as temp_f:
        line_NoSo = 0
        for linea in temp_f:
            line_NoSo += 1
            linea = linea.rstrip()
            
            if (bool(linea)):
                aux0 = str(linea)
                aux = aux0[0]
                if(aux != ' '):
                    father = linea
                if(aux == ' '):
                    salida = father + ',' + linea
                    p.write(salida)
                    p.write("\n")

#////////////////////////////////////////Obtenemos el barrel size de los TP's///////////////////////////////////////
#////////////////////////////////////////Obtenemos el barrel size de los TP's///////////////////////////////////////

def file_start_Probes():
    with open("archivo.txt","r") as temp_f:
        line_NoS1 = 0
        for linea in temp_f:
            line_NoS1 += 1
            linea = linea.rstrip()
            if "Placed 100's" in linea:
                return(line_NoS1)

def file_end_Probes():
    with open("archivo.txt","r") as temp_f:
        line_NoE1 = 0
        for linea in temp_f:
            line_NoE1 += 1
            linea = linea.rstrip()
            if "Component Pin's Signal" in linea:
                return(line_NoE1)

def file_Barrel_Size():
        p = open('BarrelSignal.txt','w')
        p.truncate(0)
        with open("archivo.txt","r") as temp_f:
            line_NoSo = 0
            for linea in temp_f:
                line_NoSo += 1
                if(line_NoSo + 1 > x1 and line_NoSo < y1):
                    linea = linea.rstrip()
                    p.writelines(linea)
                    p.write("\n")

def Structure_barrel_Size():
    p = open("OutSignal1.txt","w")
    p.truncate(0)

    with open("BarrelSignal.txt","r") as temp_f:
        line_NoSo = 0
        for line in temp_f:
            line_NoSo += 1
            linea = line.rstrip()

            if(bool(linea)):
                aux = linea[4]

                if "Placed 100" in linea:
                    a = 1
                    continue
                if "Placed 75" in linea:
                    a = 2
                if "Placed 50" in linea:
                    a = 3
                if "Placed 39" in linea:
                    a = 4

                if aux ==  ' ' and a == 1:
                    salida = '100' + linea
                    salida = salida.split()
                    p.write(str(salida))
                    p.write("\n")
                
                if aux ==  ' ' and a == 2:
                    salida = '75' + linea
                    salida = salida.split()
                    salida = str(salida)
                    p.write(salida)
                    p.write("\n")
                
                if aux ==  ' ' and a == 3:
                    salida = '50' + linea
                    salida = salida.split()
                    salida = str(salida)
                    p.write(salida)
                    p.write("\n")
                
                if aux ==  ' ' and a == 4:
                    salida = '39' + linea
                    salida = salida.split()
                    salida = str(salida)
                    p.write(salida)
                    p.write("\n")

def Structure_CSV_Barrel():
        p = open('Output2.txt','w')
        p.truncate(0)
        HEAD = "Barrel,NO,SIGNAL,X,Y,PIN,PAD,SURFACE,SURFACE1"
        p.write(HEAD)
        p.write('\n')
        with open("OutSignal1.txt","r") as temp_f:
            line_NoSo = 0
            for linea in temp_f:
                line_NoSo += 1
                linea = linea.rstrip()
                linea = linea.replace('[', '')
                linea = linea.replace(']','')
                linea = linea.replace("'",'')
                p.write(linea)
                p.write("\n")

#/////////////////////////////////////Obtenemos el ID de los artículos dentro del desarrollo a partir del BOM/////////////////////////////////
#/////////////////////////////////////Obtenemos el ID de los artículos dentro del desarrollo a partir del BOM/////////////////////////////////
#/////////////////////////////////////Obtenemos el ID de los artículos dentro del desarrollo a partir del BOM/////////////////////////////////
#/////////////////////////////////////Obtenemos el ID de los artículos dentro del desarrollo a partir del BOM/////////////////////////////////
#/////////////////////////////////////Obtenemos el ID de los artículos dentro del desarrollo a partir del BOM/////////////////////////////////



#////////////////////////////////////////Main Code Adaptación del texto//////////////////////////////////////////////
#////////////////////////////////////////Main Code Adaptación del texto//////////////////////////////////////////////
#////////////////////////////////////////Main Code Adaptación del texto//////////////////////////////////////////////
#////////////////////////////////////////Main Code Adaptación del texto//////////////////////////////////////////////
#////////////////////////////////////////Main Code Adaptación del texto//////////////////////////////////////////////
status = 0
conteo = 1 
test = 0
res = 0
cien = set = cin = trein = 0

x = file_start()
y = file_end()
x1 = file_start_Probes()
y1 = file_end_Probes()


file_Barrel_Size()
file_Pin_Signal()
Structure_File()
Structure_barrel_Size()
Structure_CSV_Barrel()


df = pd.read_csv("OutSignal.txt")
df = df.sort_values(by = 'ID')
bf = pd.read_csv("Output2.txt")

x = 0
y = np.array

#/////////////////////////////////////////////////Asignación de nuevas filas a tabla principal/////////////////////////////////////
#/////////////////////////////////////////////////Asignación de nuevas filas a tabla principal/////////////////////////////////////
#/////////////////////////////////////////////////Asignación de nuevas filas a tabla principal/////////////////////////////////////
#/////////////////////////////////////////////////Asignación de nuevas filas a tabla principal/////////////////////////////////////
#/////////////////////////////////////////////////Asignación de nuevas filas a tabla principal/////////////////////////////////////

df = df.assign(INICIAL = 0)
df = df.assign(TYPE = 0)
df = df.assign(PORCENT = 0)
df = df.assign(Barrel = 0)

NOM = pd.read_csv('NOM.txt', sep=',')

for n in range(int(df.shape[0])):
    device = str(df.ID[n])
    aux = device[0]
    aux1 = device[1]
    if aux1.isdigit() == False:
        aux1 = device[2]
        if aux1.isdigit() == False:
            aux = device[0:3]
        else:
            aux = device[0:2]

    df.INICIAL.loc[n] = aux
    for m in range(int(NOM.shape[0])):
        if(aux == NOM.INI[m]):
            df.TYPE.loc[n] = NOM.NOM[m]

df.to_csv("H1.csv",index=False)
print(df.head())
df = df

pt = pd.read_csv("H1.csv")


for n in range(int(pt.shape[0])):
    device = str(pt.ID[n])

    if(status == 0):
        Pdevice = device
        status = 1
        tested = str(pt.Probe[n])
        if(tested == ' Probed'):
            test = test + 1
        continue
    if(status == 1):
        if(device == Pdevice):
            
            conteo = conteo + 1
            tested = str(pt.Probe[n])

            if(tested == ' Probed'):
                test = test + 1
            Pdevice = device
        else:
            res = ((test) / (conteo)) * 100
            if(res>0):
                pt.PORCENT.loc[n-1] = res

            tested = str(pt.Probe[n])
            if(tested == ' Probed'):
                test = 1
            else:
                test = 0
            conteo = 1
            res = 0

            Pdevice = device


pt = pt.assign(SURFACE = 0)

for n in range(int(bf.shape[0])):
    Signal = 'Signal:' + str(bf.SIGNAL[n])
    Signal = Signal.replace(' ', '')

    for j in range(int(pt.shape[0])):
        Signal1 = pt.Signal[j]
        Signal1 = Signal1.replace(' ' , '')

        if(Signal == Signal1):
            Signal2 = bf.Barrel[n]
            Signal3 = bf.SURFACE1[n]
            pt.Barrel.loc[j] = Signal2
            pt.SURFACE.loc[j] = Signal3

pt['TEST'] = np.where(pt['PORCENT']>50,'Pass','Fail')
pt['PORCENT'] = np.where(pt['PORCENT']>0,pt['PORCENT'],'')

x = pt.apply(lambda x : x['Barrel'] == 100 , axis=1)
y = pt.apply(lambda x : x['Barrel'] == 75 , axis=1)
z = pt.apply(lambda x : x['Barrel'] == 50 , axis=1)
z1 = pt.apply(lambda x : x['Barrel'] == 39 , axis=1)


for n in range(x.size):
    if(x[n] == True):
        cien = cien + 1

for n in range(y.size):
    if(y[n] == True):
        set = set + 1

for n in range(z.size):
    if(z[n] == True):
        cin = cin + 1

for n in range(z1.size):
    if(z1[n] == True):
        trein = trein + 1

print(cien)
print(set)
print(cin)
print(trein)

print(type(x))


print(cien)

dates = {
    "Pin's 100" : [int(cien)],
    "Pin's 75"  : [int(set)],
    "Pin's 50"  : [int(cin)],
    "Pin's 39"  : [int(trein)],
}

mec = pd.DataFrame(dates)

pt.to_csv("OUT0.csv", index=False)

pt.to_excel("Hola.xlsx",sheet_name="General")

Esp = pt

Esp = Esp.sort_values(by="ID")

with pd.ExcelWriter("Hola.xlsx", mode='a', engine='openpyxl') as writer:
    mec.to_excel(writer, sheet_name="Mecanica")
    Esp.to_excel(writer, sheet_name="Resume")

ot = pd.read_csv("OUT0.csv")


print(ot.head())
print(OUT0.head())


    
        





































