
from matplotlib import pyplot as plt
import math


def normal_cdf(x, mu=0, sigma=1):
	return (1 + math.erf((x - mu) /math.sqrt(2)/ sigma)) /2


xs = [x/10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_cdf(x, sigma = 1) for x in xs], '-', color = 'g', label='mu=0,sigma=1')
plt.plot(xs, [normal_cdf(x,sigma = 2) for x in xs], '--', color = 'r',label = 'mu=0,sigma =2')
plt.plot(xs,[normal_cdf(x,sigma = 0.5) for x in xs], ':', color = 'b',label='mu=0, sigma=0.5')
plt.plot(xs, [normal_cdf(x,mu=-1) for x in xs], '-.',label = 'mu=-1,sigma=1')
plt.legend(loc=4)
plt.title("Various Normal cdfs")
plt.show()


# invert normal_cdf to find the value corresponding to a specified probability

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
	if mu != 0 or sigma != 1:
		return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

	low_z, low_p = -10.0, 0
	hig_z, hig_p = 10.0, 1

	while hig_z - low_z > tolerance:
		mid_z = (low_z + hig_z) / 2
		mid_p = normal_cdf(mid_z)
		if mid_p < p:
			low_z, low_p = mid_z, mid_p
		elif mid_p > p:
			hig_z, hig_p = mid_z, mid_p
		else:
			break

	return mid_z

print inverse_normal_cdf(p=0.99, mu=0, sigma=1, tolerance=0.00001)