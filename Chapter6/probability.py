import random

def random_kid():
	return random.choice(["boy", "girl"])

both_girls = 0.0
older_girl = 0.0
either_girl = 0.0

random.seed(0)
for _ in range(100000):
	younger = random_kid()
	older = random_kid()
	if older == "girl":
		older_girl += 1
	if older == "girl" and younger == "girl":
		both_girls += 1
	if older == "girl" or younger == "girl":
		either_girl += 1

print "p(both|older):", round(both_girls/older_girl, 2)
print "p(both|either):", round(both_girls/either_girl, 2)


