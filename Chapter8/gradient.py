from functools import partial

def difference_quotient(f,x,h):
	return (f(x+h) - f(x)) / h

#the square function's derivative

def square(x):
	return x * x
def derivative(x):
	return 2 * x


derivative_estimate = partial(difference_quotient, square, h=0.00001)

#plot to show they are basically the same
import matplotlib.pyplot as plt 
x = range(-10, 10)
plt.title("Actual Derivatives VS. Estimates")
plt.plot(x, map(derivative, x), 'rx', label = 'Actual')
plt.plot(x, map(derivative_estimate, x), 'b+', label = 'Estimate')
plt.legend(loc=9)
plt.show()


#calculate its ith partial derivative by treating it as a function of jsut its ith variable, holding the other variables fixed:
def partial_difference_quotient(f,v,i,h):
	# compute the ith partial difference quotient of f at v
	w = [v_j + (h if j == i else 0) 
		 for j, v_j in enumerate(v)]

	return (f(w) - f(v)) / h

def estimate_gradient(f, v, h = 0.00001):
	return [partial_difference_quotient(f,v,i,h) 
			for i, _ in enumerate(v)]

