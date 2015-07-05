list1 = ['a', 'b', 'c']
list2 = [1,2,3]

print zip(list1,list2)



pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)

print letters, numbers


def add(a, b):
	return a + b

print add(1,2)
#print add[(1,2)]
print add (*[1,2])





def doubler(f):
	def g(x):
		return 2 * f(x)

	return g

def f1(x):
	return x + 1

g = doubler(f1)
print g(3)
print g(-1)

def magic(*args, **kwargs):
	print "unnamed args:", args
	print "keyword args:", kwargs

magic(1, 2, key="word", key2="word2")


def other_way(x,y,z):
	return x+y+z

x_y_list = [1,2]
z_dict = {"z" : 3}
print other_way(*x_y_list, **z_dict)



def doubler_correct(f):
	def g(*args, **kwargs):
		return 2 * f(*args, **kwargs)
	return g

g = doubler_correct(f)
print g(1,2)





