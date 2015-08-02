import math
import numpy

num_friends = [100.0,49,41,40,25,34,4, 3, 2, 1, 1, 7,  7,  8,  8]

daily_minutes =[60,34,3,42,23,36,15,47,49,45,23,32, 34, 67, 89 ]


outlier = num_friends.index(100)
num_friends_good = [x for i, x in enumerate(num_friends)]
daily_minutes_good = [x for i, x in enumerate(daily_minutes)if i != outlier]

def data_range(x):
	return max(x) - min(x)

print data_range(num_friends)

def mean(x):
	return sum(x)/len(x)


def de_mean(x):
	x_bar = mean(x)
	return [(x_i - x_bar) ** 2 for x_i in x]


def variance(x):
	n = len(x)
	deviations = de_mean(x)
	return sum(deviations) / (n - 1)

print "variance is: ", variance(num_friends)



def standard_deviation(x):
	return math.sqrt(variance(x))



def quantile(x, p):
	p_index = int(p * len(x))
	return sorted(x)[p_index]

def interquartile_range(x):
	return quantile(x, 0.75) - quantile(x, 0.25)

print interquartile_range(num_friends)


def covariance(x, y):
	n = len(x)
	return numpy.dot(de_mean(x), de_mean(y))/(n - 1)



def correlation(x, y):
	stdev_x = standard_deviation(x)
	stdev_y = standard_deviation(y)
	if stdev_x >0 and stdev_y > 0:
		return (covariance(x, y)/stdev_x/stdev_y)
	else:
		return 0 




def predict(alpha, beta, x_i):
	return beta * x_i + alpha

def error(alpha, beta, x_i, y_i):
	return y_i - predict(alpha, beta, x_i)

def sum_of_squared_errors(alpha, beta, x, y):
	return sum(error(alpha, beta, x_i, y_i) ** 2
		       for x_i, y_i in zip(x, y))

# the least squares solution is to choose the alpha and beta that make sum_of_squared_errors as small as possible

# using calculus (or algebra), the error-minimizing alpha and beta are given by:

def least_squares_fit(x, y):
	# given training values for x and y, 
	# find the least-squares values of alpha and beta

	beta = correlation(x, y) * standard_deviation(y) / standard_deviation(x)
	alpha = mean(y) - beta * mean(x) 
	return alpha, beta

alpha, beta = least_squares_fit(num_friends_good, daily_minutes_good)


# a common measure is the coefficient of determination (or R-squared), 
# which measures the fraction of the total variation in the dependent variable
# that is captured by the model
def total_sum_of_squares(y):
	# the total squared variation of y_i's from their mean

	return sum(v ** 2 for v in de_mean(y))

def r_squared(alpha, beta, x, y):
	# the fraction of variation in y captured by the model, which equals 
	# 1 - the fraction of variation in y not captured by the model 
	return 1.0 - (sum_of_squared_errors(alpha, beta, x, y)/
				total_sum_of_squares(y))

r_squared(alpha, beta, num_friends_good, daily_minutes_good)




# ========
# using Gradient Descent
def squared_error(x_i, y_i, theta):
	alpha, beta = theta
	return error(alpha, beta, x_i, y_i) ** 2

def squared_error_gradient(x_i, y_i, theta):
	alpha, beta = theta
	return [-2 * error(alpha, beta, x_i, y_i), 
	 		-2 * error(alpha, beta, x_i, y_i) * x_i]

# choose random value to start
random.seed(0)
theta = [random.random(), random.random()]
alpha, beta = minimize_stochastic(squared_error, 
								  squared_error_gradient, 
								  num_friends_good, 
								  daily_minutes_good,
								  theta, 
								  0.0001)
print alpha, beta





