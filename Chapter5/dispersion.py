import math


num_friends = [100,49,41,40,25, 34,4,3,2,1,1,7,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]



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

print variance(num_friends)



def standard_deviation(x):
	return math.sqrt(x)

print standard_deviation(variance(num_friends))


def quantile(x, p):
	p_index = int(p * len(x))
	return sorted(x)[p_index]

def interquartile_range(x):
	return quantile(x, 0.75) - quantile(x, 0.25)

print interquartile_range(num_friends)

