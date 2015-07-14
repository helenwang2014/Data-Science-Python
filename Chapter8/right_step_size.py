'''
using a fixed step size
Gradually shrinking the step size over time
At each step, choosing the step size that minimizes the value of the objective function
'''


step_size = [100, 10,1, 0.1,0.01, 0.001, 0.0001, 0.00001]

def safe(f):
	'''return a new function that is the same as f, 
	except that it outputs infinity whenever f produces an error'''
	def safe_f(*args, **kwargs):
		try:
			return f(*args, **kwargs)
		except:
			return float('inf')
		return safe_f


'''
let's say we have chosen a starting value for the parameters theta_0. Then we can implement gradient descent as:
'''
def minimize_batch(target_fn, gradient_fn, theta_0, tolerance= 0.000001):
	'''use gradient descent to find theta that minimizes target function'''

	step_size = [100, 10,1, 0.1,0.01, 0.001, 0.0001, 0.00001]

	tehta = theta_0
	target_fn = safe(targett_fn)
	value = target_fn(theta)

	while True:
		gradient = gradient_fn(theta)
		next_thetas = [step(theta, gradient, -step_size)
						for step_size in step_sizes]
		# choose the one that minimizes the error function

		next_theta = min(next_thetas, key = target_fn)
		next_value = target_fn(next_theta)

		# stop if we 're not converging

		if abs(value - next_value) < tolerance:
			return theta
		else:
			theta, value = next_theta, next_value


#maximize a function, which we can do by minimizing its negative 
def negate(f):
	# return a function that for any input x returns -f(x)
	return lambda *args, **kwargs: -f(*args, **kwargs)

def negate_all(f):
	return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]

def maximize_batch(target_fn, gradient_fn, theta_0, tolerence= 0.000001):
	return minimize_batch(negate(target_fn), negate_all(gradient_fn), theta_0, tolerance)


	