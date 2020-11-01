##importation
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import statistics
from math import *
doc = pd.read_csv(r"C:\Users\squin\OneDrive\Documents\GitHub\projet_algo\EIVP_KM.csv", sep = ";", header = None)

##fonctions valeurs statistique

def min(liste):
    if len(liste)==1 or len(liste)==0:
        return None
    a = liste[0]
    for i in range (1,len(liste)):
        if a>liste[i]:
            a = liste[i]
    return a

def max(liste):
    if len(liste)==1 or len(liste)==0:
        return None
    a = liste[0]
    for i in range (1,len(liste)):
        if a<liste[i]:
            a = liste[i]
    return a

def moyenne(liste):
    if len(liste)==1 or len(liste)==0:
        return 0
    a = 0
    for i in range (len(liste)):
        a+=liste[i]
    return a/len(liste)

def ecartType(liste):
    if len(liste)==1 or len(liste)==0:
        return None
    a = 0
    for i in range(len(liste)):
        a+=(liste[i]-moyenne(liste))**2
    return (a/len(liste))**(1/2)

def mediane(liste):
    if len(liste)==1 or len(liste)==0:
        return None
    return statistics.median(liste)

def coefCorr(liste1,liste2):
    if len(liste1)==1 or len(liste2)==1 or len(liste1)==0 or len(liste2)==0:
        return None
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

if variable1 == 'Temperature' or variable1 == 'temperature' or variable1 == 'Température' or variable1 == 'température':
    var11 = temperature1
    var12 = temperature2
    var13 = temperature3
    var14 = temperature4
    var15 = temperature5
    var16 = temperature6
elif variable1 == 'bruit' or variable1 == 'Bruit':
    var11 = noise1
    var12 = noise2
    var13 = noise3
    var14 = noise4
    var15 = noise5
    var16 = noise6
elif variable1 == 'Humidité' or variable1 == 'humidité' or variable1 == 'Humidite' or variable1 == 'humidite' :
    var11 = humidity1
    var12 = humidity2
    var13 = humidity3
    var14 = humidity4
    var15 = humidity5
    var16 = humidity6
elif variable1 == 'Lumière' or variable1 == 'lumière' or variable1 == 'Lumiere' or variable1 == 'lumiere' :
    var11 = lum1
    var12 = lum2
    var13 = lum3
    var14 = lum4
    var15 = lum5
    var16 = lum6
elif variable1 == 'CO2' or variable1 == 'Co2' or variable1 == 'co2':
    var11 = co21
    var12 = co22
    var13 = co23
    var14 = co24
    var15 = co25
    var16 = co26
elif variable1 == 'humidex' or variable1 == 'Humidex':
    var11 = humidex1
    var12 = humidex2
    var13 = humidex3
    var14 = humidex4
    var15 = humidex5
    var16 = humidex6

if variable2 != None :
    if variable2 == 'Temperature' or variable2 == 'temperature' or variable2 == 'Température' or variable2 == 'température':
        var21 = temperature1
        var22 = temperature2
        var23 = temperature3
        var24 = temperature4
        var25 = temperature5
        var26 = temperature6
    elif variable2 == 'bruit' or variable2 == 'Bruit':
        var21 = noise1
        var22 = noise2
        var23 = noise3
        var24 = noise4
        var25 = noise5
        var26 = noise6
    elif variable2 == 'Humidité' or variable2 == 'humidité' or variable2 == 'Humidite' or variable2 == 'humidite' :
        var21 = humidity1
        var22 = humidity2
        var23 = humidity3
        var24 = humidity4
        var25 = humidity5
        var26 = humidity6
    elif variable2 == 'Lumière' or variable2 == 'lumière' or variable2 == 'Lumiere' or variable2 == 'lumiere' :
        var21 = lum1
        var22 = lum2
        var23 = lum3
        var24 = lum4
        var25 = lum5
        var26 = lum6
    elif variable2 == 'CO2' or variable2 == 'Co2' or variable2 == 'co2':
        var21 = co21
        var22 = co22
        var23 = co23
        var24 = co24
        var25 = co25
        var26 = co26
    elif variable2 == 'humidex' or variable2 == 'Humidex':
        var21 = humidex1
        var22 = humidex2
        var23 = humidex3
        var24 = humidex4
        var25 = humidex5
        var26 = humidex6

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
    e1 = -2
