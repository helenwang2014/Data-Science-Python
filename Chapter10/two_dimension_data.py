from scipy.special import ndtri
from matplotlib import pyplot as plt
import random
import numpy as np 


def random_normal():
	# returns a random draw from a standard normal distribution
	return ndtri(random.random())

xs = [random_normal() for _ in range(1000)]
ys1 = [x + random_normal() / 2 for x in xs]
ys2 = [-x + random_normal() / 2 for x in xs]

plt.scatter(xs, ys1, marker = '.', color = 'black', label = 'ys1')
plt.scatter(xs, ys2, marker = '.', color = 'gray', label = 'ys2')
plt.xlabel('xs')
plt.ylabel('ys')
plt.legend(loc=4)
plt.title("Very Different Joint Distributions")
plt.show()


print np.correlate(xs, ys1)
print np.correlate(xs, ys2)

