import csv
import datetime
with open('Инструкции.csv', encoding='utf-8') as file:
	file_reader = csv.reader(file, delimiter=';')
	not_first = False
	nw = datetime.datetime.now() + datetime.timedelta(days=30)
	for row in file_reader:
		if not_first:
			dt = datetime.datetime.strptime(row[4], '%d.%m.%Y')
			if dt < nw:
				print(row[2],'\t\t',row[0], '\t\t', row[4])
		not_first = True
input('Нажмите клавишу "ввод":')
