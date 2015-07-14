#iterate through our data in a random order

def in_random_order(data):
	#generator that returns the elements of data in random order
	indexes = [i for i, _ in enumerate(data)]
	random.shuffle(indexes) 
	for i in indexes: 
		yield data[i]


def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0 = 0.01):

	data = zip(x,y)
	theta = theta_0
	alpha = alpha_0
	min_theta, min_value = None, float('inf')
	iterations_with_no_improvement = 0

	# if we ever go 100 iterations with no improvement, stop
	while iterations_with_no_improvement< 100:
		value = sum(target_fn(x_i,y_i,theta) for x_i, y_i in data)

		if value < min_value:
			#if we've found a new minimum, remember it 
			#and go back to the original step size
			min_theta, min_value = theta, value
			iterations_with_no_improvement = 0
			alpha = alpha_0

		else:
			#otherwise we are not improving, so try shrinking the step size
			iterations_with_no_improvement += 1
			alpha *= 0.9
		# and take a gradient step for each of the data points
		for x_i, y_i in in_random_order(data):
			gradient_i = gradient_fn(x_i, y_i, theta)
			theta = vector_subtract(theta, scalar_multiply(alpha, gradient_i))
		return min_theta


#maximize version
def maximize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0 = 0.01):
	return minimize_stochastic(negate(target_fn),
		negate_all(gradient_fn), 
		x,y, theta_0, alpha_0)


	