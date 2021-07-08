import requests as req
from bs4 import BeautifulSoup as bs
import csv

list=[]
result_list=[]
unknown=[]
unknown_result_list=[]
file_root = 'D:\kpi\\4 семестр\AD\\videogamessales\\vgsales.csv'
counteroflines=0

with open (file_root, 'r', encoding='utf-8') as csvfile:
	for row in csv.reader(csvfile):
		if row[3]=='N/A':
			unknown.append([counteroflines,row[1]])
		counteroflines+=1
	
print("start finding dates-----------------------------------------")

for game in list:
	url='https://www.google.com/search?q=дата выпуска ' + game[1] + ' ' + game[2]
	print('\'',url,'\'')
	resp = req.get(url)
	soup = bs(resp.text,'lxml')
	print(soup)
	res=soup.find_all('div',{"class": "BNeawe"})[0].text
	result_list.append([game[1],res])
	print(res)

for game in unknown:
	url = 'https://www.google.com/search?q=release date ' + game[1]
	print('\'', url, '\'')
	resp = req.get(url)
	soup = bs(resp.text, 'lxml')
	print(soup)
	res = soup.find_all('div', {"class": "BNeawe"})[0].text
	unknown_result_list.append([game[1], res])
	print(res)

print('UNKNOWN result list----------------------------------------------------------')
print(unknown_result_list)