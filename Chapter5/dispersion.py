import math
import numpy

num_friends = [100,49,41,40,25,34,4, 3, 2, 1, 1, 7,  7,  8,  8]

daily_minutes =[60,34,3,42,23,36,15,47,49,45,23,32, 34, 67, 89 ]

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
	return math.sqrt(x)

print "standard deviation is: ", standard_deviation(variance(num_friends))



def quantile(x, p):
	p_index = int(p * len(x))
	return sorted(x)[p_index]

def interquartile_range(x):
	return quantile(x, 0.75) - quantile(x, 0.25)

print interquartile_range(num_friends)


def covariance(x, y):
	n = len(x)
	return numpy.dot(de_mean(x), de_mean(y))/(n - 1)

print "covariance is: ", covariance(num_friends, daily_minutes)


def correlation(x, y):
	stdev_x = standard_deviation(x)
	stdev_y = standard_deviation(y)
	if stdev_x >0 and stdev_y > 0:
		return (covariance(x, y)/stdev_x/stdev_y)
	else:
		return 0 
print "correlation is: ", correlation(num_friends, daily_minutes)



# Correlation with an outlier
outlier = num_friends.index(100)
num_friends_good = [x for i, x in enumerate(num_friends)
					if i != outlier]

daily_minutes_good = [x for i, x in enumerate(daily_minutes) 
					  if i != outlier]

correlation(num_friends_good, daily_minutes_good)



