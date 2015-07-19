

def parse_rows_with(reader, parsers):
	# wrap a reader to apply the parsers to each of its rows  
	for row in reader:
		yield parse_row(row, parsers)


def try_or_none(f):
	# wraps f to return None if f raises an exception
	# assumes f takes only one input

	def f_or_none(x):
		try: return f(x)
	 	except: return None
	return f_or_none

def parse_row(input_row, parsers):
	return [try_or_none(parser)(value) if parser is not None else value
			for value, parser in zip(input_row, parsers)]

# ============================================

import dateutil.parser
import csv

data = []

with open("comma_delimited_stock_price.csv", "rU") as f:
	reader = csv.reader(f)
	for line in parse_rows_with(reader, [dateutil.parser.parse, None, float]):
		data.append(line)

for row in data:
	if any(x is None for x in row):
		print row

def try_parse_field(field_name, value, parser_dict):
	# try to parse value using the appropriate function from parser_dict
	parser = parser_dict.get(field_name)
	if parser is not None:
		return try_or_none(parser)(value)
	else:
		return value

def parse_dict(input_dict, parser_dict):
	return {field_name : try_parse_field(field_name, value, parser_dict)
			for field_name, value in input_dict.iteritems()}


import datetime
from collections import defaultdict

'''
data = [
		{'closing_price': 102.06,
		'date': datetime.datetime(2014, 8, 29, 0, 0),
		'symbol': 'AAPL'}, 
		#...
		]
'''
max_aapl_price = max(row["closing_price"]
					 for row in data
					 	if row["symbol"] == "AAPL")

# find the highest-ever closing price for each stock in our data set
# group rows by symbol
by_symbol = defaultdict(list)
for row in data: 
	by_symbol[row["symbol"]].append(row)

# use a dict comprehension to find the max for each symbol
max_price_by_symbol = {symbol : max(row["closing_price"]
									for row in grouped_rows)
						for symbol, grouped_rows in by_symbol.iteritems()}

def picker(field_name):
	# returns a function that picks a field out of a dict
	return lambda row: row[field_name]

def pluck(field_name, rows):
	# turn a list of dicts into the list of field_name values
	return map(picker(field_name), rows)


def group_by(grouper, rows, value_transform=None):
	# key is output of grouper, value is list of rows
	grouped = defaultdict(list)
	for row in rows:
		grouped[grouper(row)].append(row)

	if value_transform is None:
		return grouped
	else:
		return {key : value_transform(rows)
				for key, rows in grouped.iteritems() }

# rewrite the above examples quite simply. 
max_price_by_symbol = group_by(picker("symbol"), 
								data, 
								lambda rows: max(pluck("closing_price", rows)))


def percent_price_change(yesterday, today):
	return today["closing_price"] / yesterday["closing_price"] - 1

def day_over_day_changes(grouped_rows):
	# sort the rows by date
	ordered = sorted(grouped_rows, key=picker("date"))

	# zip with an offset to get pairs of consecutive days
	return [{"symbol" : today["symbol"], 
			"date": today["date"], 
			"change": percent_price_change(yesterday, today)}
			for yesterday, today in zip(ordered, ordered[1:])]

	# use this as the value_tranform in a group_by
	# key is symbol, value is list of "change" dicts
changes_by_symbol = group_by(picker("symbol"), data, day_over_day_changes)

	# collect all "change" into one big list
all_changes = [change for changes in changes_by_symbol.values() for change in changes]
print all_changes
print picker("change")
max(all_changes, key=picker("change"))

min(all_changes, key=picker("change"))


def combine_pct_changes(pct_change1, pct_change2): 
	return (1 + pct_change1) * (1 + pct_change2) - 1

def overall_change(changes):
	return reduce(combine_pct_changes, pluck("change", changes))

overall_change_by_month = group_by(lambda row: row['date'].month, 
									all_changes, 
									overall_change)






