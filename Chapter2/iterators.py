"""

def lazy_range(n):
	i = 0
	while i < n:
		yield i
		i += 1




def natural_numbers():
	n = 1
	while True:
		yield n 
		n += 1

print natural_numbers()


lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)

print "lazy_evens" % lazy_evens_below_20


"""

import random

four_uniform_randoms = [random.random() for _ in range(4)]

print four_uniform_randoms 


random.seed(10)
print random.random()
random.seed(10)
print random.random()

random.seed(1)
print random.random()

print random.randrange(10)
print random.randrange(3,6)


up_to_ten = range(10)
random.shuffle(up_to_ten)
print up_to_ten

print random.choice(up_to_ten)



lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)
print winning_numbers


import random
four_with_replacement = [random.choice(range(10))
						 for _ in range(4)]

print four_with_replacement





