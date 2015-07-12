from matplotlib import pyplot as plt

def uniform_cdf(x):
	if x < 0:
		return 0 
	elif x < 1:
		return x
	else:
		return 1


xs = [x for x in range(-3,3)]
plt.plot(xs, [uniform_cdf(x) for x in xs])

plt.axis([-1.0, 2.0, -1.0, 1.5])

plt.show()

