# from matplotlib import pyplot as plt
#
#
# humidex = T + h
# h = #humidité relative en pourcentage
#
# plt.plot()
# plt.show()

# import xlrd
#
# document = xlrd.open_workbook(r'''C:\\Users\\aachi\\Desktop\\projet_algo\\EIVP_KM.csv''')
#
# print("Nombre de feuilles: "+str(document.nsheets))
# print("Noms des feuilles: "+str(document.sheet_names()))

path="C:\\Users\\aachi\\Desktop\\projet_algo\\EIVP_KM.csv"
import csv
objetFichier=open(path,'rb')
objetcsv=csv.writer(objetFichier,delimiter=';')
print (objetcsv)

# lst=[]
# for row in objetcsv:
#     lst.append(row)
# lst = list(objetcsv)
test
