word_counts = {}
for word in document:
	if word in word_counts:
		word_counts[words]+= 1
	else:
		word_counts[word] = 1

word_counts{}


"""
#behave gracefully for missing keys"

word_counts = {}
for word in document:
	previous_count = word_counts.get(word,0)
	word_counts[words] = previous_count + 1

"""

from collections import defaultdict
word_counts = defaultdict(int)
for word in document:
	word_counts[word] += 1

	