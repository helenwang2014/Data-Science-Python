def tokenize(message):
	message = message.lower()
	all_words = re.findall("[a - z0 - 9']+ ", message)
	return set(all_words)

# count the words in a labeled training set of messages
def count_words(training_set):
	counts = defaultdict(lambda: [0,0])
	for message, is_spam in training_set:
		for word in tokenize(message):
			counts[word][0 if is_spam else 1] += 1
		return counts

# return a list of triplets containing each word, the probability of seeing that word in a spam message, 
# and the probability of seeing that word in a nonspam message

def word_probabilities(counts, total_spams, total_non_spams, k=0.5):
	# turn the word_counts into a w, p(w | spam) and p(w | ~spam)

	return [(w, 
			 (spam + k) / (total_spams + 2 * k), 
			 (non_spam + k) / (total_non_spams + 2 * k))
			 for w, (spam, non_spam) in counts.iteritems()]

def spam_probability(word_probs, message):
	message_words = tokenize(message)
	log_prob_if_spam = log_prob_if_not_spam = 0.0

	# iterate through each word in our vocabulary
	for word, prob_if_spam, log_prob_if_not_spam in word_probs:

		if word in message_words:
			log_prob_if_spam += math.log(prob_if_spam)
			log_prob_if_not_spam += math.log(log_prob_if_not_spam)

		else:
			log_prob_if_spam += math.log(1.0 - prob_if_spam)
			log_prob_if_not_spam += math.log(1.0 - log_prob_if_not_spam)

	prob_if_spam = math.exp(log_prob_if_spam)
	log_prob_if_not_spam = math.exp(log_prob_if_not_spam)
	return prob_if_spam / (prob_if_spam + log_prob_if_not_spam)

# class NaiveBayesClassifier:
def __init__(self, k = 0.5):
	self.k = k
	self.word_probs = []

def train(self, training_set):
	# count spam and non-spam messages
	num_spams = len([is_spam
					for message, is_spam in training_set
					if is_spam])

	num_non_spams = len(training_set) - num_spams

	# run training data through our "pipeline"
	word_counts = count_words(training_set)
	self.word_probs = word_probabilities(word_counts,
										num_spams, 
										num_non_spams,
										self.k)

def classify(self, message):
	return spam_probability(self.word_probs, message)


# ===================
import glob, re

# modify the path with wherever you've put the files
path = r"C:\spam\*\*"

data = []
for fn in golb.glb(path):
	is_spam = "ham" not in fn
	with open(fn, 'r') as file:
		for line in file:
			if line.startwith("Subject:"):
				# remove the leading "Subject: " and keep what's left
				subject = re.sub(r"^Subject: ", "", line).strip()
				data.append((subject, is_spam))



random.seed(0)
train_data, test_data = split_data(data, 0.75)
classifier = NaiveBayesClassifier()
classifier.train(train_data)

classified = [(subject, is_spam, classifier.classify(subject)) 
			  for subject, is_spam in test_data]

counts = Counter((is_spam, spam_probability > 0.5)
				 for _, is_spam, spam_probability in classified)


# sort by spam_probability from smallest to largest
classfied.sort(key=lambda row: row[2])

spammist_hams = filter(lambda row: not row[1], classified)[-5]

hammiest_spams = filter(lambda row: row[1], classified)[:5]


def p_spam_given_word(word_prob):
	word, prob_if_spam, prob_if_not_spam = word_prob
	return prob_if_spam / (prob_if_spam + prob_if_not_spam)

words = sorted(classified.word_probs, key= p_spam_given_word)

spammiest_words = words[-5:]
hammiest_words = words[:5]


def drop_final_s(word):
	return re.sub("s$", "", word)

	






n