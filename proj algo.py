##importation
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
from math import *
import statistics
doc = pd.read_csv(r"C:\Users\aachi\Desktop\projet_algo\EIVP_KM.csv", sep = ";", header = None)

##fonctions valeurs statistique

def min(liste):
    a = liste[0]
    for i in range (1,len(liste)):
        if a>liste[i]:
            a = liste[i]
    return a

def max(liste):
    a = liste[0]
    for i in range (1,len(liste)):
        if a<liste[i]:
            a = liste[i]
    return a

def moyenne(liste):
    a = 0
    for i in range (len(liste)):
        a+=liste[i]
    return a/len(liste)

def ecartType(liste):
    a = 0
    for i in range(len(liste)):
        a+=(liste[i]-moyenne(liste))**2
    return (a/len(liste))**(1/2)

def mediane(liste):
    return statistics.median(liste)

def coefCorr(liste1,liste2):
    return np.corrcoef(liste1,liste2)[0][1]

## calcul humidex

def alpha(temperature,humidite):
    return 17.27*temperature/(237.7+temperature) + log(humidite)

def temperatureRosee(temperature, humidite):
    return 237.7*alpha(temperature,humidite)/(17.27-alpha(temperature,humidite))

def humidex(temperature,humidite):
    return temperature + 0.5555*(6.11*2.7183**(5417.7530*(1/273.16-1/(273.15 + temperatureRosee(temperature,humidite) )))-10)

##création des listes

noise1 = []
temperature1 = []
humidity1 = []
lum1 = []
co21 = []
humidex1 = []
sent_at1 = []

noise2 = []
temperature2 = []
humidity2 = []
lum2 = []
co22 = []
humidex2 = []
sent_at2 = []

noise3 = []
temperature3 = []
humidity3 = []
lum3 = []
co23 = []
humidex3 = []
sent_at3 = []

noise4 = []
temperature4 = []
humidity4 = []
lum4 = []
co24 = []
humidex4 = []
sent_at4 = []

noise5 = []
temperature5 = []
humidity5 = []
lum5 = []
co25 = []
humidex5 = []
sent_at5 = []

noise6 = []
temperature6 = []
humidity6 = []
lum6 = []
co26 = []
humidex6 = []
sent_at6 = []


for i in range (1,len(doc)):
    if int(doc[0][i])==1:
        noise1.append(float(doc[1][i]))
        temperature1.append(float(doc[2][i]))
        humidity1.append(float(doc[3][i]))
        lum1.append(float(doc[4][i]))
        co21.append(float(doc[5][i]))
        humidex1.append(humidex(float(doc[2][i]),float(doc[3][i])))
        sent_at1.append(datetime.datetime(int(doc[6][i][0:4]),int(doc[6][i][5:7]),int(doc[6][i][8:10]),int(doc[6][i][11:13]),int(doc[6][i][14:16]),int(doc[6][i][17:19])))
    elif int(doc[0][i])==2:
        noise2.append(float(doc[1][i]))
        temperature2.append(float(doc[2][i]))
        humidity2.append(float(doc[3][i]))
        lum2.append(float(doc[4][i]))
        co22.append(float(doc[5][i]))
        humidex2.append(humidex(float(doc[2][i]),float(doc[3][i])))
        sent_at2.append(datetime.datetime(int(doc[6][i][0:4]),int(doc[6][i][5:7]),int(doc[6][i][8:10]),int(doc[6][i][11:13]),int(doc[6][i][14:16]),int(doc[6][i][17:19])))
    elif int(doc[0][i])==3:
        noise3.append(float(doc[1][i]))
        temperature3.append(float((doc[2][i])))
        humidity3.append(float(doc[3][i]))
        lum3.append(float(doc[4][i]))
        co23.append(float(doc[5][i]))
        humidex3.append(humidex(float(doc[2][i]),float(doc[3][i])))
        sent_at3.append(datetime.datetime(int(doc[6][i][0:4]),int(doc[6][i][5:7]),int(doc[6][i][8:10]),int(doc[6][i][11:13]),int(doc[6][i][14:16]),int(doc[6][i][17:19])))
    elif int(doc[0][i])==4:
        noise4.append(float(doc[1][i]))
        temperature4.append(float(doc[2][i]))
        humidity4.append(float(doc[3][i]))
        lum4.append(float(doc[4][i]))
        co24.append(float(doc[5][i]))
        humidex4.append(humidex(float(doc[2][i]),float(doc[3][i])))
        sent_at4.append(datetime.datetime(int(doc[6][i][0:4]),int(doc[6][i][5:7]),int(doc[6][i][8:10]),int(doc[6][i][11:13]),int(doc[6][i][14:16]),int(doc[6][i][17:19])))
    elif int(doc[0][i])==5:
        noise5.append(float(doc[1][i]))
        temperature5.append(float((doc[2][i])))
        humidity5.append(float(doc[3][i]))
        lum5.append(float(doc[4][i]))
        co25.append(float(doc[5][i]))
        humidex5.append(humidex(float(doc[2][i]),float(doc[3][i])))
        sent_at5.append(datetime.datetime(int(doc[6][i][0:4]),int(doc[6][i][5:7]),int(doc[6][i][8:10]),int(doc[6][i][11:13]),int(doc[6][i][14:16]),int(doc[6][i][17:19])))
    elif int(doc[0][i])==6:
        noise6.append(float(doc[1][i]))
        temperature6.append(float(doc[2][i]))
        humidity6.append(float(doc[3][i]))
        lum6.append(float(doc[4][i]))
        co26.append(float(doc[5][i]))
        humidex6.append(humidex(float(doc[2][i]),float(doc[3][i])))
        sent_at6.append(datetime.datetime(int(doc[6][i][0:4]),int(doc[6][i][5:7]),int(doc[6][i][8:10]),int(doc[6][i][11:13]),int(doc[6][i][14:16]),int(doc[6][i][17:19])))


