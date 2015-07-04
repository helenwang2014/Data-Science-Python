"""
x = [3,4,1,2]
y = sorted(x)
x.sort()

print x


x = sorted([-4,2,3,-1], key=abs, reverse = True)

print x



wc = sorted(word_counts.items(),
	key = lambda (word,count): count,
	reverse = True)



even_numbers = [x for x in range(5) if x % 2 == 0]
squares = [x * x for x in range(5)]
even_squares = [x * x for x in even_numbers]

print even_numbers, squares, even_squares



square_dict = {x:x*x for x in range(5)}
print square_dict
square_set = {x * x for x in [-1, 1]}
print square_set



even_numbers = [x for x in range(5) if x % 2 == 0]
zeros = [0 for _ in even_numbers]
print zeros
"""

pairs = [(x,y)

		for x in range(10)
		for y in range(10)
		]
a = len(pairs)

print pairs
print a


increasing_pairs = [(x,y)
					for x in range(10)
					for y in range(x+1,10)]

a = len(increasing_pairs)
print a 
print increasing_pairs

