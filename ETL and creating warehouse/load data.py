# -*- coding: utf8 -*-
from random import randint
from datetime import datetime
import pyodbc
import csv
import faker
from faker import Faker
import pandas as pd

drivers_list = ['''Driver da Microsoft para arquivos texto (*.txt; *.csv)
Driver do Microsoft Access (*.mdb)
Driver do Microsoft dBase (*.dbf)
Driver do Microsoft Excel(*.xls)
Driver do Microsoft Paradox (*.db )
Microsoft Access Driver (*.mdb)
Microsoft Access-Treiber (*.mdb)
Microsoft dBase Driver (*.dbf)
Microsoft dBase-Treiber (*.dbf)
Microsoft Excel Driver (*.xls)
Microsoft Excel-Treiber (*.xls)
Microsoft ODBC for Oracle
Microsoft Paradox Driver (*.db )
Microsoft Paradox-Treiber (*.db )
Microsoft Text Driver (*.txt; *.csv)
Microsoft Text-Treiber (*.txt; *.csv)
SQL Server
Microsoft Access Driver (*.mdb, *.accdb)
Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)
Microsoft Access Text Driver (*.txt, *.csv)
SQL Server Native Client 11.0
ODBC Driver 17 for SQL Server''']
fake = Faker()

# presidents = []
# ids = set()
# while len(ids)<1000:
#     ids.add(randint(10000000,99999999))
# ids = list(ids)
#
#
conn : pyodbc.Connection = pyodbc.connect(
	"Driver={SQL Server Native Client 11.0};"
	" Server=BUHAIROMKA; "
	"Database=GameSales;"
	" Trusted_Connection=yes;",
	autocommit=True
)
# with conn.cursor() as cu:
#     print(list(map(lambda x:x[3] ,cu.columns(table='PresidentDim'))))
#
# '''loading president dim'''
#
# with conn.cursor() as cu:
#     with open('publisher_presidents.csv','r', encoding='utf-8') as fpres:
#         readed_file = csv.reader(fpres)
#         next(readed_file)
#         for row in readed_file:
#             row.append(str(ids.pop(0)))
#             del row[3]
#             print(row)
#             cu.execute('''insert into PresidentDim ( Name, SecondName, Birthday, Sex, UniqueID ) values (?,?,?,?,?)''',row)
#             conn.commit()
#             print('ок')
# print('Publishers - ok')
#
# '''loading publisher dim'''
# ids = set()
# while len(ids)<1000:
#     ids.add(randint(10000000,99999999))
# ids=list(ids)
#
#
# with open('updated_without_NA1.csv','r',encoding='utf-8') as f:
#     file = list(csv.reader(f))
#     file.pop(0)
# print(file[0])
#
# def min_date_of_publisher(publisher):
#     minpub=99999
#     minpub=min(list(map(lambda x : int(x[3]) if publisher == x[5] else 99999,file)))
#     if minpub == 99999:
#         raise Exception('Publisher does not exists')
#     else:
#         print(publisher,'ok')
#         return minpub
#
#
# with open('publisher_presidents.csv','r', encoding='utf-8') as fpres:
#     readed_file = csv.reader(fpres)
#     next(readed_file)
#     with conn.cursor() as fpubl:
#         for row in readed_file:
#             m=min_date_of_publisher(row[3])
#             fpubl.execute('insert into PublisherDim (UniqueID,PublisherName,FoundationDate,OfficeCountry,PresidentID) values(?,?,?,?, (select PresidentID from PresidentDim where Name=? and SecondName=?) )',[ids.pop(0),row[3],datetime(year=randint(m-15,m-1),month=randint(1,12),day=randint(1,28)),fake.country(),row[0],row[1]])
# print('Publishers - ok')
#
# '''Loading Platform dim'''
# ids = set()
# while len(ids)<1000:
#     ids.add(randint(10000000,99999999))
# ids=list(ids)
# print(fake.bothify(text='?###-##?-##%%'))
# platforms = (pd.read_csv('updated_without_NA1.csv')['Platform'].unique())
# with conn.cursor() as cu:
#     for pl in platforms:
#         cu.execute('insert into PlatformDim (UniqueID, NamePlatform, Model) values(?,?,?)',[ids.pop(0),pl,fake.bothify(text='?###-##?-##%%')])
#
#
# '''Loading Rank dim'''
#
# with conn.cursor() as cu:
#     for v in range(20000):
#         cu.execute('insert into RankDim (Value) values(?)',v)
#
# ''' Loading GenreDim'''
# ids = set()
# while len(ids)<1000:
#     ids.add(randint(10000000,99999999))
# ids=list(ids)
# genres = pd.read_csv('updated_without_NA1.csv')['Genre'].unique()
# print(genres)
#
# with conn.cursor() as cu:
#     for genre in genres:
#         cu.execute('insert into GenreDim (UniqueID, NameGenre, Description) values(?,?,?)', [ids.pop(0), genre, fake.paragraph(nb_sentences=5, variable_nb_sentences=False)])
#
#
# '''loading DateDim'''
# with open('updated_without_NA1.csv','r',encoding='utf-8') as f:
#     file = list(map(lambda x : x[3],csv.reader(f)))
#     file.pop(0)
#     file = list(map(lambda x : int(x),file))
# print(max(file),min(file))
#
# datesset = []
# for y in range(1970,2026,1):
#     for m in range(1,13,1):
#         datesset.append([y,m])
# with conn.cursor() as cu:
#     for date in datesset:
#         cu.execute('insert into DateDim (Year, Month) values(?,?)', date[0],date[1])
#
# '''loading fact table'''
# ['ID', 'RankID', 'GameName', 'PlatformID', 'DateID', 'GenreID', 'PublisherID', 'NA_Sales', 'EU_Sales', 'JP_Sales',
#  'Other_Sales', 'Global_Sales']
# newfile = open('final_version.csv','w',encoding='utf-8',newline='')
# newfilecsv = csv.writer(newfile)
#
# with open('updated_without_NA1.csv', 'r', encoding='utf-8') as t:
#     file = list(csv.reader(t))
#     head = (file.pop(0))
#     head.insert(4,'Month')
#     newfilecsv.writerow(head)
#     print(head)
# print(file[0])
#
# def mill(value):
#     return (int(float(value) * 1000000))
#
# with conn.cursor() as fact:
#
#     for row in file:
#         month = randint(1, 12)
#         fact.execute(
# 			'insert into FactTable (RankID,GameName,PlatformID,DateID,GenreID,PublisherID,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales) '
# 			'values( (select RankID from RankDim where Value =?), ? , (select PlatformID from PlatformDim where NamePlatform =?) , (select DateID from DateDim where Year = ? and Month = ?) , (select GenreID from GenreDim where NameGenre = ?), (select PublisherID from PublisherDim where PublisherName = ?), ?, ?, ?, ?, ?)',
# 			row[0], row[1], row[2], int(row[3]), month, row[4], row[5],      mill(row[6]), mill(row[7]), mill(row[8]), mill(row[9]), mill(row[10]))
#         row.insert(4,month)
#         newfilecsv.writerow(row)
# newfile.close()
# print('fact table loaded')
#
#
#
# with open('publisher_presidents.csv','r', encoding='utf-8') as fpres:
#     readed_file = csv.reader(fpres)
#     next(readed_file)
#     with conn.cursor() as fpubl:
#         for row in readed_file:
#             m=min_date_of_publisher(row[3])
#             fpubl.execute('insert into PublisherDim (UniqueID,PublisherName,FoundationDate,OfficeCountry,PresidentID) values(?,?,?,?, (select PresidentID from PresidentDim where Name=? and SecondName=?) )',[ids.pop(0),row[3],datetime(year=randint(m-15,m-1),month=randint(1,12),day=randint(1,28)),fake.country(),row[0],row[1]])
#
# print(str(datetime.now()))

def SCD_GenreDim_change_descr(descrip,name, conn:pyodbc.Connection=conn):
    with conn.cursor() as cu:
        if descrip and name:
            cu.execute(
				''' UPDATE GenreDim
					set valid_to = ?
					WHERE NameGenre = ? and valid_to is NULL;
					insert into GenreDim (UniqueID,Description,valid_from, NameGenre)
				 	values ((select distinct (UniqueID) from GenreDim where NameGenre = ?),?,?,?);
					
				''',datetime.now(),
					name,name,descrip,datetime.now(),name,
					)

SCD_GenreDim_change_descr('lorem ipsum 111111', 'Action')
SCD_GenreDim_change_descr('lorem ipsum 222222', 'Action')
SCD_GenreDim_change_descr('nice genre', 'Action')


