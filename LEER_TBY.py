from codecs import ignore_errors
import os
import pandas as pd
import numpy as np

#///////////////////////////////////////////////////Variables globales/////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////Variables globales/////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////Variables globales/////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////Variables globales/////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////Variables globales/////////////////////////////////////////////////////////////////////////////////
line_NoS = 0
line_NoE = 0
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


#////////////////////////////////////////Main Code Adaptación del texto//////////////////////////////////////////////
#////////////////////////////////////////Main Code Adaptación del texto//////////////////////////////////////////////
#////////////////////////////////////////Main Code Adaptación del texto//////////////////////////////////////////////
#////////////////////////////////////////Main Code Adaptación del texto//////////////////////////////////////////////
#////////////////////////////////////////Main Code Adaptación del texto//////////////////////////////////////////////

x = file_start()
y = file_end()
file_Pin_Signal()
Structure_File()

df = pd.read_csv("OutSignal.txt")
df = df.sort_values(by = 'ID')

x = 0
y = np.array

df = df.assign(INICIAL = 0)
df = df.assign(TYPE = 0)
df = df.assign(PORCENT = 0)


for n in range(int(df.shape[0])):
    device = str(df.ID[n])
    aux = device[0]
    df.INICIAL.loc[n] = aux
    if(aux == 'C'):
        df.TYPE.loc[n] = 'Capacitor'
        CAP += 1
    if(aux == 'L'):
        df.TYPE.loc[n] = 'Inductor'
        IND += 1
    if(aux == 'Q'):
        df.TYPE.loc[n] = 'Library'
    if(aux == 'U'):
        df.TYPE.loc[n] = 'Library'
    if(aux == 'R'):
        df.TYPE.loc[n] = 'Resistor'
        RES += 1
    if(aux == 'V'):
        df.TYPE.loc[n] = 'Library'
    if(aux == 'P'):
        df.TYPE.loc[n] = 'Connector'
        CON += 1
    if(aux == 'K'):
        df.TYPE.loc[n] = 'Library'
    if(aux == 'D'):
        df.TYPE.loc[n] = 'Library'
    if(aux == 'J'):
        df.TYPE.loc[n] = 'Jumper'
        JUM += 1

status = 0
conteo = 1 
test = 0
res = 0

df = df

for n in range(int(df.shape[0])):
    device = str(df.ID[n])

    if(status == 0):
        Pdevice = device
        status = 1
        tested = str(df.Probe[n])
        if(tested == ' Probed'):
            test = test + 1
        continue
    if(status == 1):
        if(device == Pdevice):
            
            conteo = conteo + 1
            tested = str(df.Probe[n])

            if(tested == ' Probed'):
                test = test + 1
            Pdevice = device
        else:
            res = ((test) / (conteo)) * 100
            if(res>0):
                df.PORCENT.loc[n-1] = res
            tested = str(df.Probe[n])
            if(tested == ' Probed'):
                test = 1
            else:
                test = 0
            conteo = 1
            res = 0

            Pdevice = device


df['TEST'] = np.where(df['PORCENT']>=50,'Pass','Fail')
df['PORCENT'] = np.where(df['PORCENT']>0,df['PORCENT'],'')






    
print(OUTTYPE)
df = df.sort_values(by = 'ID')
df.to_csv("OUT0.csv", index=False)
print(OUT0.head())


    
        






































