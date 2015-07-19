import math
from scipy import spatial
from numpy import dot

a_to_b = spatial.distance.euclidean([63, 150], [67, 160])
a_to_c = spatial.distance.euclidean([63, 150], [70, 160])
b_to_c =spatial.distance.euclidean([67, 160], [70, 171])


print a_to_b
print a_to_c
print b_to_c

def make_matrix(num_rows, num_cols, entry_fn):
    """returns a num_rows x num_cols matrix 
    whose (i,j)-th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j) for j in range(num_cols)]
            for i in range(num_rows)]  
def mean(x):
	return sum(x) / len(x)

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)
    
def standard_deviation(x):
    return math.sqrt(variance(x))

def get_row(A, i):
    return A[i]
    
def get_column(A, j):
    return [A_i[j] for A_i in A]

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def scale(data_matrix):
	# returns the means and standard deviation of each column
	num_rows, num_cols = shape(data_matrix)

	means = [mean(get_column(data_matrix, j))
			for j in range(num_cols)]
	stdevs = [standard_deviation(get_column(data_matrix, j))
				for j in range(num_cols)]
	return means, stdevs

def rescale(data_matrix):
	# rescales the input data so that each column has 
	# mean 0 and standard deviation
	# leaves alone columns with no deviation

	means, stdevs = scale(data_matrix)

	def rescaled(i, j):
		if stdevs[j] > 0:
			return (data_matrix[i][j] - means[j]) / stdevs[j]
		else:
			return data_matrix[i][j]

	num_rows, num_cols = shape(data_matrix)
	return make_matrix(num_rows, num_cols, rescaled)


print scale([[63,23],[3,4], [87,35], [43,34], [32, 14]])