else :
    e1 = -1

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
    e2 = -2
else :
    e2 = -1

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
    e3 = -2
else :
    e3 = -1

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
    e4 = -2
else :
    e4 = -1

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
    e5 = -2
else :
    e5 = -1

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
    e6 = -2
else :
    e6 = -1

##tracé de la courbe

plt.clf()
if variable1 == 'Temperature' or variable1 == 'temperature' or variable1 == 'Température' or variable1 == 'température':
    plt.subplot(321)
    plt.plot(sent_at1, temperature1, label='tem 1')
    plt.text(start_date, max(var11), u"min temp = %f"%(min(temperature1[s1:e1+1])), fontsize=7)
    plt.text(start_date, 12*(max(var11)-min(var11))/13 + min(var11), u"max temp = %f"%(max(temperature1[s1:e1+1])), fontsize=7)
    plt.text(start_date, 11*(max(var11)-min(var11))/13 + min(var11), u"moy temp = %f"%(moyenne(temperature1[s1:e1+1])), fontsize=7)
    plt.text(start_date, 10*(max(var11)-min(var11))/13 + min(var11), u"med temp = %f"%(mediane(temperature1[s1:e1+1])), fontsize=7)
    plt.text(start_date, 9*(max(var11)-min(var11))/13 + min(var11), u"EcTyp temp = %f"%(ecartType(temperature1[s1:e1+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(322)
    plt.plot(sent_at2, temperature2, label='tem 2')
    plt.text(start_date, max(var12), u"min temp = %f"%(min(temperature2[s2:e2+1])), fontsize=7)
    plt.text(start_date, 12*(max(var12)-min(var12))/13 + min(var12), u"max temp = %f"%(max(temperature2[s2:e2+1])), fontsize=7)
    plt.text(start_date, 11*(max(var12)-min(var12))/13 + min(var12), u"moy temp = %f"%(moyenne(temperature2[s2:e2+1])), fontsize=7)
    plt.text(start_date, 10*(max(var12)-min(var12))/13 + min(var12), u"med temp = %f"%(mediane(temperature2[s2:e2+1])), fontsize=7)
    plt.text(start_date, 9*(max(var12)-min(var12))/13 + min(var12), u"EcTyp temp = %f"%(ecartType(temperature2[s2:e2+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(323)
    plt.plot(sent_at3, temperature3, label='tem 3')
    plt.text(start_date, max(var13), u"min temp = %f"%(min(temperature3[s3:e3+1])), fontsize=7)
    plt.text(start_date, 12*(max(var13)-min(var13))/13 + min(var13), u"max temp = %f"%(max(temperature3[s3:e3+1])), fontsize=7)
    plt.text(start_date, 11*(max(var13)-min(var13))/13 + min(var13), u"moy temp = %f"%(moyenne(temperature3[s3:e3+1])), fontsize=7)
    plt.text(start_date, 10*(max(var13)-min(var13))/13 + min(var13), u"med temp = %f"%(mediane(temperature3[s3:e3+1])), fontsize=7)
    plt.text(start_date, 9*(max(var13)-min(var13))/13 + min(var13), u"EcTyp temp = %f"%(ecartType(temperature3[s3:e3+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(324)
    plt.plot(sent_at4, temperature4, label='tem 4')
    plt.text(start_date, max(var14), u"min temp = %f"%(min(temperature4[s4:e4+1])), fontsize=7)
    plt.text(start_date, 12*(max(var14)-min(var14))/13 + min(var14), u"max temp = %f"%(max(temperature4[s4:e4+1])), fontsize=7)
    plt.text(start_date, 11*(max(var14)-min(var14))/13 + min(var14), u"moy temp = %f"%(moyenne(temperature4[s4:e4+1])), fontsize=7)
    plt.text(start_date, 10*(max(var14)-min(var14))/13 + min(var14), u"med temp = %f"%(mediane(temperature4[s4:e4+1])), fontsize=7)
    plt.text(start_date, 9*(max(var14)-min(var14))/13 + min(var14), u"EcTyp temp = %f"%(ecartType(temperature4[s4:e4+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(325)
    plt.plot(sent_at5, temperature5, label='tem 5')
    plt.text(start_date, max(var15), u"min temp = %f"%(min(temperature5[s5:e5+1])), fontsize=7)
    plt.text(start_date, 12*(max(var15)-min(var15))/13 + min(var15), u"max temp = %f"%(max(temperature5[s5:e5+1])), fontsize=7)
    plt.text(start_date, 11*(max(var15)-min(var15))/13 + min(var15), u"moy temp = %f"%(moyenne(temperature5[s5:e5+1])), fontsize=7)
    plt.text(start_date, 10*(max(var15)-min(var15))/13 + min(var15), u"med temp = %f"%(mediane(temperature5[s5:e5+1])), fontsize=7)
    plt.text(start_date, 9*(max(var15)-min(var15))/13 + min(var15), u"EcTyp temp = %f"%(ecartType(temperature5[s5:e5+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.legend()
    plt.subplot(326)
    plt.plot(sent_at6, temperature6, label='tem 6')
    plt.text(start_date, max(var16), u"min temp = %f"%(min(temperature6[s6:e6+1])), fontsize=7)
    plt.text(start_date, 12*(max(var16)-min(var16))/13 + min(var16), u"max temp = %f"%(max(temperature6[s6:e6+1])), fontsize=7)
    plt.text(start_date, 11*(max(var16)-min(var16))/13 + min(var16), u"moy temp = %f"%(moyenne(temperature6[s6:e6+1])), fontsize=7)
    plt.text(start_date, 10*(max(var16)-min(var16))/13 + min(var16), u"med temp = %f"%(mediane(temperature6[s6:e6+1])), fontsize=7)
    plt.text(start_date, 9*(max(var16)-min(var16))/13 + min(var16), u"EcTyp temp = %f"%(ecartType(temperature6[s6:e6+1])), fontsize=7)
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
        plt.text(start_date, 7*(max(var11)-min(var11))/13 + min(var11), u"min temp = %f"%(min(temperature1[s1:e1+1])), fontsize=7)
        plt.text(start_date, 6*(max(var11)-min(var11))/13 + min(var11), u"max temp = %f"%(max(temperature1[s1:e1+1])), fontsize=7)
        plt.text(start_date, 5*(max(var11)-min(var11))/13 + min(var11), u"moy temp = %f"%(moyenne(temperature1[s1:e1+1])), fontsize=7)
        plt.text(start_date, 4*(max(var11)-min(var11))/13 + min(var11), u"med temp = %f"%(mediane(temperature1[s1:e1+1])), fontsize=7)
        plt.text(start_date, 3*(max(var11)-min(var11))/13 + min(var11), u"EcTyp temp = %f"%(ecartType(temperature1[s1:e1+1])), fontsize=7)
        plt.text(start_date, (max(var11)-min(var11))/13 + min(var11), u"coef corr = %f"%coefCorr(var11[s1:e1+1],var21[s1:e1+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(322)
        plt.plot(sent_at2, temperature2, label='tem 2')
        plt.text(start_date, 7*(max(var12)-min(var12))/13 + min(var12), u"min temp = %f"%(min(temperature2[s2:e2+1])), fontsize=7)
        plt.text(start_date, 6*(max(var12)-min(var12))/13 + min(var12), u"max temp = %f"%(max(temperature2[s2:e2+1])), fontsize=7)
        plt.text(start_date, 5*(max(var12)-min(var12))/13 + min(var12), u"moy temp = %f"%(moyenne(temperature2[s2:e2+1])), fontsize=7)
        plt.text(start_date, 4*(max(var12)-min(var12))/13 + min(var12), u"med temp = %f"%(mediane(temperature2[s2:e2+1])), fontsize=7)
        plt.text(start_date, 3*(max(var12)-min(var12))/13 + min(var12), u"EcTyp temp = %f"%(ecartType(temperature2[s2:e2+1])), fontsize=7)
        plt.text(start_date, (max(var11)-min(var11))/13 + min(var11), u"coef corr = %f"%coefCorr(var12[s2:e2+1],var22[s2:e2+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(323)
        plt.plot(sent_at3, temperature3, label='tem 3')
        plt.text(start_date, 7*(max(var13)-min(var13))/13 + min(var13), u"min temp = %f"%(min(temperature3[s3:e3+1])), fontsize=7)
        plt.text(start_date, 6*(max(var13)-min(var13))/13 + min(var13), u"max temp = %f"%(max(temperature3[s3:e3+1])), fontsize=7)
        plt.text(start_date, 5*(max(var13)-min(var13))/13 + min(var13), u"moy temp = %f"%(moyenne(temperature3[s3:e3+1])), fontsize=7)
        plt.text(start_date, 4*(max(var13)-min(var13))/13 + min(var13), u"med temp = %f"%(mediane(temperature3[s3:e3+1])), fontsize=7)
        plt.text(start_date, 3*(max(var13)-min(var13))/13 + min(var13), u"EcTyp temp = %f"%(ecartType(temperature3[s3:e3+1])), fontsize=7)
        plt.text(start_date, (max(var11)-min(var11))/13 + min(var11), u"coef corr = %f"%coefCorr(var13[s3:e3+1],var23[s3:e3+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(324)
        plt.plot(sent_at4, temperature4, label='tem 4')
        plt.text(start_date, 7*(max(var14)-min(var14))/13 + min(var14), u"min temp = %f"%(min(temperature4[s4:e4+1])), fontsize=7)
        plt.text(start_date, 6*(max(var14)-min(var14))/13 + min(var14), u"max temp = %f"%(max(temperature4[s4:e4+1])), fontsize=7)
        plt.text(start_date, 5*(max(var14)-min(var14))/13 + min(var14), u"moy temp = %f"%(moyenne(temperature4[s4:e4+1])), fontsize=7)
        plt.text(start_date, 4*(max(var14)-min(var14))/13 + min(var14), u"med temp = %f"%(mediane(temperature4[s4:e4+1])), fontsize=7)
        plt.text(start_date, 3*(max(var14)-min(var14))/13 + min(var14), u"EcTyp temp = %f"%(ecartType(temperature4[s4:e4+1])), fontsize=7)
        plt.text(start_date, (max(var11)-min(var11))/13 + min(var11), u"coef corr = %f"%coefCorr(var14[s4:e4+1],var24[s4:e4+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(325)
        plt.plot(sent_at5, temperature5, label='tem 5')
        plt.text(start_date, 7*(max(var15)-min(var15))/13 + min(var15), u"min temp = %f"%(min(temperature5[s5:e5+1])), fontsize=7)
        plt.text(start_date, 6*(max(var15)-min(var15))/13 + min(var15), u"max temp = %f"%(max(temperature5[s5:e5+1])), fontsize=7)
        plt.text(start_date, 5*(max(var15)-min(var15))/13 + min(var15), u"moy temp = %f"%(moyenne(temperature5[s5:e5+1])), fontsize=7)
        plt.text(start_date, 4*(max(var15)-min(var15))/13 + min(var15), u"med temp = %f"%(mediane(temperature5[s5:e5+1])), fontsize=7)
        plt.text(start_date, 3*(max(var15)-min(var15))/13 + min(var15), u"EcTyp temp = %f"%(ecartType(temperature5[s5:e5+1])), fontsize=7)
        plt.text(start_date, (max(var11)-min(var11))/13 + min(var11), u"coef corr = %f"%coefCorr(var15[s5:e5+1],var25[s5:e5+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        plt.legend()
        plt.subplot(326)
        plt.plot(sent_at6, temperature6, label='tem 6')
        plt.text(start_date, 7*(max(var16)-min(var16))/13 + min(var16), u"min temp = %f"%(min(temperature6[s6:e6+1])), fontsize=7)
        plt.text(start_date, 6*(max(var16)-min(var16))/13 + min(var16), u"max temp = %f"%(max(temperature6[s6:e6+1])), fontsize=7)
        plt.text(start_date, 5*(max(var16)-min(var16))/13 + min(var16), u"moy temp = %f"%(moyenne(temperature6[s6:e6+1])), fontsize=7)
        plt.text(start_date, 4*(max(var16)-min(var16))/13 + min(var16), u"med temp = %f"%(mediane(temperature6[s6:e6+1])), fontsize=7)
        plt.text(start_date, 3*(max(var16)-min(var16))/13 + min(var16), u"EcTyp temp = %f"%(ecartType(temperature6[s6:e6+1])), fontsize=7)
        plt.text(start_date, (max(var11)-min(var11))/13 + min(var11), u"coef corr = %f"%coefCorr(var16[s6:e6+1],var26[s6:e6+1]), fontsize=7)
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
