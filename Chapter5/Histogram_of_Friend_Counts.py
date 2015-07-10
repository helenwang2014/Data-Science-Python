from collections import Counter
from matplotlib import pyplot as plt 

num_friends = [100,49,41,40,25, 34, 4,3,2,1,1,7,7,8, 8,8,8,8,8,8,8,8, 8,8,8,8,8,8,8,8]

friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs,ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()