## inputs

debut = str(input('date de début ? (AAAA-MM-JJ)'))
fin = str(input('date de fin ? (AAAA-MM-JJ)'))
variable = str(input('variable ?'))

start_date = datetime.datetime(int(debut[0:4]),int(debut[5:7]),int(debut[8:10]),0,0,0)
end_date = datetime.datetime(int(fin[0:4]),int(fin[5:7]),int(fin[8:10]),23,59,59)

## encadrement pour les valeurs statistiques

#indices laps de temps capteur 1
if start_date>sent_at1[0] and start_date<sent_at1[-1]:
    s1=0
    while start_date>sent_at1[s1]:
        s1+=1
elif start_date<sent_at1[0]:
    s1 = 0
else :
    s1 = -1

if end_date>sent_at1[0] and end_date<sent_at1[-1]:
    e1=0
    while end_date>sent_at1[e1]:
        e1+=1
elif end_date>sent_at1[-1]:
    e1 = -1
else :
    e1 = 0

#indices laps de temps capteur 2
if start_date>sent_at2[0] and start_date<sent_at2[-1]:
    s2=0
    while start_date>sent_at2[s2]:
        s2+=1
elif start_date<sent_at2[0]:
    s2 = 0
else :
    s2 = -1

if end_date>sent_at2[0] and end_date<sent_at2[-1]:
    e2=0
    while end_date>sent_at2[e2]:
        e2+=1
elif end_date>sent_at2[-1]:
    e2 = -1
else :
    e2 = 0

#indices laps de temps capteur 3
if start_date>sent_at3[0] and start_date<sent_at3[-1]:
    s3=0
    while start_date>sent_at3[s3]:
        s3+=1
elif start_date<sent_at3[0]:
    s3 = 0
else :
    s3 = -1

if end_date>sent_at3[0] and end_date<sent_at3[-1]:
    e3=0
    while end_date>sent_at3[e3]:
        e3+=1
elif end_date>sent_at3[-1]:
    e3 = -1
else :
    e3 = 0

#indices laps de temps capteur 4
if start_date>sent_at4[0] and start_date<sent_at4[-1]:
    s4=0
    while start_date>sent_at4[s4]:
        s4+=1
elif start_date<sent_at4[0]:
    s4 = 0
else :
    s4 = -1

if end_date>sent_at4[0] and end_date<sent_at4[-1]:
    e4=0
    while end_date>sent_at4[e4]:
        e4+=1
elif end_date>sent_at4[-1]:
    e4 = -1
else :
    e4 = 0

#indices laps de temps capteur 5
if start_date>sent_at5[0] and start_date<sent_at5[-1]:
    s5=0
    while start_date>sent_at5[s5]:
        s5+=1
elif start_date<sent_at5[0]:
    s5 = 0
else :
    s5 = -1

