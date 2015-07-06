s1 = set()
s2 = set([1,2,2,3])
self.dict = {}
if value is not None:
	for value in values:
		self.add(value)

def __repr__(self):
	return "set: " + str(self.dict.keys())

def add(self, value):
	self.dict[value] = True

def contains(self, value):
	return value in self.dict

def remove(self, value):
	del self.dict[value]

s = set([1,2,3])
s.add(4)
print s.contains(4)
s.remove(3)
print s.contains(3)











