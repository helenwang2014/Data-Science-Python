v = [1,2]
w = [2,1]

def vector_add(v,w):
	return [v_i + w_i for v_i, w_i in zip(v, w)]

h = vector_add(v,w)
print h

def vector_subtract(v,w):

	return [v_i - w_i
			for v_i, w_i in zip(v,w)]

g = vector_subtract(v,w)
print g

'''
vectors = [4,3,4]
def vector_sum(vectors):
	result = vectors[0]
	for vector in vectors[1:]:
		result = vector_add(result, vector)
	return result


'''

def vector_sum(vectors):
	return reduce(vector_add, vectors)

vector_sum = partial(reduce, vector_add)


def scalar_multiply(c,v):
	return [c * v_i for v_i in v]

def vector_mean(vectors):
	'''compute the vector whose ith element is the mean of the ith elements
	of the input vectors'''

	n = len(vectors)
	return scalar_multiply(1/n, vector_sum(vectors))


def dot(v,w):
	return sum(v_i * w_i
				for v_i, w_i in zip(v,w))



def sum_of_squares(v):
	return dot(v,v)

import math
def magintude(v):
	return math.sqrt(sum_of_squares(v))


def squared_distance(v,w):
	return sum_of_squares(vector_subtract(v,w))


def distance(v,w):
	return math.sqrt(squared_distance(v,w))

def distance(v,w):
	return magnitude(vector_subtract(v,w))


	