if end_date>sent_at5[0] and end_date<sent_at5[-1]:
    e5=0
    while end_date>sent_at5[e5]:
        e5+=1
elif end_date>sent_at5[-1]:
    e5 = -1
else :
    e5 = 0

#indices laps de temps capteur 6
if start_date>sent_at6[0] and start_date<sent_at6[-1]:
    s6=0
    while start_date>sent_at6[s6]:
        s6+=1
elif start_date<sent_at6[0]:
    s6 = 0
else :
    s6 = -1

if end_date>sent_at6[0] and end_date<sent_at6[-1]:
    e6=0
    while end_date>sent_at6[e6]:
        e6+=1
elif end_date>sent_at6[-1]:
    e6 = -1
else :
    e6 = 0


##tracé de la courbe

plt.clf()
if variable == 'Temperature' or variable == 'temperature' or variable == 'Température' or variable == 'température':
    plt.subplot(321)
    plt.plot(sent_at1, temperature1, label='capteur 1')
    plt.text(start_date,min(temperature1[s1:e1+1]),max(temperature1[s1:e1+1]))
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(322)
    plt.plot(sent_at2, temperature2, label='capteur 2')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(323)
    plt.plot(sent_at3, temperature3, label='capteur 3')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(324)
    plt.plot(sent_at4, temperature4, label='capteur 4')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(325)
    plt.plot(sent_at5, temperature5, label='capteur 5')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(326)
    plt.plot(sent_at6, temperature6, label='capteur 6')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.show()
elif variable == 'bruit' or variable == 'Bruit':
    plt.subplot(321)
    plt.plot(sent_at1, noise1, label='capteur 1')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(322)
    plt.plot(sent_at2, noise2, label='capteur 2')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(323)
    plt.plot(sent_at3, noise3, label='capteur 3')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(324)
    plt.plot(sent_at4, noise4, label='capteur 4')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(325)
    plt.plot(sent_at5, noise5, label='capteur 5')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(326)
    plt.plot(sent_at6, noise6, label='capteur 6')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.show()
elif variable == 'Humidité' or variable == 'humidité' or variable == 'Humidite' or variable == 'humidite' :
    plt.subplot(321)
    plt.plot(sent_at1, humidity1, label='capteur 1')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(322)
    plt.plot(sent_at2, humidity2, label='capteur 2')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(323)
    plt.plot(sent_at3, humidity3, label='capteur 3')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(324)
    plt.plot(sent_at4, humidity4, label='capteur 4')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(325)
    plt.plot(sent_at5, humidity5, label='capteur 5')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(326)
    plt.plot(sent_at6, humidity6, label='capteur 6')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.show()
elif variable == 'Lumière' or variable == 'lumière' or variable == 'Lumiere' or variable == 'lumiere' :
    plt.subplot(321)
    plt.plot(sent_at1, lum1, label='capteur 1')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(322)
    plt.plot(sent_at2, lum2, label='capteur 2')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(323)
    plt.plot(sent_at3, lum3, label='capteur 3')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(324)
    plt.plot(sent_at4, lum4, label='capteur 4')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(325)
    plt.plot(sent_at5, lum5, label='capteur 5')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(326)
    plt.plot(sent_at6, lum6, label='capteur 6')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.show()
elif variable == 'CO2' or variable == 'Co2' or variable == 'co2':
    plt.subplot(321)
    plt.plot(sent_at1, co21, label='capteur 1')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(322)
    plt.plot(sent_at2, co22, label='capteur 2')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(323)
    plt.plot(sent_at3, co23, label='capteur 3')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(324)
    plt.plot(sent_at4, co24, label='capteur 4')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(325)
    plt.plot(sent_at5, co25, label='capteur 5')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(326)
    plt.plot(sent_at6, co26, label='capteur 6')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.show()
elif variable == 'humidex' or variable == 'Humidex':
    plt.subplot(321)
    plt.plot(sent_at1, humidex1, label='capteur 1')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(322)
    plt.plot(sent_at2, humidex2, label='capteur 2')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(323)
    plt.plot(sent_at3, humidex3, label='capteur 3')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(324)
    plt.plot(sent_at4, humidex4, label='capteur 4')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(325)
    plt.plot(sent_at5, humdiex5, label='capteur 5')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(326)
    plt.plot(sent_at6, humidex6, label='capteur 6')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.show()
else :
    print ("erreur d'entrée de variable")

