##importation

import pandas as pd
import datetime
import matplotlib.pyplot as plt
import statistics
from math import *
doc = pd.read_csv(r"C:\Users\aachi\Desktop\projet_algo\post-32566-EIVP_KM.csv", sep = ";", header = None)

##fonctions valeurs statistique

def min(liste):
    if len(liste)==1 or len(liste)==0:
        return 0
    a = liste[0]
    for i in range (1,len(liste)):
        if a>liste[i]:
            a = liste[i]
    return a

def max(liste):
    if len(liste)==1 or len(liste)==0:
        return 0
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
        return 0
    a = 0
    for i in range(len(liste)):
        a+=(liste[i]-moyenne(liste))**2
    return (a/len(liste))**(1/2)

def tri(liste):
    n=len(liste)
    for i in range(1,n):
        temp=liste[i]
        j=i-1
        while j >= 0 and liste[j] > temp:
            liste[j+1]=liste[j]
            j-=1
        liste[j+1]=temp
    return liste

def mediane(liste):
    n=len(liste)
    l=tri(liste)
    if len(liste)==1 or len(liste)==0:
        return 0
    else:
        if n%2!=0:
            med=l[n//2]
        else:
            med=(l[n//2]+l[(n//2)-1])/2
    return med

def cov(liste1,liste2):
    if len(liste1)==1 or len(liste2)==1 or len(liste1)==0 or len(liste2)==0:
        return 0
    else:
        n=len(liste1)
        cov=0
        x=0
        y=0
    for i in range(n):
        cov=cov+(liste1[i]*liste2[i])
        x=x+liste1[i]
        y=y+liste2[i]
    c=cov/n-((x/n)*(y/n))
    return c

def coefCorr(liste1,liste2):
    cc=cov(liste1,liste2)/(ecartType(liste1)*ecartType(liste2))
    if len(liste1)==1 or len(liste2)==1 or len(liste1)==0 or len(liste2)==0:
        return O
    else:
        return cc

def anom(liste):    #liste de datetime
    l = []
    for i in range(len(liste)-1):
        if liste[i+1] - liste[i] > datetime.timedelta(seconds=3600):
            l.append(i)
    return l


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
    if int(doc[1][i])==1:
        noise1.append(float(doc[2][i]))
        temperature1.append(float(doc[3][i]))
        humidity1.append(float(doc[4][i]))
        lum1.append(float(doc[5][i]))
        co21.append(float(doc[6][i]))
        humidex1.append(humidex(float(doc[3][i]),float(doc[4][i])))
        sent_at1.append(datetime.datetime(int(doc[7][i][0:4]),int(doc[7][i][5:7]),int(doc[7][i][8:10]),int(doc[7][i][11:13]),int(doc[7][i][14:16]),int(doc[7][i][17:19])))
    elif int(doc[1][i])==2:
        noise2.append(float(doc[2][i]))
        temperature2.append(float(doc[3][i]))
        humidity2.append(float(doc[4][i]))
        lum2.append(float(doc[5][i]))
        co22.append(float(doc[6][i]))
        humidex2.append(humidex(float(doc[3][i]),float(doc[4][i])))
        sent_at2.append(datetime.datetime(int(doc[7][i][0:4]),int(doc[7][i][5:7]),int(doc[7][i][8:10]),int(doc[7][i][11:13]),int(doc[7][i][14:16]),int(doc[7][i][17:19])))
    elif int(doc[1][i])==3:
        noise3.append(float(doc[2][i]))
        temperature3.append(float((doc[3][i])))
        humidity3.append(float(doc[4][i]))
        lum3.append(float(doc[5][i]))
        co23.append(float(doc[6][i]))
        humidex3.append(humidex(float(doc[3][i]),float(doc[4][i])))
        sent_at3.append(datetime.datetime(int(doc[7][i][0:4]),int(doc[7][i][5:7]),int(doc[7][i][8:10]),int(doc[7][i][11:13]),int(doc[7][i][14:16]),int(doc[7][i][17:19])))
    elif int(doc[1][i])==4:
        noise4.append(float(doc[2][i]))
        temperature4.append(float(doc[3][i]))
        humidity4.append(float(doc[4][i]))
        lum4.append(float(doc[5][i]))
        co24.append(float(doc[6][i]))
        humidex4.append(humidex(float(doc[3][i]),float(doc[4][i])))
        sent_at4.append(datetime.datetime(int(doc[7][i][0:4]),int(doc[7][i][5:7]),int(doc[7][i][8:10]),int(doc[7][i][11:13]),int(doc[7][i][14:16]),int(doc[7][i][17:19])))
    elif int(doc[1][i])==5:
        noise5.append(float(doc[2][i]))
        temperature5.append(float((doc[3][i])))
        humidity5.append(float(doc[4][i]))
        lum5.append(float(doc[5][i]))
        co25.append(float(doc[6][i]))
        humidex5.append(humidex(float(doc[3][i]),float(doc[4][i])))
        sent_at5.append(datetime.datetime(int(doc[7][i][0:4]),int(doc[7][i][5:7]),int(doc[7][i][8:10]),int(doc[7][i][11:13]),int(doc[7][i][14:16]),int(doc[7][i][17:19])))
    elif int(doc[1][i])==6:
        noise6.append(float(doc[2][i]))
        temperature6.append(float(doc[3][i]))
        humidity6.append(float(doc[4][i]))
        lum6.append(float(doc[5][i]))
        co26.append(float(doc[6][i]))
        humidex6.append(humidex(float(doc[3][i]),float(doc[4][i])))
        sent_at6.append(datetime.datetime(int(doc[7][i][0:4]),int(doc[7][i][5:7]),int(doc[7][i][8:10]),int(doc[7][i][11:13]),int(doc[7][i][14:16]),int(doc[7][i][17:19])))


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
#ax_var_capt
plt.clf()
if variable2 == None :
    plt.suptitle(variable1, fontsize = 32)
else :
    plt.suptitle(u"%s (violet) et %s (vert)"%(variable1,variable2), fontsize = 32)
if variable1 == 'Temperature' or variable1 == 'temperature' or variable1 == 'Température' or variable1 == 'température':
    ax11 = plt.subplot(321)
    plt.subplot(321)
    ax11.plot(sent_at1, temperature1, label='tem 1', color = 'tab:purple')
    ax11.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at1)) != 0 :
        ax11.plot(sent_at1[anom(sent_at1)[0]:anom(sent_at1)[-1]+2], temperature1[anom(sent_at1)[0]:anom(sent_at1)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var11), u"min temp = %f"%(min(temperature1[s1:e1+1])), fontsize=7)
    plt.text(start_date, 12*(max(var11)-min(var11))/13 + min(var11), u"max temp = %f"%(max(temperature1[s1:e1+1])), fontsize=7)
    plt.text(start_date, 11*(max(var11)-min(var11))/13 + min(var11), u"moy temp = %f"%(moyenne(temperature1[s1:e1+1])), fontsize=7)
    plt.text(start_date, 10*(max(var11)-min(var11))/13 + min(var11), u"med temp = %f"%(mediane(temperature1[s1:e1+1])), fontsize=7)
    plt.text(start_date, 9*(max(var11)-min(var11))/13 + min(var11), u"EcTyp temp = %f"%(ecartType(temperature1[s1:e1+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 1')
    ax12 = plt.subplot(322)
    plt.subplot(322)
    ax12.plot(sent_at2, temperature2, label='tem 2', color = 'tab:purple')
    ax12.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at2)) != 0 :
        ax12.plot(sent_at2[anom(sent_at2)[0]:anom(sent_at2)[-1]+2], temperature2[anom(sent_at2)[0]:anom(sent_at2)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var12), u"min temp = %f"%(min(temperature2[s2:e2+1])), fontsize=7)
    plt.text(start_date, 12*(max(var12)-min(var12))/13 + min(var12), u"max temp = %f"%(max(temperature2[s2:e2+1])), fontsize=7)
    plt.text(start_date, 11*(max(var12)-min(var12))/13 + min(var12), u"moy temp = %f"%(moyenne(temperature2[s2:e2+1])), fontsize=7)
    plt.text(start_date, 10*(max(var12)-min(var12))/13 + min(var12), u"med temp = %f"%(mediane(temperature2[s2:e2+1])), fontsize=7)
    plt.text(start_date, 9*(max(var12)-min(var12))/13 + min(var12), u"EcTyp temp = %f"%(ecartType(temperature2[s2:e2+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 2')
    ax13 = plt.subplot(323)
    plt.subplot(323)
    ax13.plot(sent_at3, temperature3, label='tem 3', color = 'tab:purple')
    ax13.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at3)) != 0 :
        ax13.plot(sent_at3[anom(sent_at3)[0]:anom(sent_at3)[-1]+2], temperature3[anom(sent_at3)[0]:anom(sent_at3)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var13), u"min temp = %f"%(min(temperature3[s3:e3+1])), fontsize=7)
    plt.text(start_date, 12*(max(var13)-min(var13))/13 + min(var13), u"max temp = %f"%(max(temperature3[s3:e3+1])), fontsize=7)
    plt.text(start_date, 11*(max(var13)-min(var13))/13 + min(var13), u"moy temp = %f"%(moyenne(temperature3[s3:e3+1])), fontsize=7)
    plt.text(start_date, 10*(max(var13)-min(var13))/13 + min(var13), u"med temp = %f"%(mediane(temperature3[s3:e3+1])), fontsize=7)
    plt.text(start_date, 9*(max(var13)-min(var13))/13 + min(var13), u"EcTyp temp = %f"%(ecartType(temperature3[s3:e3+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 3')
    ax14 = plt.subplot(324)
    plt.subplot(324)
    ax14.plot(sent_at4, temperature4, label='tem 4', color = 'tab:purple')
    ax14.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at4)) != 0 :
        ax14.plot(sent_at4[anom(sent_at4)[0]:anom(sent_at4)[-1]+2], temperature4[anom(sent_at4)[0]:anom(sent_at4)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var14), u"min temp = %f"%(min(temperature4[s4:e4+1])), fontsize=7)
    plt.text(start_date, 12*(max(var14)-min(var14))/13 + min(var14), u"max temp = %f"%(max(temperature4[s4:e4+1])), fontsize=7)
    plt.text(start_date, 11*(max(var14)-min(var14))/13 + min(var14), u"moy temp = %f"%(moyenne(temperature4[s4:e4+1])), fontsize=7)
    plt.text(start_date, 10*(max(var14)-min(var14))/13 + min(var14), u"med temp = %f"%(mediane(temperature4[s4:e4+1])), fontsize=7)
    plt.text(start_date, 9*(max(var14)-min(var14))/13 + min(var14), u"EcTyp temp = %f"%(ecartType(temperature4[s4:e4+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 4')
    ax15 = plt.subplot(325)
    plt.subplot(325)
    ax15.plot(sent_at5, temperature5, label='tem 5', color = 'tab:purple')
    ax15.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at5)) != 0 :
        ax15.plot(sent_at5[anom(sent_at5)[0]:anom(sent_at5)[-1]+2], temperature5[anom(sent_at5)[0]:anom(sent_at5)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var15), u"min temp = %f"%(min(temperature5[s5:e5+1])), fontsize=7)
    plt.text(start_date, 12*(max(var15)-min(var15))/13 + min(var15), u"max temp = %f"%(max(temperature5[s5:e5+1])), fontsize=7)
    plt.text(start_date, 11*(max(var15)-min(var15))/13 + min(var15), u"moy temp = %f"%(moyenne(temperature5[s5:e5+1])), fontsize=7)
    plt.text(start_date, 10*(max(var15)-min(var15))/13 + min(var15), u"med temp = %f"%(mediane(temperature5[s5:e5+1])), fontsize=7)
    plt.text(start_date, 9*(max(var15)-min(var15))/13 + min(var15), u"EcTyp temp = %f"%(ecartType(temperature5[s5:e5+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 5')
    ax16 = plt.subplot(326)
    plt.subplot(326)
    ax16.plot(sent_at6, temperature6, label='tem 6', color = 'tab:purple')
    ax16.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at6)) != 0 :
        ax16.plot(sent_at6[anom(sent_at6)[0]:anom(sent_at6)[-1]+2], temperature6[anom(sent_at6)[0]:anom(sent_at6)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var16), u"min temp = %f"%(min(temperature6[s6:e6+1])), fontsize=7)
    plt.text(start_date, 12*(max(var16)-min(var16))/13 + min(var16), u"max temp = %f"%(max(temperature6[s6:e6+1])), fontsize=7)
    plt.text(start_date, 11*(max(var16)-min(var16))/13 + min(var16), u"moy temp = %f"%(moyenne(temperature6[s6:e6+1])), fontsize=7)
    plt.text(start_date, 10*(max(var16)-min(var16))/13 + min(var16), u"med temp = %f"%(mediane(temperature6[s6:e6+1])), fontsize=7)
    plt.text(start_date, 9*(max(var16)-min(var16))/13 + min(var16), u"EcTyp temp = %f"%(ecartType(temperature6[s6:e6+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 6')
elif variable1 == 'bruit' or variable1 == 'Bruit':
    ax11 = plt.subplot(321)
    plt.subplot(321)
    ax11.plot(sent_at1, noise1, label='bruit 1', color = 'tab:purple')
    ax11.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at1)) != 0 :
        ax11.plot(sent_at1[anom(sent_at1)[0]:anom(sent_at1)[-1]+2], noise1[anom(sent_at1)[0]:anom(sent_at1)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var11), u"min bruit = %f"%(min(noise1[s1:e1+1])), fontsize=7)
    plt.text(start_date, 12*(max(var11)-min(var11))/13 + min(var11), u"max bruit = %f"%(max(noise1[s1:e1+1])), fontsize=7)
    plt.text(start_date, 11*(max(var11)-min(var11))/13 + min(var11), u"moy bruit = %f"%(moyenne(noise1[s1:e1+1])), fontsize=7)
    plt.text(start_date, 10*(max(var11)-min(var11))/13 + min(var11), u"med bruit = %f"%(mediane(noise1[s1:e1+1])), fontsize=7)
    plt.text(start_date, 9*(max(var11)-min(var11))/13 + min(var11), u"EcTyp bruit = %f"%(ecartType(noise1[s1:e1+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 1')
    ax12 = plt.subplot(322)
    plt.subplot(322)
    ax12.plot(sent_at2, noise2, label='bruit 2', color = 'tab:purple')
    ax12.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at2)) != 0 :
        ax12.plot(sent_at2[anom(sent_at2)[0]:anom(sent_at2)[-1]+2], noise2[anom(sent_at2)[0]:anom(sent_at2)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var12), u"min bruit = %f"%(min(noise2[s2:e2+1])), fontsize=7)
    plt.text(start_date, 12*(max(var12)-min(var12))/13 + min(var12), u"max bruit = %f"%(max(noise2[s2:e2+1])), fontsize=7)
    plt.text(start_date, 11*(max(var12)-min(var12))/13 + min(var12), u"moy bruit = %f"%(moyenne(noise2[s2:e2+1])), fontsize=7)
    plt.text(start_date, 10*(max(var12)-min(var12))/13 + min(var12), u"med bruit = %f"%(mediane(noise2[s2:e2+1])), fontsize=7)
    plt.text(start_date, 9*(max(var12)-min(var12))/13 + min(var12), u"EcTyp bruit = %f"%(ecartType(noise2[s2:e2+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 2')
    ax13 = plt.subplot(323)
    plt.subplot(323)
    ax13.plot(sent_at3, noise3, label='bruit 3', color = 'tab:purple')
    ax13.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at3)) != 0 :
        ax13.plot(sent_at3[anom(sent_at3)[0]:anom(sent_at3)[-1]+2], noise3[anom(sent_at3)[0]:anom(sent_at3)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var13), u"min bruit = %f"%(min(noise3[s3:e3+1])), fontsize=7)
    plt.text(start_date, 12*(max(var13)-min(var13))/13 + min(var13), u"max bruit = %f"%(max(noise3[s3:e3+1])), fontsize=7)
    plt.text(start_date, 11*(max(var13)-min(var13))/13 + min(var13), u"moy bruit = %f"%(moyenne(noise3[s3:e3+1])), fontsize=7)
    plt.text(start_date, 10*(max(var13)-min(var13))/13 + min(var13), u"med bruit = %f"%(mediane(noise3[s3:e3+1])), fontsize=7)
    plt.text(start_date, 9*(max(var13)-min(var13))/13 + min(var13), u"EcTyp bruit = %f"%(ecartType(noise3[s3:e3+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 3')
    ax14 = plt.subplot(324)
    plt.subplot(324)
    ax14.plot(sent_at4, noise4, label='bruit 4', color = 'tab:purple')
    ax14.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at4)) != 0 :
        ax14.plot(sent_at4[anom(sent_at4)[0]:anom(sent_at4)[-1]+2], noise1[anom(sent_at4)[0]:anom(sent_at4)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var14), u"min bruit = %f"%(min(noise4[s4:e4+1])), fontsize=7)
    plt.text(start_date, 12*(max(var14)-min(var14))/13 + min(var14), u"max bruit = %f"%(max(noise4[s4:e4+1])), fontsize=7)
    plt.text(start_date, 11*(max(var14)-min(var14))/13 + min(var14), u"moy bruit = %f"%(moyenne(noise4[s4:e4+1])), fontsize=7)
    plt.text(start_date, 10*(max(var14)-min(var14))/13 + min(var14), u"med bruit = %f"%(mediane(noise4[s4:e4+1])), fontsize=7)
    plt.text(start_date, 9*(max(var14)-min(var14))/13 + min(var14), u"EcTyp bruit = %f"%(ecartType(noise4[s4:e4+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 4')
    ax15 = plt.subplot(325)
    plt.subplot(325)
    ax15.plot(sent_at5, noise5, label='bruit 5', color = 'tab:purple')
    ax15.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at5)) != 0 :
        ax15.plot(sent_at5[anom(sent_at5)[0]:anom(sent_at5)[-1]+2], noise5[anom(sent_at5)[0]:anom(sent_at5)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var15), u"min bruit = %f"%(min(noise5[s5:e5+1])), fontsize=7)
    plt.text(start_date, 12*(max(var15)-min(var15))/13 + min(var15), u"max bruit = %f"%(max(noise5[s5:e5+1])), fontsize=7)
    plt.text(start_date, 11*(max(var15)-min(var15))/13 + min(var15), u"moy bruit = %f"%(moyenne(noise5[s5:e5+1])), fontsize=7)
    plt.text(start_date, 10*(max(var15)-min(var15))/13 + min(var15), u"med bruit = %f"%(mediane(noise5[s5:e5+1])), fontsize=7)
    plt.text(start_date, 9*(max(var15)-min(var15))/13 + min(var15), u"EcTyp bruit = %f"%(ecartType(noise5[s5:e5+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 5')
    ax16 = plt.subplot(326)
    plt.subplot(326)
    ax16.plot(sent_at6, noise6, label='bruit 6', color = 'tab:purple')
    ax16.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at6)) != 0 :
        ax16.plot(sent_at6[anom(sent_at6)[0]:anom(sent_at6)[-1]+2], noise6[anom(sent_at6)[0]:anom(sent_at6)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var16), u"min bruit = %f"%(min(noise6[s6:e6+1])), fontsize=7)
    plt.text(start_date, 12*(max(var16)-min(var16))/13 + min(var16), u"max bruit = %f"%(max(noise6[s6:e6+1])), fontsize=7)
    plt.text(start_date, 11*(max(var16)-min(var16))/13 + min(var16), u"moy bruit = %f"%(moyenne(noise6[s6:e6+1])), fontsize=7)
    plt.text(start_date, 10*(max(var16)-min(var16))/13 + min(var16), u"med bruit = %f"%(mediane(noise6[s6:e6+1])), fontsize=7)
    plt.text(start_date, 9*(max(var16)-min(var16))/13 + min(var16), u"EcTyp bruit = %f"%(ecartType(noise6[s6:e6+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 6')
elif variable1 == 'Humidité' or variable1 == 'humidité' or variable1 == 'Humidite' or variable1 == 'humidite' :
    ax11 = plt.subplot(321)
    plt.subplot(321)
    ax11.plot(sent_at1, humidity1, label='hum 1', color = 'tab:purple')
    ax11.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at1)) != 0 :
        ax11.plot(sent_at1[anom(sent_at1)[0]:anom(sent_at1)[-1]+2], humidity1[anom(sent_at1)[0]:anom(sent_at1)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var11), u"min hum = %f"%(min(humidity1[s1:e1+1])), fontsize=7)
    plt.text(start_date, 12*(max(var11)-min(var11))/13 + min(var11), u"max hum = %f"%(max(humidity1[s1:e1+1])), fontsize=7)
    plt.text(start_date, 11*(max(var11)-min(var11))/13 + min(var11), u"moy hum = %f"%(moyenne(humidity1[s1:e1+1])), fontsize=7)
    plt.text(start_date, 10*(max(var11)-min(var11))/13 + min(var11), u"med hum = %f"%(mediane(humidity1[s1:e1+1])), fontsize=7)
    plt.text(start_date, 9*(max(var11)-min(var11))/13 + min(var11), u"EcTyp hum = %f"%(ecartType(humidity1[s1:e1+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 1')
    ax12 = plt.subplot(322)
    plt.subplot(322)
    ax12.plot(sent_at2, humidity2, label='hum 2', color = 'tab:purple')
    ax12.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at2)) != 0 :
        ax12.plot(sent_at2[anom(sent_at2)[0]:anom(sent_at2)[-1]+2], humidity2[anom(sent_at2)[0]:anom(sent_at2)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var12), u"min hum = %f"%(min(humidity2[s2:e2+1])), fontsize=7)
    plt.text(start_date, 12*(max(var12)-min(var12))/13 + min(var12), u"max hum = %f"%(max(humidity2[s2:e2+1])), fontsize=7)
    plt.text(start_date, 11*(max(var12)-min(var12))/13 + min(var12), u"moy hum = %f"%(moyenne(humidity2[s2:e2+1])), fontsize=7)
    plt.text(start_date, 10*(max(var12)-min(var12))/13 + min(var12), u"med hum = %f"%(mediane(humidity2[s2:e2+1])), fontsize=7)
    plt.text(start_date, 9*(max(var12)-min(var12))/13 + min(var12), u"EcTyp hum = %f"%(ecartType(humidity2[s2:e2+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 2')
    ax13 = plt.subplot(323)
    plt.subplot(323)
    ax13.plot(sent_at3, humidity3, label='hum 3', color = 'tab:purple')
    ax13.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at3)) != 0 :
        ax13.plot(sent_at3[anom(sent_at3)[0]:anom(sent_at3)[-1]+2], humidity3[anom(sent_at3)[0]:anom(sent_at3)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var13), u"min hum = %f"%(min(humidity3[s3:e3+1])), fontsize=7)
    plt.text(start_date, 12*(max(var13)-min(var13))/13 + min(var13), u"max hum = %f"%(max(humidity3[s3:e3+1])), fontsize=7)
    plt.text(start_date, 11*(max(var13)-min(var13))/13 + min(var13), u"moy hum = %f"%(moyenne(humidity3[s3:e3+1])), fontsize=7)
    plt.text(start_date, 10*(max(var13)-min(var13))/13 + min(var13), u"med hum = %f"%(mediane(humidity3[s3:e3+1])), fontsize=7)
    plt.text(start_date, 9*(max(var13)-min(var13))/13 + min(var13), u"EcTyp hum = %f"%(ecartType(humidity3[s3:e3+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 3')
    ax14 = plt.subplot(324)
    plt.subplot(324)
    ax14.plot(sent_at4, humidity4, label='hum 4', color = 'tab:purple')
    ax14.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at4)) != 0 :
        ax14.plot(sent_at4[anom(sent_at4)[0]:anom(sent_at4)[-1]+2], humidity4[anom(sent_at4)[0]:anom(sent_at4)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var14), u"min hum = %f"%(min(humidity4[s4:e4+1])), fontsize=7)
    plt.text(start_date, 12*(max(var14)-min(var14))/13 + min(var14), u"max hum = %f"%(max(humidity4[s4:e4+1])), fontsize=7)
    plt.text(start_date, 11*(max(var14)-min(var14))/13 + min(var14), u"moy hum = %f"%(moyenne(humidity4[s4:e4+1])), fontsize=7)
    plt.text(start_date, 10*(max(var14)-min(var14))/13 + min(var14), u"med hum = %f"%(mediane(humidity4[s4:e4+1])), fontsize=7)
    plt.text(start_date, 9*(max(var14)-min(var14))/13 + min(var14), u"EcTyp hum = %f"%(ecartType(humidity4[s4:e4+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 4')
    ax15 = plt.subplot(325)
    plt.subplot(325)
    ax15.plot(sent_at5, humidity5, label='hum 5', color = 'tab:purple')
    ax15.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at5)) != 0 :
        ax15.plot(sent_at5[anom(sent_at5)[0]:anom(sent_at5)[-1]+2], humidity5[anom(sent_at5)[0]:anom(sent_at5)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var15), u"min hum = %f"%(min(humidity5[s5:e5+1])), fontsize=7)
    plt.text(start_date, 12*(max(var15)-min(var15))/13 + min(var15), u"max hum = %f"%(max(humidity5[s5:e5+1])), fontsize=7)
    plt.text(start_date, 11*(max(var15)-min(var15))/13 + min(var15), u"moy hum = %f"%(moyenne(humidity5[s5:e5+1])), fontsize=7)
    plt.text(start_date, 10*(max(var15)-min(var15))/13 + min(var15), u"med hum = %f"%(mediane(humidity5[s5:e5+1])), fontsize=7)
    plt.text(start_date, 9*(max(var15)-min(var15))/13 + min(var15), u"EcTyp hum = %f"%(ecartType(humidity5[s5:e5+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 5')
    ax16 = plt.subplot(326)
    plt.subplot(326)
    ax16.plot(sent_at6, humidity6, label='hum 6', color = 'tab:purple')
    ax16.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at6)) != 0 :
        ax16.plot(sent_at6[anom(sent_at6)[0]:anom(sent_at6)[-1]+2], humidity6[anom(sent_at6)[0]:anom(sent_at6)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var16), u"min hum = %f"%(min(humidity6[s6:e6+1])), fontsize=7)
    plt.text(start_date, 12*(max(var16)-min(var16))/13 + min(var16), u"max hum = %f"%(max(humidity6[s6:e6+1])), fontsize=7)
    plt.text(start_date, 11*(max(var16)-min(var16))/13 + min(var16), u"moy hum = %f"%(moyenne(humidity6[s6:e6+1])), fontsize=7)
    plt.text(start_date, 10*(max(var16)-min(var16))/13 + min(var16), u"med hum = %f"%(mediane(humidity6[s6:e6+1])), fontsize=7)
    plt.text(start_date, 9*(max(var16)-min(var16))/13 + min(var16), u"EcTyp hum = %f"%(ecartType(humidity6[s6:e6+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 6')
elif variable1 == 'Lumière' or variable1 == 'lumière' or variable1 == 'Lumiere' or variable1 == 'lumiere' :
    ax11 = plt.subplot(321)
    plt.subplot(321)
    ax11.plot(sent_at1, lum1, label='lum 1', color = 'tab:purple')
    ax11.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at1)) != 0 :
        ax11.plot(sent_at1[anom(sent_at1)[0]:anom(sent_at1)[-1]+2], lum1[anom(sent_at1)[0]:anom(sent_at1)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var11), u"min lum = %f"%(min(lum1[s1:e1+1])), fontsize=7)
    plt.text(start_date, 12*(max(var11)-min(var11))/13 + min(var11), u"max lum = %f"%(max(lum1[s1:e1+1])), fontsize=7)
    plt.text(start_date, 11*(max(var11)-min(var11))/13 + min(var11), u"moy lum = %f"%(moyenne(lum1[s1:e1+1])), fontsize=7)
    plt.text(start_date, 10*(max(var11)-min(var11))/13 + min(var11), u"med lum = %f"%(mediane(lum1[s1:e1+1])), fontsize=7)
    plt.text(start_date, 9*(max(var11)-min(var11))/13 + min(var11), u"EcTyp lum = %f"%(ecartType(lum1[s1:e1+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 1')
    ax12 = plt.subplot(322)
    plt.subplot(322)
    ax12.plot(sent_at2, lum2, label='lum 2', color = 'tab:purple')
    ax12.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at2)) != 0 :
        ax12.plot(sent_at2[anom(sent_at2)[0]:anom(sent_at2)[-1]+2], lum2[anom(sent_at2)[0]:anom(sent_at2)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var12), u"min lum = %f"%(min(lum2[s2:e2+1])), fontsize=7)
    plt.text(start_date, 12*(max(var12)-min(var12))/13 + min(var12), u"max lum = %f"%(max(lum2[s2:e2+1])), fontsize=7)
    plt.text(start_date, 11*(max(var12)-min(var12))/13 + min(var12), u"moy lum = %f"%(moyenne(lum2[s2:e2+1])), fontsize=7)
    plt.text(start_date, 10*(max(var12)-min(var12))/13 + min(var12), u"med lum = %f"%(mediane(lum2[s2:e2+1])), fontsize=7)
    plt.text(start_date, 9*(max(var12)-min(var12))/13 + min(var12), u"EcTyp lum = %f"%(ecartType(lum2[s2:e2+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 2')
    ax13 = plt.subplot(323)
    plt.subplot(323)
    ax13.plot(sent_at3, lum3, label='lum 3', color = 'tab:purple')
    ax13.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at3)) != 0 :
        ax13.plot(sent_at3[anom(sent_at3)[0]:anom(sent_at3)[-1]+2], lum3[anom(sent_at3)[0]:anom(sent_at3)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var13), u"min lum = %f"%(min(lum3[s3:e3+1])), fontsize=7)
    plt.text(start_date, 12*(max(var13)-min(var13))/13 + min(var13), u"max lum = %f"%(max(lum3[s3:e3+1])), fontsize=7)
    plt.text(start_date, 11*(max(var13)-min(var13))/13 + min(var13), u"moy lum = %f"%(moyenne(lum3[s3:e3+1])), fontsize=7)
    plt.text(start_date, 10*(max(var13)-min(var13))/13 + min(var13), u"med lum = %f"%(mediane(lum3[s3:e3+1])), fontsize=7)
    plt.text(start_date, 9*(max(var13)-min(var13))/13 + min(var13), u"EcTyp lum = %f"%(ecartType(lum3[s3:e3+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 3')
    ax14 = plt.subplot(324)
    plt.subplot(324)
    ax14.plot(sent_at4, lum4, label='lum 4', color = 'tab:purple')
    ax14.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at4)) != 0 :
        ax14.plot(sent_at4[anom(sent_at4)[0]:anom(sent_at4)[-1]+2], lum4[anom(sent_at4)[0]:anom(sent_at4)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var14), u"min lum = %f"%(min(lum4[s4:e4+1])), fontsize=7)
    plt.text(start_date, 12*(max(var14)-min(var14))/13 + min(var14), u"max lum = %f"%(max(lum4[s4:e4+1])), fontsize=7)
    plt.text(start_date, 11*(max(var14)-min(var14))/13 + min(var14), u"moy lum = %f"%(moyenne(lum4[s4:e4+1])), fontsize=7)
    plt.text(start_date, 10*(max(var14)-min(var14))/13 + min(var14), u"med lum = %f"%(mediane(lum4[s4:e4+1])), fontsize=7)
    plt.text(start_date, 9*(max(var14)-min(var14))/13 + min(var14), u"EcTyp lum = %f"%(ecartType(lum4[s4:e4+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 4')
    ax15 = plt.subplot(325)
    plt.subplot(325)
    ax15.plot(sent_at5, lum5, label='lum 5', color = 'tab:purple')
    ax15.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at5)) != 0 :
        ax15.plot(sent_at5[anom(sent_at5)[0]:anom(sent_at5)[-1]+2], lum5[anom(sent_at5)[0]:anom(sent_at5)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var15), u"min lum = %f"%(min(lum5[s5:e5+1])), fontsize=7)
    plt.text(start_date, 12*(max(var15)-min(var15))/13 + min(var15), u"max lum = %f"%(max(lum5[s5:e5+1])), fontsize=7)
    plt.text(start_date, 11*(max(var15)-min(var15))/13 + min(var15), u"moy lum = %f"%(moyenne(lum5[s5:e5+1])), fontsize=7)
    plt.text(start_date, 10*(max(var15)-min(var15))/13 + min(var15), u"med lum = %f"%(mediane(lum5[s5:e5+1])), fontsize=7)
    plt.text(start_date, 9*(max(var15)-min(var15))/13 + min(var15), u"EcTyp lum = %f"%(ecartType(lum5[s5:e5+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 5')
    ax16 = plt.subplot(326)
    plt.subplot(326)
    ax16.plot(sent_at6, lum6, label='lum 6', color = 'tab:purple')
    ax16.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at6)) != 0 :
        ax16.plot(sent_at6[anom(sent_at6)[0]:anom(sent_at6)[-1]+2], lum6[anom(sent_at6)[0]:anom(sent_at6)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var16), u"min lum = %f"%(min(lum6[s6:e6+1])), fontsize=7)
    plt.text(start_date, 12*(max(var16)-min(var16))/13 + min(var16), u"max lum = %f"%(max(lum6[s6:e6+1])), fontsize=7)
    plt.text(start_date, 11*(max(var16)-min(var16))/13 + min(var16), u"moy lum = %f"%(moyenne(lum6[s6:e6+1])), fontsize=7)
    plt.text(start_date, 10*(max(var16)-min(var16))/13 + min(var16), u"med lum = %f"%(mediane(lum6[s6:e6+1])), fontsize=7)
    plt.text(start_date, 9*(max(var16)-min(var16))/13 + min(var16), u"EcTyp lum = %f"%(ecartType(lum6[s6:e6+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 6')
elif variable1 == 'CO2' or variable1 == 'Co2' or variable1 == 'co2':
    ax11 = plt.subplot(321)
    plt.subplot(321)
    ax11.plot(sent_at1, co21, label='CO2 1', color = 'tab:purple')
    ax11.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at1)) != 0 :
        ax11.plot(sent_at1[anom(sent_at1)[0]:anom(sent_at1)[-1]+2], co21[anom(sent_at1)[0]:anom(sent_at1)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var11), u"min co2 = %f"%(min(co21[s1:e1+1])), fontsize=7)
    plt.text(start_date, 12*(max(var11)-min(var11))/13 + min(var11), u"max co2 = %f"%(max(co21[s1:e1+1])), fontsize=7)
    plt.text(start_date, 11*(max(var11)-min(var11))/13 + min(var11), u"moy co2 = %f"%(moyenne(co21[s1:e1+1])), fontsize=7)
    plt.text(start_date, 10*(max(var11)-min(var11))/13 + min(var11), u"med co2 = %f"%(mediane(co21[s1:e1+1])), fontsize=7)
    plt.text(start_date, 9*(max(var11)-min(var11))/13 + min(var11), u"EcTyp co2 = %f"%(ecartType(co21[s1:e1+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 1')
    ax2 = plt.subplot(322)
    plt.subplot(322)
    ax12.plot(sent_at2, co22, label='CO2 2', color = 'tab:purple')
    ax12.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at2)) != 0 :
        ax12.plot(sent_at2[anom(sent_at2)[0]:anom(sent_at2)[-1]+2], co22[anom(sent_at2)[0]:anom(sent_at2)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var12), u"min co2 = %f"%(min(co22[s2:e2+1])), fontsize=7)
    plt.text(start_date, 12*(max(var12)-min(var12))/13 + min(var12), u"max co2 = %f"%(max(co22[s2:e2+1])), fontsize=7)
    plt.text(start_date, 11*(max(var12)-min(var12))/13 + min(var12), u"moy co2 = %f"%(moyenne(co22[s2:e2+1])), fontsize=7)
    plt.text(start_date, 10*(max(var12)-min(var12))/13 + min(var12), u"med co2 = %f"%(mediane(co22[s2:e2+1])), fontsize=7)
    plt.text(start_date, 9*(max(var12)-min(var12))/13 + min(var12), u"EcTyp co2 = %f"%(ecartType(co22[s2:e2+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 2')
    ax13 = plt.subplot(323)
    plt.subplot(323)
    ax13.plot(sent_at3, co23, label='CO2 3', color = 'tab:purple')
    ax13.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at3)) != 0 :
        ax13.plot(sent_at3[anom(sent_at3)[0]:anom(sent_at3)[-1]+2], co23[anom(sent_at3)[0]:anom(sent_at3)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var13), u"min co2 = %f"%(min(co23[s3:e3+1])), fontsize=7)
    plt.text(start_date, 12*(max(var13)-min(var13))/13 + min(var13), u"max co2 = %f"%(max(co23[s3:e3+1])), fontsize=7)
    plt.text(start_date, 11*(max(var13)-min(var13))/13 + min(var13), u"moy co2 = %f"%(moyenne(co23[s3:e3+1])), fontsize=7)
    plt.text(start_date, 10*(max(var13)-min(var13))/13 + min(var13), u"med co2 = %f"%(mediane(co23[s3:e3+1])), fontsize=7)
    plt.text(start_date, 9*(max(var13)-min(var13))/13 + min(var13), u"EcTyp co2 = %f"%(ecartType(co23[s3:e3+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 3')
    ax14 = plt.subplot(324)
    plt.subplot(324)
    ax14.plot(sent_at4, co24, label='CO2 4', color = 'tab:purple')
    ax14.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at4)) != 0 :
        ax14.plot(sent_at4[anom(sent_at4)[0]:anom(sent_at4)[-1]+2], co24[anom(sent_at4)[0]:anom(sent_at4)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var14), u"min co2 = %f"%(min(co24[s4:e4+1])), fontsize=7)
    plt.text(start_date, 12*(max(var14)-min(var14))/13 + min(var14), u"max co2 = %f"%(max(co24[s4:e4+1])), fontsize=7)
    plt.text(start_date, 11*(max(var14)-min(var14))/13 + min(var14), u"moy co2 = %f"%(moyenne(co24[s4:e4+1])), fontsize=7)
    plt.text(start_date, 10*(max(var14)-min(var14))/13 + min(var14), u"med co2 = %f"%(mediane(co24[s4:e4+1])), fontsize=7)
    plt.text(start_date, 9*(max(var14)-min(var14))/13 + min(var14), u"EcTyp co2 = %f"%(ecartType(co24[s4:e4+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 4')
    ax15 = plt.subplot(325)
    plt.subplot(325)
    ax15.plot(sent_at5, co25, label='CO2 5', color = 'tab:purple')
    ax15.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at5)) != 0 :
        ax15.plot(sent_at5[anom(sent_at5)[0]:anom(sent_at5)[-1]+2], co25[anom(sent_at5)[0]:anom(sent_at5)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var15), u"min co2 = %f"%(min(co25[s5:e5+1])), fontsize=7)
    plt.text(start_date, 12*(max(var15)-min(var15))/13 + min(var15), u"max co2 = %f"%(max(co25[s5:e5+1])), fontsize=7)
    plt.text(start_date, 11*(max(var15)-min(var15))/13 + min(var15), u"moy co2 = %f"%(moyenne(co25[s5:e5+1])), fontsize=7)
    plt.text(start_date, 10*(max(var15)-min(var15))/13 + min(var15), u"med co2 = %f"%(mediane(co25[s5:e5+1])), fontsize=7)
    plt.text(start_date, 9*(max(var15)-min(var15))/13 + min(var15), u"EcTyp co2 = %f"%(ecartType(co25[s5:e5+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 5')
    ax16 = plt.subplot(326)
    plt.subplot(326)
    ax16.plot(sent_at6, co26, label='CO2 6', color = 'tab:purple')
    ax16.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at6)) != 0 :
        ax16.plot(sent_at6[anom(sent_at6)[0]:anom(sent_at6)[-1]+2], co26[anom(sent_at6)[0]:anom(sent_at6)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var16), u"min co2 = %f"%(min(lum6[s6:e6+1])), fontsize=7)
    plt.text(start_date, 12*(max(var16)-min(var16))/13 + min(var16), u"max co2 = %f"%(max(co26[s6:e6+1])), fontsize=7)
    plt.text(start_date, 11*(max(var16)-min(var16))/13 + min(var16), u"moy co2 = %f"%(moyenne(co26[s6:e6+1])), fontsize=7)
    plt.text(start_date, 10*(max(var16)-min(var16))/13 + min(var16), u"med co2 = %f"%(mediane(co26[s6:e6+1])), fontsize=7)
    plt.text(start_date, 9*(max(var16)-min(var16))/13 + min(var16), u"EcTyp co2 = %f"%(ecartType(co26[s6:e6+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 6')
elif variable1 == 'humidex' or variable1 == 'Humidex':
    ax11 = plt.subplot(321)
    plt.subplot(321)
    ax11.plot(sent_at1, humidex1, label='humidex 1', color = 'tab:purple')
    ax11.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at1)) != 0 :
        ax11.plot(sent_at1[anom(sent_at1)[0]:anom(sent_at1)[-1]+2], humidex1[anom(sent_at1)[0]:anom(sent_at1)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var11), u"min humidex = %f"%(min(humidex1[s1:e1+1])), fontsize=7)
    plt.text(start_date, 12*(max(var11)-min(var11))/13 + min(var11), u"max humidex = %f"%(max(humidex1[s1:e1+1])), fontsize=7)
    plt.text(start_date, 11*(max(var11)-min(var11))/13 + min(var11), u"moy humidex = %f"%(moyenne(humidex1[s1:e1+1])), fontsize=7)
    plt.text(start_date, 10*(max(var11)-min(var11))/13 + min(var11), u"med humidex = %f"%(mediane(humidex1[s1:e1+1])), fontsize=7)
    plt.text(start_date, 9*(max(var11)-min(var11))/13 + min(var11), u"EcTyp humidex = %f"%(ecartType(humidex1[s1:e1+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 1')
    ax12 = plt.subplot(322)
    plt.subplot(322)
    ax12.plot(sent_at2, humidex2, label='humidex 2', color = 'tab:purple')
    ax12.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at2)) != 0 :
        ax12.plot(sent_at2[anom(sent_at2)[0]:anom(sent_at2)[-1]+2], humidex2[anom(sent_at2)[0]:anom(sent_at2)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var12), u"min humidex = %f"%(min(humidex2[s2:e2+1])), fontsize=7)
    plt.text(start_date, 12*(max(var12)-min(var12))/13 + min(var12), u"max humidex = %f"%(max(humidex2[s2:e2+1])), fontsize=7)
    plt.text(start_date, 11*(max(var12)-min(var12))/13 + min(var12), u"moy humidex = %f"%(moyenne(humidex2[s2:e2+1])), fontsize=7)
    plt.text(start_date, 10*(max(var12)-min(var12))/13 + min(var12), u"med humidex = %f"%(mediane(humidex2[s2:e2+1])), fontsize=7)
    plt.text(start_date, 9*(max(var12)-min(var12))/13 + min(var12), u"EcTyp humidex = %f"%(ecartType(humidex2[s2:e2+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 2')
    ax13 = plt.subplot(323)
    plt.subplot(323)
    ax13.plot(sent_at3, humidex3, label='humidex 3', color = 'tab:purple')
    ax13.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at3)) != 0 :
        ax13.plot(sent_at3[anom(sent_at3)[0]:anom(sent_at3)[-1]+2], humidex3[anom(sent_at3)[0]:anom(sent_at3)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var13), u"min humidex = %f"%(min(humidex3[s3:e3+1])), fontsize=7)
    plt.text(start_date, 12*(max(var13)-min(var13))/13 + min(var13), u"max humidex = %f"%(max(humidex3[s3:e3+1])), fontsize=7)
    plt.text(start_date, 11*(max(var13)-min(var13))/13 + min(var13), u"moy humidex = %f"%(moyenne(humidex3[s3:e3+1])), fontsize=7)
    plt.text(start_date, 10*(max(var13)-min(var13))/13 + min(var13), u"med humidex = %f"%(mediane(humidex3[s3:e3+1])), fontsize=7)
    plt.text(start_date, 9*(max(var13)-min(var13))/13 + min(var13), u"EcTyp humidex = %f"%(ecartType(humidex3[s3:e3+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 3')
    ax14 = plt.subplot(324)
    plt.subplot(324)
    ax14.plot(sent_at4, humidex4, label='humidex 4', color = 'tab:purple')
    ax14.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at4)) != 0 :
        ax14.plot(sent_at4[anom(sent_at4)[0]:anom(sent_at4)[-1]+2], humidex4[anom(sent_at4)[0]:anom(sent_at4)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var14), u"min humidex = %f"%(min(humidex4[s4:e4+1])), fontsize=7)
    plt.text(start_date, 12*(max(var14)-min(var14))/13 + min(var14), u"max humidex = %f"%(max(humidex4[s4:e4+1])), fontsize=7)
    plt.text(start_date, 11*(max(var14)-min(var14))/13 + min(var14), u"moy humidex = %f"%(moyenne(humidex4[s4:e4+1])), fontsize=7)
    plt.text(start_date, 10*(max(var14)-min(var14))/13 + min(var14), u"med humidex = %f"%(mediane(humidex4[s4:e4+1])), fontsize=7)
    plt.text(start_date, 9*(max(var14)-min(var14))/13 + min(var14), u"EcTyp humidex = %f"%(ecartType(humidex4[s4:e4+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 4')
    ax15 = plt.subplot(325)
    plt.subplot(325)
    ax15.plot(sent_at5, humidex5, label='humidex 5', color = 'tab:purple')
    ax15.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at5)) != 0 :
        ax15.plot(sent_at5[anom(sent_at5)[0]:anom(sent_at5)[-1]+2], humidex5[anom(sent_at5)[0]:anom(sent_at5)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var15), u"min humidex = %f"%(min(humidex5[s5:e5+1])), fontsize=7)
    plt.text(start_date, 12*(max(var15)-min(var15))/13 + min(var15), u"max humidex = %f"%(max(humidex5[s5:e5+1])), fontsize=7)
    plt.text(start_date, 11*(max(var15)-min(var15))/13 + min(var15), u"moy humidex = %f"%(moyenne(humidex5[s5:e5+1])), fontsize=7)
    plt.text(start_date, 10*(max(var15)-min(var15))/13 + min(var15), u"med humidex = %f"%(mediane(humidex5[s5:e5+1])), fontsize=7)
    plt.text(start_date, 9*(max(var15)-min(var15))/13 + min(var15), u"EcTyp humidex = %f"%(ecartType(humidex5[s5:e5+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 5')
    ax16 = plt.subplot(326)
    plt.subplot(326)
    ax16.plot(sent_at6, humidex6, label='humidex 6', color = 'tab:purple')
    ax16.tick_params(axis='y',  labelcolor = 'tab:purple')
    if len(anom(sent_at6)) != 0 :
        ax16.plot(sent_at6[anom(sent_at6)[0]:anom(sent_at6)[-1]+2], humidex6[anom(sent_at6)[0]:anom(sent_at6)[-1]+2], color = 'tab:red')
    plt.text(start_date, max(var16), u"min humidex = %f"%(min(humidex6[s6:e6+1])), fontsize=7)
    plt.text(start_date, 12*(max(var16)-min(var16))/13 + min(var16), u"max humidex = %f"%(max(humidex6[s6:e6+1])), fontsize=7)
    plt.text(start_date, 11*(max(var16)-min(var16))/13 + min(var16), u"moy humidex = %f"%(moyenne(humidex6[s6:e6+1])), fontsize=7)
    plt.text(start_date, 10*(max(var16)-min(var16))/13 + min(var16), u"med humidex = %f"%(mediane(humidex6[s6:e6+1])), fontsize=7)
    plt.text(start_date, 9*(max(var16)-min(var16))/13 + min(var16), u"EcTyp humidex = %f"%(ecartType(humidex6[s6:e6+1])), fontsize=7)
    plt.xlim(start_date,end_date)
    plt.title('capteur 6')
else :
    print ("erreur d'entrée de variable1")

ax21 = ax11.twinx()
ax22 = ax12.twinx()
ax23 = ax13.twinx()
ax24 = ax14.twinx()
ax25 = ax15.twinx()
ax26 = ax16.twinx()

if variable2 != None :
    if variable2 == 'Temperature' or variable2 == 'temperature' or variable2 == 'Température' or variable2 == 'température':
        ax21.plot(sent_at1, temperature1, label='tem 1', color = 'tab:green')
        ax21.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at1)) != 0 :
            ax21.plot(sent_at1[anom(sent_at1)[0]:anom(sent_at1)[-1]+2], temperature1[anom(sent_at1)[0]:anom(sent_at1)[-1]+2], color = 'tab:red')
        ax11.text(start_date, 7*(max(var11)-min(var11))/13 + min(var11), u"min temp = %f"%(min(temperature1[s1:e1+1])), fontsize=7)
        ax11.text(start_date, 6*(max(var11)-min(var11))/13 + min(var11), u"max temp = %f"%(max(temperature1[s1:e1+1])), fontsize=7)
        ax11.text(start_date, 5*(max(var11)-min(var11))/13 + min(var11), u"moy temp = %f"%(moyenne(temperature1[s1:e1+1])), fontsize=7)
        ax11.text(start_date, 4*(max(var11)-min(var11))/13 + min(var11), u"med temp = %f"%(mediane(temperature1[s1:e1+1])), fontsize=7)
        ax11.text(start_date, 3*(max(var11)-min(var11))/13 + min(var11), u"EcTyp temp = %f"%(ecartType(temperature1[s1:e1+1])), fontsize=7)
        ax11.text(start_date, (max(var11)-min(var11))/13 + min(var11), u"coef corr = %f"%coefCorr(var11[s1:e1+1],var21[s1:e1+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax22.plot(sent_at2, temperature2, label='tem 2', color = 'tab:green')
        ax22.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at2)) != 0 :
            ax22.plot(sent_at2[anom(sent_at2)[0]:anom(sent_at2)[-1]+2], temperature2[anom(sent_at2)[0]:anom(sent_at2)[-1]+2], color = 'tab:red')
        ax12.text(start_date, 7*(max(var12)-min(var12))/13 + min(var12), u"min temp = %f"%(min(temperature2[s2:e2+1])), fontsize=7)
        ax12.text(start_date, 6*(max(var12)-min(var12))/13 + min(var12), u"max temp = %f"%(max(temperature2[s2:e2+1])), fontsize=7)
        ax12.text(start_date, 5*(max(var12)-min(var12))/13 + min(var12), u"moy temp = %f"%(moyenne(temperature2[s2:e2+1])), fontsize=7)
        ax12.text(start_date, 4*(max(var12)-min(var12))/13 + min(var12), u"med temp = %f"%(mediane(temperature2[s2:e2+1])), fontsize=7)
        ax12.text(start_date, 3*(max(var12)-min(var12))/13 + min(var12), u"EcTyp temp = %f"%(ecartType(temperature2[s2:e2+1])), fontsize=7)
        ax12.text(start_date, (max(var12)-min(var12))/13 + min(var12), u"coef corr = %f"%coefCorr(var12[s2:e2+1],var22[s2:e2+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax23.plot(sent_at3, temperature3, label='tem 3', color = 'tab:green')
        ax23.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at3)) != 0 :
            ax23.plot(sent_at3[anom(sent_at3)[0]:anom(sent_at3)[-1]+2], temperature3[anom(sent_at1)[0]:anom(sent_at3)[-1]+2], color = 'tab:red')
        ax13.text(start_date, 7*(max(var13)-min(var13))/13 + min(var13), u"min temp = %f"%(min(temperature3[s3:e3+1])), fontsize=7)
        ax13.text(start_date, 6*(max(var13)-min(var13))/13 + min(var13), u"max temp = %f"%(max(temperature3[s3:e3+1])), fontsize=7)
        ax13.text(start_date, 5*(max(var13)-min(var13))/13 + min(var13), u"moy temp = %f"%(moyenne(temperature3[s3:e3+1])), fontsize=7)
        ax13.text(start_date, 4*(max(var13)-min(var13))/13 + min(var13), u"med temp = %f"%(mediane(temperature3[s3:e3+1])), fontsize=7)
        ax13.text(start_date, 3*(max(var13)-min(var13))/13 + min(var13), u"EcTyp temp = %f"%(ecartType(temperature3[s3:e3+1])), fontsize=7)
        ax13.text(start_date, (max(var13)-min(var13))/13 + min(var13), u"coef corr = %f"%coefCorr(var13[s3:e3+1],var23[s3:e3+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax24.plot(sent_at4, temperature4, label='tem 4', color = 'tab:green')
        ax24.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at4)) != 0 :
            ax24.plot(sent_at4[anom(sent_at4)[0]:anom(sent_at4)[-1]+2], temperature4[anom(sent_at4)[0]:anom(sent_at4)[-1]+2], color = 'tab:red')
        ax14.text(start_date, 7*(max(var14)-min(var14))/13 + min(var14), u"min temp = %f"%(min(temperature4[s4:e4+1])), fontsize=7)
        ax14.text(start_date, 6*(max(var14)-min(var14))/13 + min(var14), u"max temp = %f"%(max(temperature4[s4:e4+1])), fontsize=7)
        ax14.text(start_date, 5*(max(var14)-min(var14))/13 + min(var14), u"moy temp = %f"%(moyenne(temperature4[s4:e4+1])), fontsize=7)
        ax14.text(start_date, 4*(max(var14)-min(var14))/13 + min(var14), u"med temp = %f"%(mediane(temperature4[s4:e4+1])), fontsize=7)
        ax14.text(start_date, 3*(max(var14)-min(var14))/13 + min(var14), u"EcTyp temp = %f"%(ecartType(temperature4[s4:e4+1])), fontsize=7)
        ax14.text(start_date, (max(var14)-min(var14))/13 + min(var14), u"coef corr = %f"%coefCorr(var14[s4:e4+1],var24[s4:e4+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax25.plot(sent_at5, temperature5, label='tem 5', color = 'tab:green')
        ax25.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at5)) != 0 :
            ax25.plot(sent_at5[anom(sent_at5)[0]:anom(sent_at5)[-1]+2], temperature5[anom(sent_at5)[0]:anom(sent_at5)[-1]+2], color = 'tab:red')
        ax15.text(start_date, 7*(max(var15)-min(var15))/13 + min(var15), u"min temp = %f"%(min(temperature5[s5:e5+1])), fontsize=7)
        ax15.text(start_date, 6*(max(var15)-min(var15))/13 + min(var15), u"max temp = %f"%(max(temperature5[s5:e5+1])), fontsize=7)
        ax15.text(start_date, 5*(max(var15)-min(var15))/13 + min(var15), u"moy temp = %f"%(moyenne(temperature5[s5:e5+1])), fontsize=7)
        ax15.text(start_date, 4*(max(var15)-min(var15))/13 + min(var15), u"med temp = %f"%(mediane(temperature5[s5:e5+1])), fontsize=7)
        ax15.text(start_date, 3*(max(var15)-min(var15))/13 + min(var15), u"EcTyp temp = %f"%(ecartType(temperature5[s5:e5+1])), fontsize=7)
        ax15.text(start_date, (max(var15)-min(var15))/13 + min(var15), u"coef corr = %f"%coefCorr(var15[s5:e5+1],var25[s5:e5+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax26.plot(sent_at6, temperature6, label='tem 6', color = 'tab:green')
        ax26.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at6)) != 0 :
            ax26.plot(sent_at6[anom(sent_at6)[0]:anom(sent_at6)[-1]+2], temperature6[anom(sent_at6)[0]:anom(sent_at6)[-1]+2], color = 'tab:red')
        ax16.text(start_date, 7*(max(var16)-min(var16))/13 + min(var16), u"min temp = %f"%(min(temperature6[s6:e6+1])), fontsize=7)
        ax16.text(start_date, 6*(max(var16)-min(var16))/13 + min(var16), u"max temp = %f"%(max(temperature6[s6:e6+1])), fontsize=7)
        ax16.text(start_date, 5*(max(var16)-min(var16))/13 + min(var16), u"moy temp = %f"%(moyenne(temperature6[s6:e6+1])), fontsize=7)
        ax16.text(start_date, 4*(max(var16)-min(var16))/13 + min(var16), u"med temp = %f"%(mediane(temperature6[s6:e6+1])), fontsize=7)
        ax16.text(start_date, 3*(max(var16)-min(var16))/13 + min(var16), u"EcTyp temp = %f"%(ecartType(temperature6[s6:e6+1])), fontsize=7)
        ax16.text(start_date, (max(var16)-min(var16))/13 + min(var16), u"coef corr = %f"%coefCorr(var16[s6:e6+1],var26[s6:e6+1]), fontsize=7)
        plt.xlim(start_date,end_date)
    elif variable2 == 'bruit' or variable2 == 'Bruit':
        ax21.plot(sent_at1, noise1, label='bruit 1', color = 'tab:green')
        ax21.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at1)) != 0 :
            ax21.plot(sent_at1[anom(sent_at1)[0]:anom(sent_at1)[-1]+2], noise1[anom(sent_at1)[0]:anom(sent_at1)[-1]+2], color = 'tab:red')
        ax11.text(start_date, 7*(max(var11)-min(var11))/13 + min(var11), u"min bruit = %f"%(min(noise1[s1:e1+1])), fontsize=7)
        ax11.text(start_date, 6*(max(var11)-min(var11))/13 + min(var11), u"max bruit = %f"%(max(noise1[s1:e1+1])), fontsize=7)
        ax11.text(start_date, 5*(max(var11)-min(var11))/13 + min(var11), u"moy bruit = %f"%(moyenne(noise1[s1:e1+1])), fontsize=7)
        ax11.text(start_date, 4*(max(var11)-min(var11))/13 + min(var11), u"med bruit = %f"%(mediane(noise1[s1:e1+1])), fontsize=7)
        ax11.text(start_date, 3*(max(var11)-min(var11))/13 + min(var11), u"EcTyp bruit = %f"%(ecartType(noise1[s1:e1+1])), fontsize=7)
        ax11.text(start_date, (max(var11)-min(var11))/13 + min(var11), u"coef corr = %f"%coefCorr(var11[s1:e1+1],var21[s1:e1+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax22.plot(sent_at2, noise2, label='bruit 2', color = 'tab:green')
        ax22.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at2)) != 0 :
            ax22.plot(sent_at2[anom(sent_at2)[0]:anom(sent_at2)[-1]+2], noise2[anom(sent_at2)[0]:anom(sent_at2)[-1]+2], color = 'tab:red')
        ax12.text(start_date, 7*(max(var12)-min(var12))/13 + min(var12), u"min bruit = %f"%(min(noise2[s2:e2+1])), fontsize=7)
        ax12.text(start_date, 6*(max(var12)-min(var12))/13 + min(var12), u"max bruit = %f"%(max(noise2[s2:e2+1])), fontsize=7)
        ax12.text(start_date, 5*(max(var12)-min(var12))/13 + min(var12), u"moy bruit = %f"%(moyenne(noise2[s2:e2+1])), fontsize=7)
        ax12.text(start_date, 4*(max(var12)-min(var12))/13 + min(var12), u"med bruit = %f"%(mediane(noise2[s2:e2+1])), fontsize=7)
        ax12.text(start_date, 3*(max(var12)-min(var12))/13 + min(var12), u"EcTyp bruit = %f"%(ecartType(noise2[s2:e2+1])), fontsize=7)
        ax12.text(start_date, (max(var12)-min(var12))/13 + min(var12), u"coef corr = %f"%coefCorr(var12[s2:e2+1],var22[s2:e2+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax23.plot(sent_at3, noise3, label='bruit 3', color = 'tab:green')
        ax23.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at3)) != 0 :
            ax23.plot(sent_at1[anom(sent_at3)[0]:anom(sent_at3)[-1]+2], noise3[anom(sent_at3)[0]:anom(sent_at3)[-1]+2], color = 'tab:red')
        ax13.text(start_date, 7*(max(var13)-min(var13))/13 + min(var13), u"min bruit = %f"%(min(noise3[s3:e3+1])), fontsize=7)
        ax13.text(start_date, 6*(max(var13)-min(var13))/13 + min(var13), u"max bruit = %f"%(max(noise3[s3:e3+1])), fontsize=7)
        ax13.text(start_date, 5*(max(var13)-min(var13))/13 + min(var13), u"moy bruit = %f"%(moyenne(noise3[s3:e3+1])), fontsize=7)
        ax13.text(start_date, 4*(max(var13)-min(var13))/13 + min(var13), u"med bruit = %f"%(mediane(noise3[s3:e3+1])), fontsize=7)
        ax13.text(start_date, 3*(max(var13)-min(var13))/13 + min(var13), u"EcTyp bruit = %f"%(ecartType(noise3[s3:e3+1])), fontsize=7)
        ax13.text(start_date, (max(var13)-min(var13))/13 + min(var13), u"coef corr = %f"%coefCorr(var13[s3:e3+1],var23[s3:e3+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax24.plot(sent_at4, noise4, label='bruit 4', color = 'tab:green')
        ax24.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at4)) != 0 :
            ax24.plot(sent_at4[anom(sent_at4)[0]:anom(sent_at4)[-1]+2], noise4[anom(sent_at4)[0]:anom(sent_at4)[-1]+2], color = 'tab:red')
        ax14.text(start_date, 7*(max(var14)-min(var14))/13 + min(var14), u"min bruit = %f"%(min(noise4[s4:e4+1])), fontsize=7)
        ax14.text(start_date, 6*(max(var14)-min(var14))/13 + min(var14), u"max bruit = %f"%(max(noise4[s4:e4+1])), fontsize=7)
        ax14.text(start_date, 5*(max(var14)-min(var14))/13 + min(var14), u"moy bruit = %f"%(moyenne(noise4[s4:e4+1])), fontsize=7)
        ax14.text(start_date, 4*(max(var14)-min(var14))/13 + min(var14), u"med bruit = %f"%(mediane(noise4[s4:e4+1])), fontsize=7)
        ax14.text(start_date, 3*(max(var14)-min(var14))/13 + min(var14), u"EcTyp bruit = %f"%(ecartType(noise4[s4:e4+1])), fontsize=7)
        ax14.text(start_date, (max(var14)-min(var14))/13 + min(var14), u"coef corr = %f"%coefCorr(var14[s4:e4+1],var24[s4:e4+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax25.plot(sent_at5, noise5, label='bruit 5', color = 'tab:green')
        ax25.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at5)) != 0 :
            ax25.plot(sent_at5[anom(sent_at5)[0]:anom(sent_at5)[-1]+2], noise5[anom(sent_at5)[0]:anom(sent_at5)[-1]+2], color = 'tab:red')
        ax15.text(start_date, 7*(max(var15)-min(var15))/13 + min(var15), u"min bruit = %f"%(min(noise5[s5:e5+1])), fontsize=7)
        ax15.text(start_date, 6*(max(var15)-min(var15))/13 + min(var15), u"max bruit = %f"%(max(noise5[s5:e5+1])), fontsize=7)
        ax15.text(start_date, 5*(max(var15)-min(var15))/13 + min(var15), u"moy bruit = %f"%(moyenne(noise5[s5:e5+1])), fontsize=7)
        ax15.text(start_date, 4*(max(var15)-min(var15))/13 + min(var15), u"med bruit = %f"%(mediane(noise5[s5:e5+1])), fontsize=7)
        ax15.text(start_date, 3*(max(var15)-min(var15))/13 + min(var15), u"EcTyp bruit = %f"%(ecartType(noise5[s5:e5+1])), fontsize=7)
        ax15.text(start_date, (max(var15)-min(var15))/13 + min(var15), u"coef corr = %f"%coefCorr(var15[s5:e5+1],var25[s5:e5+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax26.plot(sent_at6, noise6, label='bruit 6', color = 'tab:green')
        ax26.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at6)) != 0 :
            ax26.plot(sent_at6[anom(sent_at6)[0]:anom(sent_at6)[-1]+2], noise6[anom(sent_at6)[0]:anom(sent_at6)[-1]+2], color = 'tab:red')
        ax16.text(start_date, 7*(max(var16)-min(var16))/13 + min(var16), u"min bruit = %f"%(min(noise6[s6:e6+1])), fontsize=7)
        ax16.text(start_date, 6*(max(var16)-min(var16))/13 + min(var16), u"max bruit = %f"%(max(noise6[s6:e6+1])), fontsize=7)
        ax16.text(start_date, 5*(max(var16)-min(var16))/13 + min(var16), u"moy bruit = %f"%(moyenne(noise6[s6:e6+1])), fontsize=7)
        ax16.text(start_date, 4*(max(var16)-min(var16))/13 + min(var16), u"med bruit = %f"%(mediane(noise6[s6:e6+1])), fontsize=7)
        ax16.text(start_date, 3*(max(var16)-min(var16))/13 + min(var16), u"EcTyp bruit = %f"%(ecartType(noise6[s6:e6+1])), fontsize=7)
        ax16.text(start_date, (max(var16)-min(var16))/13 + min(var16), u"coef corr = %f"%coefCorr(var16[s6:e6+1],var26[s6:e6+1]), fontsize=7)
        plt.xlim(start_date,end_date)
    elif variable2 == 'Humidité' or variable2 == 'humidité' or variable2 == 'Humidite' or variable2 == 'humidite' :
        ax21.plot(sent_at1, humidity1, label='hum 1', color = 'tab:green')
        ax21.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at1)) != 0 :
            ax21.plot(sent_at1[anom(sent_at1)[0]:anom(sent_at1)[-1]+2], humidity1[anom(sent_at1)[0]:anom(sent_at1)[-1]+2], color = 'tab:red')
        ax11.text(start_date, 7*(max(var11)-min(var11))/13 + min(var11), u"min hum = %f"%(min(humidity1[s1:e1+1])), fontsize=7)
        ax11.text(start_date, 6*(max(var11)-min(var11))/13 + min(var11), u"max hum = %f"%(max(humidity1[s1:e1+1])), fontsize=7)
        ax11.text(start_date, 5*(max(var11)-min(var11))/13 + min(var11), u"moy hum = %f"%(moyenne(humidity1[s1:e1+1])), fontsize=7)
        ax11.text(start_date, 4*(max(var11)-min(var11))/13 + min(var11), u"med hum = %f"%(mediane(humidity1[s1:e1+1])), fontsize=7)
        ax11.text(start_date, 3*(max(var11)-min(var11))/13 + min(var11), u"EcTyp hum = %f"%(ecartType(humidity1[s1:e1+1])), fontsize=7)
        ax11.text(start_date, (max(var11)-min(var11))/13 + min(var11), u"coef corr = %f"%coefCorr(var11[s1:e1+1],var21[s1:e1+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax22.plot(sent_at2, humidity2, label='hum 2', color = 'tab:green')
        ax22.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at2)) != 0 :
            ax22.plot(sent_at2[anom(sent_at2)[0]:anom(sent_at2)[-1]+2], humidity2[anom(sent_at2)[0]:anom(sent_at2)[-1]+2], color = 'tab:red')
        ax12.text(start_date, 7*(max(var12)-min(var12))/13 + min(var12), u"min hum = %f"%(min(humidity2[s2:e2+1])), fontsize=7)
        ax12.text(start_date, 6*(max(var12)-min(var12))/13 + min(var12), u"max hum = %f"%(max(humidity2[s2:e2+1])), fontsize=7)
        ax12.text(start_date, 5*(max(var12)-min(var12))/13 + min(var12), u"moy hum = %f"%(moyenne(humidity2[s2:e2+1])), fontsize=7)
        ax12.text(start_date, 4*(max(var12)-min(var12))/13 + min(var12), u"med hum = %f"%(mediane(humidity2[s2:e2+1])), fontsize=7)
        ax12.text(start_date, 3*(max(var12)-min(var12))/13 + min(var12), u"EcTyp hum = %f"%(ecartType(humidity2[s2:e2+1])), fontsize=7)
        ax12.text(start_date, (max(var12)-min(var12))/13 + min(var12), u"coef corr = %f"%coefCorr(var12[s2:e2+1],var22[s2:e2+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax23.plot(sent_at3, humidity3, label='hum 3', color = 'tab:green')
        ax23.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at3)) != 0 :
            ax23.plot(sent_at3[anom(sent_at3)[0]:anom(sent_at3)[-1]+2], humidity3[anom(sent_at3)[0]:anom(sent_at3)[-1]+2], color = 'tab:red')
        ax13.text(start_date, 7*(max(var13)-min(var13))/13 + min(var13), u"min hum = %f"%(min(humidity3[s3:e3+1])), fontsize=7)
        ax13.text(start_date, 6*(max(var13)-min(var13))/13 + min(var13), u"max hum = %f"%(max(humidity3[s3:e3+1])), fontsize=7)
        ax13.text(start_date, 5*(max(var13)-min(var13))/13 + min(var13), u"moy hum = %f"%(moyenne(humidity3[s3:e3+1])), fontsize=7)
        ax13.text(start_date, 4*(max(var13)-min(var13))/13 + min(var13), u"med hum = %f"%(mediane(humidity3[s3:e3+1])), fontsize=7)
        ax13.text(start_date, 3*(max(var13)-min(var13))/13 + min(var13), u"EcTyp hum = %f"%(ecartType(humidity3[s3:e3+1])), fontsize=7)
        ax13.text(start_date, (max(var13)-min(var13))/13 + min(var13), u"coef corr = %f"%coefCorr(var13[s3:e3+1],var23[s3:e3+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax24.plot(sent_at4, humidity4, label='hum 4', color = 'tab:green')
        ax24.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at4)) != 0 :
            ax24.plot(sent_at4[anom(sent_at4)[0]:anom(sent_at4)[-1]+2], humidity4[anom(sent_at1)[0]:anom(sent_at4)[-1]+2], color = 'tab:red')
        ax14.text(start_date, 7*(max(var14)-min(var14))/13 + min(var14), u"min hum = %f"%(min(humidity4[s4:e4+1])), fontsize=7)
        ax14.text(start_date, 6*(max(var14)-min(var14))/13 + min(var14), u"max hum = %f"%(max(humidity4[s4:e4+1])), fontsize=7)
        ax14.text(start_date, 5*(max(var14)-min(var14))/13 + min(var14), u"moy hum = %f"%(moyenne(humidity4[s4:e4+1])), fontsize=7)
        ax14.text(start_date, 4*(max(var14)-min(var14))/13 + min(var14), u"med hum = %f"%(mediane(humidity4[s4:e4+1])), fontsize=7)
        ax14.text(start_date, 3*(max(var14)-min(var14))/13 + min(var14), u"EcTyp hum = %f"%(ecartType(humidity4[s4:e4+1])), fontsize=7)
        ax14.text(start_date, (max(var14)-min(var14))/13 + min(var14), u"coef corr = %f"%coefCorr(var14[s4:e4+1],var24[s4:e4+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax25.plot(sent_at5, humidity5, label='hum 5', color = 'tab:green')
        ax25.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at5)) != 0 :
            ax25.plot(sent_at5[anom(sent_at5)[0]:anom(sent_at5)[-1]+2], humidity5[anom(sent_at5)[0]:anom(sent_at5)[-1]+2], color = 'tab:red')
        ax15.text(start_date, 7*(max(var15)-min(var15))/13 + min(var15), u"min hum = %f"%(min(humidity5[s5:e5+1])), fontsize=7)
        ax15.text(start_date, 6*(max(var15)-min(var15))/13 + min(var15), u"max hum = %f"%(max(humidity5[s5:e5+1])), fontsize=7)
        ax15.text(start_date, 5*(max(var15)-min(var15))/13 + min(var15), u"moy hum = %f"%(moyenne(humidity5[s5:e5+1])), fontsize=7)
        ax15.text(start_date, 4*(max(var15)-min(var15))/13 + min(var15), u"med hum = %f"%(mediane(humidity5[s5:e5+1])), fontsize=7)
        ax15.text(start_date, 3*(max(var15)-min(var15))/13 + min(var15), u"EcTyp hum = %f"%(ecartType(humidity5[s5:e5+1])), fontsize=7)
        ax15.text(start_date, (max(var15)-min(var15))/13 + min(var15), u"coef corr = %f"%coefCorr(var15[s5:e5+1],var25[s5:e5+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax26.plot(sent_at6, humidity6, label='hum 6', color = 'tab:green')
        ax26.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at6)) != 0 :
            ax26.plot(sent_at6[anom(sent_at6)[0]:anom(sent_at6)[-1]+2], humidity6[anom(sent_at6)[0]:anom(sent_at6)[-1]+2], color = 'tab:red')
        ax16.text(start_date, 7*(max(var16)-min(var16))/13 + min(var16), u"min hum = %f"%(min(humidity6[s6:e6+1])), fontsize=7)
        ax16.text(start_date, 6*(max(var16)-min(var16))/13 + min(var16), u"max hum = %f"%(moyenne(humidity6[s6:e6+1])), fontsize=7)
        ax16.text(start_date, 5*(max(var16)-min(var16))/13 + min(var16), u"moy hum = %f"%(moyenne(humidity6[s6:e6+1])), fontsize=7)
        ax16.text(start_date, 4*(max(var16)-min(var16))/13 + min(var16), u"med hum = %f"%(mediane(humidity6[s6:e6+1])), fontsize=7)
        ax16.text(start_date, 3*(max(var16)-min(var16))/13 + min(var16), u"EcTyp hum = %f"%(ecartType(humidity6[s6:e6+1])), fontsize=7)
        ax16.text(start_date, (max(var16)-min(var16))/13 + min(var16), u"coef corr = %f"%coefCorr(var16[s6:e6+1],var26[s6:e6+1]), fontsize=7)
        plt.xlim(start_date,end_date)
    elif variable2 == 'Lumière' or variable2 == 'lumière' or variable2 == 'Lumiere' or variable2 == 'lumiere' :
        ax21.plot(sent_at1, lum1, label='lum 1', color = 'tab:green')
        ax21.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at1)) != 0 :
            ax21.plot(sent_at1[anom(sent_at1)[0]:anom(sent_at1)[-1]+2], lum1[anom(sent_at1)[0]:anom(sent_at1)[-1]+2], color = 'tab:red')
        ax11.text(start_date, 7*(max(var11)-min(var11))/13 + min(var11), u"min lum = %f"%(min(lum1[s1:e1+1])), fontsize=7)
        ax11.text(start_date, 6*(max(var11)-min(var11))/13 + min(var11), u"max lum = %f"%(max(lum1[s1:e1+1])), fontsize=7)
        ax11.text(start_date, 5*(max(var11)-min(var11))/13 + min(var11), u"moy lum = %f"%(moyenne(lum1[s1:e1+1])), fontsize=7)
        ax11.text(start_date, 4*(max(var11)-min(var11))/13 + min(var11), u"med lum = %f"%(mediane(lum1[s1:e1+1])), fontsize=7)
        ax11.text(start_date, 3*(max(var11)-min(var11))/13 + min(var11), u"EcTyp lum = %f"%(ecartType(lum1[s1:e1+1])), fontsize=7)
        ax11.text(start_date, (max(var11)-min(var11))/13 + min(var11), u"coef corr = %f"%coefCorr(var11[s1:e1+1],var21[s1:e1+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax22.plot(sent_at2, lum2, label='lum 2', color = 'tab:green')
        ax22.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at2)) != 0 :
            ax22.plot(sent_at2[anom(sent_at2)[0]:anom(sent_at2)[-1]+2], lum2[anom(sent_at2)[0]:anom(sent_at2)[-1]+2], color = 'tab:red')
        ax12.text(start_date, 7*(max(var12)-min(var12))/13 + min(var12), u"min lum = %f"%(min(lum2[s2:e2+1])), fontsize=7)
        ax12.text(start_date, 6*(max(var12)-min(var12))/13 + min(var12), u"max lum = %f"%(max(lum2[s2:e2+1])), fontsize=7)
        ax12.text(start_date, 5*(max(var12)-min(var12))/13 + min(var12), u"moy lum = %f"%(moyenne(lum2[s2:e2+1])), fontsize=7)
        ax12.text(start_date, 4*(max(var12)-min(var12))/13 + min(var12), u"med lum = %f"%(mediane(lum2[s2:e2+1])), fontsize=7)
        ax12.text(start_date, 3*(max(var12)-min(var12))/13 + min(var12), u"EcTyp lum = %f"%(ecartType(lum2[s2:e2+1])), fontsize=7)
        ax12.text(start_date, (max(var12)-min(var12))/13 + min(var12), u"coef corr = %f"%coefCorr(var12[s2:e2+1],var22[s2:e2+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax23.plot(sent_at3, lum3, label='lum 3', color = 'tab:green')
        ax23.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at3)) != 0 :
            ax23.plot(sent_at3[anom(sent_at3)[0]:anom(sent_at3)[-1]+2], lum3[anom(sent_at3)[0]:anom(sent_at3)[-1]+2], color = 'tab:red')
        ax13.text(start_date, 7*(max(var13)-min(var13))/13 + min(var13), u"min lum = %f"%(min(lum3[s3:e3+1])), fontsize=7)
        ax13.text(start_date, 6*(max(var13)-min(var13))/13 + min(var13), u"max lum = %f"%(max(lum3[s3:e3+1])), fontsize=7)
        ax13.text(start_date, 5*(max(var13)-min(var13))/13 + min(var13), u"moy lum = %f"%(moyenne(lum3[s3:e3+1])), fontsize=7)
        ax13.text(start_date, 4*(max(var13)-min(var13))/13 + min(var13), u"med lum = %f"%(mediane(lum3[s3:e3+1])), fontsize=7)
        ax13.text(start_date, 3*(max(var13)-min(var13))/13 + min(var13), u"EcTyp lum = %f"%(ecartType(lum3[s3:e3+1])), fontsize=7)
        ax13.text(start_date, (max(var13)-min(var13))/13 + min(var13), u"coef corr = %f"%coefCorr(var13[s3:e3+1],var23[s3:e3+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax24.plot(sent_at4, lum4, label='lum 4', color = 'tab:green')
        ax24.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at4)) != 0 :
            ax24.plot(sent_at4[anom(sent_at4)[0]:anom(sent_at4)[-1]+2], lum4[anom(sent_at4)[0]:anom(sent_at4)[-1]+2], color = 'tab:red')
        ax14.text(start_date, 7*(max(var14)-min(var14))/13 + min(var14), u"min lum = %f"%(min(lum4[s4:e4+1])), fontsize=7)
        ax14.text(start_date, 6*(max(var14)-min(var14))/13 + min(var14), u"max lum = %f"%(max(lum4[s4:e4+1])), fontsize=7)
        ax14.text(start_date, 5*(max(var14)-min(var14))/13 + min(var14), u"moy lum = %f"%(moyenne(lum4[s4:e4+1])), fontsize=7)
        ax14.text(start_date, 4*(max(var14)-min(var14))/13 + min(var14), u"med lum = %f"%(mediane(lum4[s4:e4+1])), fontsize=7)
        ax14.text(start_date, 3*(max(var14)-min(var14))/13 + min(var14), u"EcTyp lum = %f"%(ecartType(lum4[s4:e4+1])), fontsize=7)
        ax14.text(start_date, (max(var14)-min(var14))/13 + min(var14), u"coef corr = %f"%coefCorr(var14[s4:e4+1],var24[s4:e4+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax25.plot(sent_at5, lum5, label='lum 5', color = 'tab:green')
        ax25.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at5)) != 0 :
            ax25.plot(sent_at5[anom(sent_at5)[0]:anom(sent_at5)[-1]+2], lum5[anom(sent_at5)[0]:anom(sent_at5)[-1]+2], color = 'tab:red')
        ax15.text(start_date, 7*(max(var15)-min(var15))/13 + min(var15), u"min lum = %f"%(min(lum5[s5:e5+1])), fontsize=7)
        ax15.text(start_date, 6*(max(var15)-min(var15))/13 + min(var15), u"max lum = %f"%(max(lum5[s5:e5+1])), fontsize=7)
        ax15.text(start_date, 5*(max(var15)-min(var15))/13 + min(var15), u"moy lum = %f"%(moyenne(lum5[s5:e5+1])), fontsize=7)
        ax15.text(start_date, 4*(max(var15)-min(var15))/13 + min(var15), u"med lum = %f"%(mediane(lum5[s5:e5+1])), fontsize=7)
        ax15.text(start_date, 3*(max(var15)-min(var15))/13 + min(var15), u"EcTyp lum = %f"%(ecartType(lum5[s5:e5+1])), fontsize=7)
        ax15.text(start_date, (max(var15)-min(var15))/13 + min(var15), u"coef corr = %f"%coefCorr(var15[s5:e5+1],var25[s5:e5+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax26.plot(sent_at6, lum6, label='lum 6', color = 'tab:green')
        ax26.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at6)) != 0 :
            ax26.plot(sent_at6[anom(sent_at6)[0]:anom(sent_at6)[-1]+2], lum6[anom(sent_at6)[0]:anom(sent_at6)[-1]+2], color = 'tab:red')
        ax16.text(start_date, 7*(max(var16)-min(var16))/13 + min(var16), u"min lum = %f"%(min(lum6[s6:e6+1])), fontsize=7)
        ax16.text(start_date, 6*(max(var16)-min(var16))/13 + min(var16), u"max lum = %f"%(moyenne(lum6[s6:e6+1])), fontsize=7)
        ax16.text(start_date, 5*(max(var16)-min(var16))/13 + min(var16), u"moy lum = %f"%(moyenne(lum6[s6:e6+1])), fontsize=7)
        ax16.text(start_date, 4*(max(var16)-min(var16))/13 + min(var16), u"med lum = %f"%(mediane(lum6[s6:e6+1])), fontsize=7)
        ax16.text(start_date, 3*(max(var16)-min(var16))/13 + min(var16), u"EcTyp lum = %f"%(ecartType(lum6[s6:e6+1])), fontsize=7)
        ax16.text(start_date, (max(var16)-min(var16))/13 + min(var16), u"coef corr = %f"%coefCorr(var16[s6:e6+1],var26[s6:e6+1]), fontsize=7)
        plt.xlim(start_date,end_date)
    elif variable2 == 'CO2' or variable2 == 'Co2' or variable2 == 'co2':
        ax21.plot(sent_at1, co21, label='co2 1', color = 'tab:green')
        ax21.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at1)) != 0 :
            ax21.plot(sent_at1[anom(sent_at1)[0]:anom(sent_at1)[-1]+2], co21[anom(sent_at1)[0]:anom(sent_at1)[-1]+2], color = 'tab:red')
        ax11.text(start_date, 7*(max(var11)-min(var11))/13 + min(var11), u"min co2 = %f"%(min(co21[s1:e1+1])), fontsize=7)
        ax11.text(start_date, 6*(max(var11)-min(var11))/13 + min(var11), u"max co2 = %f"%(max(co21[s1:e1+1])), fontsize=7)
        ax11.text(start_date, 5*(max(var11)-min(var11))/13 + min(var11), u"moy co2 = %f"%(moyenne(co21[s1:e1+1])), fontsize=7)
        ax11.text(start_date, 4*(max(var11)-min(var11))/13 + min(var11), u"med co2 = %f"%(mediane(co21[s1:e1+1])), fontsize=7)
        ax11.text(start_date, 3*(max(var11)-min(var11))/13 + min(var11), u"EcTyp co2 = %f"%(ecartType(co21[s1:e1+1])), fontsize=7)
        ax11.text(start_date, (max(var11)-min(var11))/13 + min(var11), u"coef corr = %f"%coefCorr(var11[s1:e1+1],var21[s1:e1+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax22.plot(sent_at2, co22, label='co2 2', color = 'tab:green')
        ax22.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at2)) != 0 :
            ax22.plot(sent_at2[anom(sent_at2)[0]:anom(sent_at2)[-1]+2], co22[anom(sent_at2)[0]:anom(sent_at2)[-1]+2], color = 'tab:red')
        ax12.text(start_date, 7*(max(var12)-min(var12))/13 + min(var12), u"min co2 = %f"%(min(co22[s2:e2+1])), fontsize=7)
        ax12.text(start_date, 6*(max(var12)-min(var12))/13 + min(var12), u"max co2 = %f"%(max(co22[s2:e2+1])), fontsize=7)
        ax12.text(start_date, 5*(max(var12)-min(var12))/13 + min(var12), u"moy co2 = %f"%(moyenne(co22[s2:e2+1])), fontsize=7)
        ax12.text(start_date, 4*(max(var12)-min(var12))/13 + min(var12), u"med co2 = %f"%(mediane(co22[s2:e2+1])), fontsize=7)
        ax12.text(start_date, 3*(max(var12)-min(var12))/13 + min(var12), u"EcTyp co2 = %f"%(ecartType(co22[s2:e2+1])), fontsize=7)
        ax12.text(start_date, (max(var12)-min(var12))/13 + min(var12), u"coef corr = %f"%coefCorr(var12[s2:e2+1],var22[s2:e2+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax23.plot(sent_at3, co23, label='co2 3', color = 'tab:green')
        ax23.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at3)) != 0 :
            ax23.plot(sent_at3[anom(sent_at3)[0]:anom(sent_at3)[-1]+2], co23[anom(sent_at3)[0]:anom(sent_at3)[-1]+2], color = 'tab:red')
        ax13.text(start_date, 7*(max(var13)-min(var13))/13 + min(var13), u"min co2 = %f"%(min(co23[s3:e3+1])), fontsize=7)
        ax13.text(start_date, 6*(max(var13)-min(var13))/13 + min(var13), u"max co2 = %f"%(max(co23[s3:e3+1])), fontsize=7)
        ax13.text(start_date, 5*(max(var13)-min(var13))/13 + min(var13), u"moy co2 = %f"%(moyenne(co23[s3:e3+1])), fontsize=7)
        ax13.text(start_date, 4*(max(var13)-min(var13))/13 + min(var13), u"med co2 = %f"%(mediane(co23[s3:e3+1])), fontsize=7)
        ax13.text(start_date, 3*(max(var13)-min(var13))/13 + min(var13), u"EcTyp co2 = %f"%(ecartType(co23[s3:e3+1])), fontsize=7)
        ax13.text(start_date, (max(var13)-min(var13))/13 + min(var13), u"coef corr = %f"%coefCorr(var13[s3:e3+1],var23[s3:e3+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax24.plot(sent_at4, co24, label='co2 4', color = 'tab:green')
        ax24.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at4)) != 0 :
            ax24.plot(sent_at4[anom(sent_at4)[0]:anom(sent_at4)[-1]+2], co24[anom(sent_at4)[0]:anom(sent_at4)[-1]+2], color = 'tab:red')
        ax14.text(start_date, 7*(max(var14)-min(var14))/13 + min(var14), u"min co2 = %f"%(min(co24[s4:e4+1])), fontsize=7)
        ax14.text(start_date, 6*(max(var14)-min(var14))/13 + min(var14), u"max co2 = %f"%(max(co24[s4:e4+1])), fontsize=7)
        ax14.text(start_date, 5*(max(var14)-min(var14))/13 + min(var14), u"moy co2 = %f"%(moyenne(co24[s4:e4+1])), fontsize=7)
        ax14.text(start_date, 4*(max(var14)-min(var14))/13 + min(var14), u"med co2 = %f"%(mediane(co24[s4:e4+1])), fontsize=7)
        ax14.text(start_date, 3*(max(var14)-min(var14))/13 + min(var14), u"EcTyp co2 = %f"%(ecartType(co24[s4:e4+1])), fontsize=7)
        ax14.text(start_date, (max(var14)-min(var14))/13 + min(var14), u"coef corr = %f"%coefCorr(var14[s4:e4+1],var24[s4:e4+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax25.plot(sent_at5, co25, label='co2 5', color = 'tab:green')
        ax25.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at5)) != 0 :
            ax25.plot(sent_at5[anom(sent_at5)[0]:anom(sent_at5)[-1]+2], co25[anom(sent_at5)[0]:anom(sent_at5)[-1]+2], color = 'tab:red')
        ax15.text(start_date, 7*(max(var15)-min(var15))/13 + min(var15), u"min co2 = %f"%(min(co25[s5:e5+1])), fontsize=7)
        ax15.text(start_date, 6*(max(var15)-min(var15))/13 + min(var15), u"max co2 = %f"%(max(co25[s5:e5+1])), fontsize=7)
        ax15.text(start_date, 5*(max(var15)-min(var15))/13 + min(var15), u"moy co2 = %f"%(moyenne(co25[s5:e5+1])), fontsize=7)
        ax15.text(start_date, 4*(max(var15)-min(var15))/13 + min(var15), u"med co2 = %f"%(mediane(co25[s5:e5+1])), fontsize=7)
        ax15.text(start_date, 3*(max(var15)-min(var15))/13 + min(var15), u"EcTyp co2 = %f"%(ecartType(co25[s5:e5+1])), fontsize=7)
        ax15.text(start_date, (max(var15)-min(var15))/13 + min(var15), u"coef corr = %f"%coefCorr(var15[s5:e5+1],var25[s5:e5+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax26.plot(sent_at6, co26, label='co2 6', color = 'tab:green')
        ax26.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at6)) != 0 :
            ax26.plot(sent_at6[anom(sent_at6)[0]:anom(sent_at6)[-1]+2], co26[anom(sent_at6)[0]:anom(sent_at6)[-1]+2], color = 'tab:red')
        ax16.text(start_date, 7*(max(var16)-min(var16))/13 + min(var16), u"min co2 = %f"%(min(co26[s6:e6+1])), fontsize=7)
        ax16.text(start_date, 6*(max(var16)-min(var16))/13 + min(var16), u"max co2 = %f"%(moyenne(co26[s6:e6+1])), fontsize=7)
        ax16.text(start_date, 5*(max(var16)-min(var16))/13 + min(var16), u"moy co2 = %f"%(moyenne(co26[s6:e6+1])), fontsize=7)
        ax16.text(start_date, 4*(max(var16)-min(var16))/13 + min(var16), u"med co2 = %f"%(mediane(co26[s6:e6+1])), fontsize=7)
        ax16.text(start_date, 3*(max(var16)-min(var16))/13 + min(var16), u"EcTyp co2 = %f"%(ecartType(co26[s6:e6+1])), fontsize=7)
        ax16.text(start_date, (max(var16)-min(var16))/13 + min(var16), u"coef corr = %f"%coefCorr(var16[s6:e6+1],var26[s6:e6+1]), fontsize=7)
        plt.xlim(start_date,end_date)
    elif variable2 == 'humidex' or variable2 == 'Humidex':
        ax21.plot(sent_at1, humidex1, label='humidex 1', color = 'tab:green')
        ax21.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at1)) != 0 :
            ax21.plot(sent_at1[anom(sent_at1)[0]:anom(sent_at1)[-1]+2], humidex1[anom(sent_at1)[0]:anom(sent_at1)[-1]+2], color = 'tab:red')
        ax11.text(start_date, 7*(max(var11)-min(var11))/13 + min(var11), u"min humidex = %f"%(min(humidex1[s1:e1+1])), fontsize=7)
        ax11.text(start_date, 6*(max(var11)-min(var11))/13 + min(var11), u"max humidex = %f"%(max(humidex1[s1:e1+1])), fontsize=7)
        ax11.text(start_date, 5*(max(var11)-min(var11))/13 + min(var11), u"moy humidex = %f"%(moyenne(humidex1[s1:e1+1])), fontsize=7)
        ax11.text(start_date, 4*(max(var11)-min(var11))/13 + min(var11), u"med humidex = %f"%(mediane(humidex1[s1:e1+1])), fontsize=7)
        ax11.text(start_date, 3*(max(var11)-min(var11))/13 + min(var11), u"EcTyp humidex = %f"%(ecartType(humidex1[s1:e1+1])), fontsize=7)
        plt.text(start_date, (max(var11)-min(var11))/13 + min(var11), u"coef corr = %f"%coefCorr(var11[s1:e1+1],var21[s1:e1+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax22.plot(sent_at2, humidex2, label='humidex 2', color = 'tab:green')
        ax22.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at2)) != 0 :
            ax22.plot(sent_at2[anom(sent_at2)[0]:anom(sent_at2)[-1]+2], humidex2[anom(sent_at2)[0]:anom(sent_at2)[-1]+2], color = 'tab:red')
        ax12.text(start_date, 7*(max(var12)-min(var12))/13 + min(var12), u"min humidex = %f"%(min(humidex2[s2:e2+1])), fontsize=7)
        ax12.text(start_date, 6*(max(var12)-min(var12))/13 + min(var12), u"max humidex = %f"%(max(humidex2[s2:e2+1])), fontsize=7)
        ax12.text(start_date, 5*(max(var12)-min(var12))/13 + min(var12), u"moy humidex = %f"%(moyenne(humidex2[s2:e2+1])), fontsize=7)
        ax12.text(start_date, 4*(max(var12)-min(var12))/13 + min(var12), u"med humidex = %f"%(mediane(humidex2[s2:e2+1])), fontsize=7)
        ax12.text(start_date, 3*(max(var12)-min(var12))/13 + min(var12), u"EcTyp humidex = %f"%(ecartType(humidex2[s2:e2+1])), fontsize=7)
        ax12.text(start_date, (max(var12)-min(var12))/13 + min(var12), u"coef corr = %f"%coefCorr(var12[s2:e2+1],var22[s2:e2+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax23.plot(sent_at3, humidex3, label='humidex 3', color = 'tab:green')
        ax23.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at3)) != 0 :
            ax23.plot(sent_at3[anom(sent_at3)[0]:anom(sent_at3)[-1]+2], humidex3[anom(sent_at3)[0]:anom(sent_at3)[-1]+2], color = 'tab:red')
        ax13.text(start_date, 7*(max(var13)-min(var13))/13 + min(var13), u"min humidex = %f"%(min(humidex3[s3:e3+1])), fontsize=7)
        ax13.text(start_date, 6*(max(var13)-min(var13))/13 + min(var13), u"max humidex = %f"%(max(humidex3[s3:e3+1])), fontsize=7)
        ax13.text(start_date, 5*(max(var13)-min(var13))/13 + min(var13), u"moy humidex = %f"%(moyenne(humidex3[s3:e3+1])), fontsize=7)
        ax13.text(start_date, 4*(max(var13)-min(var13))/13 + min(var13), u"med humidex = %f"%(mediane(humidex3[s3:e3+1])), fontsize=7)
        ax13.text(start_date, 3*(max(var13)-min(var13))/13 + min(var13), u"EcTyp humidex = %f"%(ecartType(humidex3[s3:e3+1])), fontsize=7)
        ax13.text(start_date, (max(var13)-min(var13))/13 + min(var13), u"coef corr = %f"%coefCorr(var13[s3:e3+1],var23[s3:e3+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax24.plot(sent_at4, humidex4, label='humidex 4', color = 'tab:green')
        ax24.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at4)) != 0 :
            ax24.plot(sent_at4[anom(sent_at4)[0]:anom(sent_at4)[-1]+2], humidex4[anom(sent_at4)[0]:anom(sent_at4)[-1]+2], color = 'tab:red')
        ax14.text(start_date, 7*(max(var14)-min(var14))/13 + min(var14), u"min humidex = %f"%(min(humidex4[s4:e4+1])), fontsize=7)
        ax14.text(start_date, 6*(max(var14)-min(var14))/13 + min(var14), u"max humidex = %f"%(max(humidex4[s4:e4+1])), fontsize=7)
        ax14.text(start_date, 5*(max(var14)-min(var14))/13 + min(var14), u"moy humidex = %f"%(moyenne(humidex4[s4:e4+1])), fontsize=7)
        ax14.text(start_date, 4*(max(var14)-min(var14))/13 + min(var14), u"med humidex = %f"%(mediane(humidex4[s4:e4+1])), fontsize=7)
        ax14.text(start_date, 3*(max(var14)-min(var14))/13 + min(var14), u"EcTyp humidex = %f"%(ecartType(humidex4[s4:e4+1])), fontsize=7)
        ax14.text(start_date, (max(var14)-min(var14))/13 + min(var14), u"coef corr = %f"%coefCorr(var14[s4:e4+1],var24[s4:e4+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax25.plot(sent_at5, humidex5, label='humidex 5', color = 'tab:green')
        ax25.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at5)) != 0 :
            ax25.plot(sent_at5[anom(sent_at5)[0]:anom(sent_at5)[-1]+2], humidex5[anom(sent_at5)[0]:anom(sent_at5)[-1]+2], color = 'tab:red')
        ax15.text(start_date, 7*(max(var15)-min(var15))/13 + min(var15), u"min humidex = %f"%(min(humidex5[s5:e5+1])), fontsize=7)
        ax15.text(start_date, 6*(max(var15)-min(var15))/13 + min(var15), u"max humidex = %f"%(max(humidex5[s5:e5+1])), fontsize=7)
        ax15.text(start_date, 5*(max(var15)-min(var15))/13 + min(var15), u"moy humidex = %f"%(moyenne(humidex5[s5:e5+1])), fontsize=7)
        ax15.text(start_date, 4*(max(var15)-min(var15))/13 + min(var15), u"med humidex = %f"%(mediane(humidex5[s5:e5+1])), fontsize=7)
        ax15.text(start_date, 3*(max(var15)-min(var15))/13 + min(var15), u"EcTyp humidex = %f"%(ecartType(humidex5[s5:e5+1])), fontsize=7)
        ax15.text(start_date, (max(var15)-min(var15))/13 + min(var15), u"coef corr = %f"%coefCorr(var15[s5:e5+1],var25[s5:e5+1]), fontsize=7)
        plt.xlim(start_date,end_date)
        ax26.plot(sent_at6, humidex6, label='humidex 6', color = 'tab:green')
        ax26.tick_params(axis='y', labelcolor = 'tab:green')
        if len(anom(sent_at6)) != 0 :
            ax26.plot(sent_at6[anom(sent_at6)[0]:anom(sent_at6)[-1]+2], humidex6[anom(sent_at6)[0]:anom(sent_at6)[-1]+2], color = 'tab:red')
        ax16.text(start_date, 7*(max(var16)-min(var16))/13 + min(var16), u"min humidex = %f"%(min(humidex6[s6:e6+1])), fontsize=7)
        ax16.text(start_date, 6*(max(var16)-min(var16))/13 + min(var16), u"max humidex = %f"%(moyenne(humidex6[s6:e6+1])), fontsize=7)
        ax16.text(start_date, 5*(max(var16)-min(var16))/13 + min(var16), u"moy humidex = %f"%(moyenne(humidex6[s6:e6+1])), fontsize=7)
        ax16.text(start_date, 4*(max(var16)-min(var16))/13 + min(var16), u"med humidex = %f"%(mediane(humidex6[s6:e6+1])), fontsize=7)
        ax16.text(start_date, 3*(max(var16)-min(var16))/13 + min(var16), u"EcTyp humidex = %f"%(ecartType(humidex6[s6:e6+1])), fontsize=7)
        ax16.text(start_date, (max(var16)-min(var16))/13 + min(var16), u"coef corr = %f"%coefCorr(var16[s6:e6+1],var26[s6:e6+1]), fontsize=7)
        plt.xlim(start_date,end_date)
    else :
        print ("erreur d'entrée de variable2")

if variable2 != None:
    print(u"capteur 1 : coefficient de corrélation = %f"%coefCorr(var11[s1:e1+1],var21[s1:e1+1]))
    print(u"capteur 2 : coefficient de corrélation = %f"%coefCorr(var12[s2:e2+1],var22[s2:e2+1]))
    print(u"capteur 3 : coefficient de corrélation = %f"%coefCorr(var13[s3:e3+1],var23[s3:e3+1]))
    print(u"capteur 4 : coefficient de corrélation = %f"%coefCorr(var14[s4:e4+1],var24[s4:e4+1]))
    print(u"capteur 5 : coefficient de corrélation = %f"%coefCorr(var15[s5:e5+1],var25[s5:e5+1]))
    print(u"capteur 6 : coefficient de corrélation = %f"%coefCorr(var16[s6:e6+1],var26[s6:e6+1]))

plt.show()