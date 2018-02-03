'''
Created on 29.10.2017

@author: info_000
'''
import pandas as pd
from datetime import timedelta,date,datetime

#woche =input('woche?')
woche=('\kw36_17')
#Pfad der Unigraph asc Datei
pfad='D:'+r'\VIH'+r'\unigraphII'+r'\Daten'+r'\Hauptstr west'
file=(pfad+str(woche)+'.asc')
#Ausgabepfad
apfad='D:'+r'\VIH'+r'\uni'
adatei=apfad+str(woche)+'.xls'

dat=pd.read_csv(file,header=None,delimiter=';',sep=" ", names=["Datum", "null","V","L","R"])

#get date time format
dat.Datum = [datetime.strptime(i,"%d.%m.%y %H:%M:%S") for i in dat.Datum]   

#get only the date (no time information)
dates= [datum.date() for datum in dat.Datum]

#use set() to obtain a unique list of dates
uniqueDates = list(set(dates))
uniqueDates.sort()
countsAndDays      = [[ud.strftime("%A"),dates.count(ud)] for ud in uniqueDates]
#create new DataFrame
carsPerDateDF = pd.DataFrame(data = countsAndDays,columns = ["WochenTag","DTV",],index = uniqueDates)

#writer = pd.ExcelWriter(adatei)
carsPerDateDF.to_excel(adatei)
#writer.save()
#writer.close()
