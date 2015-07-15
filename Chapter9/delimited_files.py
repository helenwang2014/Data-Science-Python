

import csv

with open("NYSEACN.txt", 'r') as f:
	reader = csv.reader(f, dialect=csv.excel_tab)
	for row in reader:
		print now
		date = row[0]
		closing_price = float(row[1])
		process(date, closing_price)


'''
# if file has headers:
with open('colon_delimited_stock_prices.txt', 'rb') as f:
	reader = csv.DictReader(f, delimiter=':')
	for row in reader:
		date = row["data"]
		clsoing_price
		process(data, closing_price)

'''