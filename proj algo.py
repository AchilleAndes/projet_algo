##importation
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import statistics
from math import *
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
variable1 = str(input('première variable ?'))
boole = str(input("afficher une seconde variable ? (oui/non)"))
if boole == "oui" or boole == "Oui" :
    variable2 = str(input('seconde variable ?'))
else :
    variable2 = None

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
if variable1 == 'Temperature' or variable1 == 'temperature' or variable1 == 'Température' or variable1 == 'température':
    plt.subplot(321)
    plt.plot(sent_at1, temperature1, label='tem 1')
    plt.text(start_date, max(temperature1), u"min temp = %f"%(min(temperature1)), fontsize=7)
    plt.text(start_date, 12*(max(temperature1)-min(temperature1))/13 + min(temperature1), u"max temp = %f"%(max(temperature1)), fontsize=7)
    plt.text(start_date, 11*(max(temperature1)-min(temperature1))/13 + min(temperature1), u"moy temp = %f"%(moyenne(temperature1)), fontsize=7)
    plt.text(start_date, 10*(max(temperature1)-min(temperature1))/13 + min(temperature1), u"med temp = %f"%(mediane(temperature1)), fontsize=7)
    plt.text(start_date, 9*(max(temperature1)-min(temperature1))/13 + min(temperature1), u"EcTyp temp = %f"%(ecartType(temperature1)), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(322)
    plt.plot(sent_at2, temperature2, label='tem 2')
    plt.text(start_date, max(temperature2), u"min temp = %f"%(min(temperature2)), fontsize=7)
    plt.text(start_date, 12*(max(temperature2)-min(temperature2))/13 + min(temperature2), u"max temp = %f"%(max(temperature2)), fontsize=7)
    plt.text(start_date, 11*(max(temperature2)-min(temperature2))/13 + min(temperature2), u"moy temp = %f"%(moyenne(temperature2)), fontsize=7)
    plt.text(start_date, 10*(max(temperature2)-min(temperature2))/13 + min(temperature2), u"med temp = %f"%(mediane(temperature2)), fontsize=7)
    plt.text(start_date, 9*(max(temperature2)-min(temperature2))/13 + min(temperature2), u"EcTyp temp = %f"%(ecartType(temperature2)), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(323)
    plt.plot(sent_at3, temperature3, label='tem 3')
    plt.text(start_date, max(temperature3), u"min temp = %f"%(min(temperature3)), fontsize=7)
    plt.text(start_date, 12*(max(temperature3)-min(temperature3))/13 + min(temperature3), u"max temp = %f"%(max(temperature3)), fontsize=7)
    plt.text(start_date, 11*(max(temperature3)-min(temperature3))/13 + min(temperature3), u"moy temp = %f"%(moyenne(temperature3)), fontsize=7)
    plt.text(start_date, 10*(max(temperature3)-min(temperature3))/13 + min(temperature3), u"med temp = %f"%(mediane(temperature3)), fontsize=7)
    plt.text(start_date, 9*(max(temperature3)-min(temperature3))/13 + min(temperature3), u"EcTyp temp = %f"%(ecartType(temperature3)), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(324)
    plt.plot(sent_at4, temperature4, label='tem 4')
    plt.text(start_date, max(temperature4), u"min temp = %f"%(min(temperature4)), fontsize=7)
    plt.text(start_date, 12*(max(temperature4)-min(temperature4))/13 + min(temperature4), u"max temp = %f"%(max(temperature4)), fontsize=7)
    plt.text(start_date, 11*(max(temperature4)-min(temperature4))/13 + min(temperature4), u"moy temp = %f"%(moyenne(temperature4)), fontsize=7)
    plt.text(start_date, 10*(max(temperature4)-min(temperature4))/13 + min(temperature4), u"med temp = %f"%(mediane(temperature4)), fontsize=7)
    plt.text(start_date, 9*(max(temperature4)-min(temperature4))/13 + min(temperature4), u"EcTyp temp = %f"%(ecartType(temperature4)), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(325)
    plt.plot(sent_at5, temperature5, label='tem 5')
    plt.text(start_date, max(temperature5), u"min temp = %f"%(min(temperature5)), fontsize=7)
    plt.text(start_date, 12*(max(temperature5)-min(temperature5))/13 + min(temperature5), u"max temp = %f"%(max(temperature5)), fontsize=7)
    plt.text(start_date, 11*(max(temperature5)-min(temperature5))/13 + min(temperature5), u"moy temp = %f"%(moyenne(temperature5)), fontsize=7)
    plt.text(start_date, 10*(max(temperature5)-min(temperature5))/13 + min(temperature5), u"med temp = %f"%(mediane(temperature5)), fontsize=7)
    plt.text(start_date, 9*(max(temperature5)-min(temperature5))/13 + min(temperature5), u"EcTyp temp = %f"%(ecartType(temperature5)), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(326)
    plt.plot(sent_at6, temperature6, label='tem 6')
    plt.text(start_date, max(temperature6), u"min temp = %f"%(min(temperature6)), fontsize=7)
    plt.text(start_date, 12*(max(temperature6)-min(temperature6))/13 + min(temperature6), u"max temp = %f"%(max(temperature6)), fontsize=7)
    plt.text(start_date, 11*(max(temperature6)-min(temperature6))/13 + min(temperature6), u"moy temp = %f"%(moyenne(temperature6)), fontsize=7)
    plt.text(start_date, 10*(max(temperature6)-min(temperature6))/13 + min(temperature6), u"med temp = %f"%(mediane(temperature6)), fontsize=7)
    plt.text(start_date, 9*(max(temperature6)-min(temperature6))/13 + min(temperature6), u"EcTyp temp = %f"%(ecartType(temperature6)), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.show()
elif variable1 == 'bruit' or variable1 == 'Bruit':
    plt.subplot(321)
    plt.plot(sent_at1, noise1, label='bruit 1')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(322)
    plt.plot(sent_at2, noise2, label='bruit 2')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(323)
    plt.plot(sent_at3, noise3, label='bruit 3')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(324)
    plt.plot(sent_at4, noise4, label='bruit 4')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(325)
    plt.plot(sent_at5, noise5, label='bruit 5')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(326)
    plt.plot(sent_at6, noise6, label='bruit 6')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.show()
elif variable1 == 'Humidité' or variable1 == 'humidité' or variable1 == 'Humidite' or variable1 == 'humidite' :
    plt.subplot(321)
    plt.plot(sent_at1, humidity1, label='hum 1')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(322)
    plt.plot(sent_at2, humidity2, label='hum 2')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(323)
    plt.plot(sent_at3, humidity3, label='hum 3')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(324)
    plt.plot(sent_at4, humidity4, label='hum 4')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(325)
    plt.plot(sent_at5, humidity5, label='hum 5')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(326)
    plt.plot(sent_at6, humidity6, label='hum 6')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.show()
elif variable1 == 'Lumière' or variable1 == 'lumière' or variable1 == 'Lumiere' or variable1 == 'lumiere' :
    plt.subplot(321)
    plt.plot(sent_at1, lum1, label='lum 1')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(322)
    plt.plot(sent_at2, lum2, label='lum 2')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(323)
    plt.plot(sent_at3, lum3, label='lum 3')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(324)
    plt.plot(sent_at4, lum4, label='lum 4')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(325)
    plt.plot(sent_at5, lum5, label='lum 5')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(326)
    plt.plot(sent_at6, lum6, label='lum 6')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.show()
elif variable1 == 'CO2' or variable1 == 'Co2' or variable1 == 'co2':
    plt.subplot(321)
    plt.plot(sent_at1, co21, label='CO2 1')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(322)
    plt.plot(sent_at2, co22, label='CO2 2')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(323)
    plt.plot(sent_at3, co23, label='CO2 3')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(324)
    plt.plot(sent_at4, co24, label='CO2 4')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(325)
    plt.plot(sent_at5, co25, label='CO2 5')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(326)
    plt.plot(sent_at6, co26, label='CO2 6')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.show()
elif variable1 == 'humidex' or variable1 == 'Humidex':
    plt.subplot(321)
    plt.plot(sent_at1, humidex1, label='Humidex 1')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(322)
    plt.plot(sent_at2, humidex2, label='Humidex 2')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(323)
    plt.plot(sent_at3, humidex3, label='Humidex 3')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(324)
    plt.plot(sent_at4, humidex4, label='Humidex 4')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(325)
    plt.plot(sent_at5, humdiex5, label='Humidex 5')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(326)
    plt.plot(sent_at6, humidex6, label='Humidex 6')
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.show()
else :
    print ("erreur d'entrée de variable1")


if variable2 != None :
    if variable2 == 'Temperature' or variable2 == 'temperature' or variable2 == 'Température' or variable2 == 'température':
        plt.subplot(321)
        plt.plot(sent_at1, temperature1, label='tem 1')
        plt.text(end_date, max(temperature1), u"min temp = %f"%(min(temperature1)), fontsize=7)
        plt.text(end_date, 7*(max(temperature1)-min(temperature1))/13 + min(temperature1), u"max temp = %f"%(max(temperature1)), fontsize=7)
        plt.text(end_date, 6*(max(temperature1)-min(temperature1))/13 + min(temperature1), u"moy temp = %f"%(moyenne(temperature1)), fontsize=7)
        plt.text(end_date, 5*(max(temperature1)-min(temperature1))/13 + min(temperature1), u"med temp = %f"%(mediane(temperature1)), fontsize=7)
        plt.text(end_date, 4*(max(temperature1)-min(temperature1))/13 + min(temperature1), u"EcTyp temp = %f"%(ecartType(temperature1)), fontsize=7)
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(322)
        plt.plot(sent_at2, temperature2, label='tem 2')
        plt.text(end_date, max(temperature2), u"min temp = %f"%(min(temperature2)), fontsize=7)
        plt.text(end_date, 7*(max(temperature2)-min(temperature2))/13 + min(temperature2), u"max temp = %f"%(max(temperature2)), fontsize=7)
        plt.text(end_date, 6*(max(temperature2)-min(temperature2))/13 + min(temperature2), u"moy temp = %f"%(moyenne(temperature2)), fontsize=7)
        plt.text(end_date, 5*(max(temperature2)-min(temperature2))/13 + min(temperature2), u"med temp = %f"%(mediane(temperature2)), fontsize=7)
        plt.text(end_date, 4*(max(temperature2)-min(temperature2))/13 + min(temperature2), u"EcTyp temp = %f"%(ecartType(temperature2)), fontsize=7)
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(323)
        plt.plot(sent_at3, temperature3, label='tem 3')
        plt.text(end_date, max(temperature3), u"min temp = %f"%(min(temperature3)), fontsize=7)
        plt.text(end_date, 7*(max(temperature3)-min(temperature3))/13 + min(temperature3), u"max temp = %f"%(max(temperature3)), fontsize=7)
        plt.text(end_date, 6*(max(temperature3)-min(temperature3))/13 + min(temperature3), u"moy temp = %f"%(moyenne(temperature3)), fontsize=7)
        plt.text(end_date, 5*(max(temperature3)-min(temperature3))/13 + min(temperature3), u"med temp = %f"%(mediane(temperature3)), fontsize=7)
        plt.text(end_date, 4*(max(temperature3)-min(temperature3))/13 + min(temperature3), u"EcTyp temp = %f"%(ecartType(temperature3)), fontsize=7)
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(324)
        plt.plot(sent_at4, temperature4, label='tem 4')
        plt.text(end_date, max(temperature4), u"min temp = %f"%(min(temperature4)), fontsize=7)
        plt.text(end_date, 7*(max(temperature4)-min(temperature4))/13 + min(temperature4), u"max temp = %f"%(max(temperature4)), fontsize=7)
        plt.text(end_date, 6*(max(temperature4)-min(temperature4))/13 + min(temperature4), u"moy temp = %f"%(moyenne(temperature4)), fontsize=7)
        plt.text(end_date, 5*(max(temperature4)-min(temperature4))/13 + min(temperature4), u"med temp = %f"%(mediane(temperature4)), fontsize=7)
        plt.text(end_date, 4*(max(temperature4)-min(temperature4))/13 + min(temperature4), u"EcTyp temp = %f"%(ecartType(temperature4)), fontsize=7)
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(325)
        plt.plot(sent_at5, temperature5, label='tem 5')
        plt.text(end_date, max(temperature5), u"min temp = %f"%(min(temperature5)), fontsize=7)
        plt.text(end_date, 7*(max(temperature5)-min(temperature5))/13 + min(temperature5), u"max temp = %f"%(max(temperature5)), fontsize=7)
        plt.text(end_date, 6*(max(temperature5)-min(temperature5))/13 + min(temperature5), u"moy temp = %f"%(moyenne(temperature5)), fontsize=7)
        plt.text(end_date, 5*(max(temperature5)-min(temperature5))/13 + min(temperature5), u"med temp = %f"%(mediane(temperature5)), fontsize=7)
        plt.text(end_date, 4*(max(temperature5)-min(temperature5))/13 + min(temperature5), u"EcTyp temp = %f"%(ecartType(temperature5)), fontsize=7)
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(326)
        plt.plot(sent_at6, temperature6, label='tem 6')
        plt.text(end_date, max(temperature6), u"min temp = %f"%(min(temperature6)), fontsize=7)
        plt.text(end_date, 7*(max(temperature6)-min(temperature6))/13 + min(temperature6), u"max temp = %f"%(max(temperature6)), fontsize=7)
        plt.text(end_date, 6*(max(temperature6)-min(temperature6))/13 + min(temperature6), u"moy temp = %f"%(moyenne(temperature6)), fontsize=7)
        plt.text(end_date, 5*(max(temperature6)-min(temperature6))/13 + min(temperature6), u"med temp = %f"%(mediane(temperature6)), fontsize=7)
        plt.text(end_date, 4*(max(temperature6)-min(temperature6))/13 + min(temperature6), u"EcTyp temp = %f"%(ecartType(temperature6)), fontsize=7)
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.show()
    elif variable2 == 'bruit' or variable2 == 'Bruit':
        plt.subplot(321)
        plt.plot(sent_at1, noise1, label='bruit 1')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(322)
        plt.plot(sent_at2, noise2, label='bruit 2')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(323)
        plt.plot(sent_at3, noise3, label='bruit 3')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(324)
        plt.plot(sent_at4, noise4, label='bruit 4')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(325)
        plt.plot(sent_at5, noise5, label='bruit 5')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(326)
        plt.plot(sent_at6, noise6, label='bruit 6')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.show()
    elif variable2 == 'Humidité' or variable2 == 'humidité' or variable2 == 'Humidite' or variable2 == 'humidite' :
        plt.subplot(321)
        plt.plot(sent_at1, humidity1, label='hum 1')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(322)
        plt.plot(sent_at2, humidity2, label='hum 2')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(323)
        plt.plot(sent_at3, humidity3, label='hum 3')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(324)
        plt.plot(sent_at4, humidity4, label='hum 4')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(325)
        plt.plot(sent_at5, humidity5, label='hum 5')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(326)
        plt.plot(sent_at6, humidity6, label='hum 6')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.show()
    elif variable2 == 'Lumière' or variable2 == 'lumière' or variable2 == 'Lumiere' or variable2 == 'lumiere' :
        plt.subplot(321)
        plt.plot(sent_at1, lum1, label='lum 1')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(322)
        plt.plot(sent_at2, lum2, label='lum 2')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(323)
        plt.plot(sent_at3, lum3, label='lum 3')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(324)
        plt.plot(sent_at4, lum4, label='lum 4')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(325)
        plt.plot(sent_at5, lum5, label='lum 5')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(326)
        plt.plot(sent_at6, lum6, label='lum 6')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.show()
    elif variable2 == 'CO2' or variable2 == 'Co2' or variable2 == 'co2':
        plt.subplot(321)
        plt.plot(sent_at1, co21, label='CO2 1')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(322)
        plt.plot(sent_at2, co22, label='CO2 2')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(323)
        plt.plot(sent_at3, co23, label='CO2 3')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(324)
        plt.plot(sent_at4, co24, label='CO2 4')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(325)
        plt.plot(sent_at5, co25, label='CO2 5')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(326)
        plt.plot(sent_at6, co26, label='CO2 6')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.show()
    elif variable2 == 'humidex' or variable2 == 'Humidex':
        plt.subplot(321)
        plt.plot(sent_at1, humidex1, label='Hmidex 1')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(322)
        plt.plot(sent_at2, humidex2, label='Humidex 2')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(323)
        plt.plot(sent_at3, humidex3, label='Humidex 3')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(324)
        plt.plot(sent_at4, humidex4, label='Humidex 4')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(325)
        plt.plot(sent_at5, humdiex5, label='Humidex 5')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(326)
        plt.plot(sent_at6, humidex6, label='Humidex 6')
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.show()
    else :
        print ("erreur d'entrée de variable2")
