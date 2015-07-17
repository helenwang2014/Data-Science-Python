import random
import math
from scipy.special import ndtri
from collections import Counter
from matplotlib import pyplot as plt

def bucketize(point, bucket_size):
	# floor the point to the next lower multiple of bucket_size
	return bucket_size * math.floor(point / bucket_size)

def make_histogram(points, bucket_size):
	# buckets the points and counts how many in each bucket
	return Counter(bucketize(point, bucket_size) for point in points)

def plot_histogram(points, bucket_size, title= ""):
	histogram = make_histogram(points, bucket_size)
	plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
	plt.title(title)
	plt.show()

random.seed(0)

uniform = [200 * random.random() - 100 for _ in range(10000)]

normal = [57 * ndtri(random.random())
			for _ in range(10000)]



# both have means close to 0 and standard deviation close to 58

plot_histogram(uniform, 10, "Uniform Histogram")
plot_histogram(normal, 10, "Normal Histogram")


