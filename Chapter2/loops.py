'''
if 1 > 2:
	message = "if only 1 were greater than two..."
else 1 > 3:
	message = "elif stands for 'else if'"
else:
	message = "when all else falls use else(if you want to)"

'''

"""
for x in range(10):
	print x, "is less than 10"
	x += 1



"""

for x in range(10):
	if x ==3:
		continue 
	if x ==5:
		break
	print x 


"""
s = some_function_that_returns_a_string()
if s:
	first_char = s[0]
else:
	first_char = ""

first_char = s and s[0]

