from __future__ import division

from collections import Counter

num_friends = [100,49,41,40,25, 34,4,3,2,1,1,7,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]



def mean(x):
	return sum(x)/len(x)


print mean(num_friends)




def median(v):

	n = len(v)
	sorted_v = sorted(v)
	midpoint = n // 2

	if n % 2 == 1:
		return sorted_v[midpoint]

	else: 
		lo = midpoint - 1
		hi = midpoint 

		return (sorted_v[lo] + sorted_v[hi]) / 2

		median(num_friends)



print median(num_friends)





def quantile(x, p):
	p_index = int(p * len(x))
	return sorted(x)[p_index]



print quantile(num_friends, 0.10)
print quantile(num_friends, 0.25)
print quantile(num_friends, 0.75)
print quantile(num_friends, 0.90)



def mode(x):
	counts = Counter(x)
	max_count = max(counts.values())
	return [x_i for x_i, count in counts.iteritems()
			if count == max_count]

print mode(num_friends)





