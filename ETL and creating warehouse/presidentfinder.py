import random

from faker import Faker
import csv

fake = Faker()
names = []
dates=[]

for _ in range(577):
	while True:
		try:
			dateee=fake.date_between(start_date='-70y',end_date='-24y')
			dates.append(dateee)
			break
		except OSError:
			pass
dates = (list(map(str,dates)))


while len(names) < 577:
	name = fake.name()
	if len(name.split()) == 2:
		if name not in names:
			names.append(name)
print(names,len(names))


publishers = []
file_root = 'updated_without_NA1.csv'
with open (file_root, 'r', encoding='utf-8') as csvfile:
	f = csv.reader(csvfile)
	next(f)
	for row in f:
		if row[5] not in publishers:
			publishers.append(row[5])
print(publishers)
print(len(dates),len(names),len(publishers))
result_table=[]
for i in range(577):
	result_table.append([names[i].split()[0],names[i].split()[1],dates[i],publishers[i],random.choice(['m','f'])])

for i in result_table:
	print(i)





file_root = 'publisher_presidents.csv'
with open (file_root, 'w', encoding='utf-8', newline='') as csvfile:
	f = csv.writer(csvfile)
	f.writerow(['Name','SecondName','BirthDate','Company','Sex'])
	f.writerows(result_table)



