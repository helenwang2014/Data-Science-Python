from twython import TwythonStreamer
from  collections import Counter
# appending data to a global variable is pretty poor form
# but it makes the example much simpler
tweets = []

class MyStreamer(TwythonStreamer):
	'''our own subclass of TwythonStreamer that specifies how to interact with the stream'''

	def on_success(self, data):
		'''what do we do when twitter sends us data? 
		here data will be a Python dict representing a tweet'''

		# only want to collect English-language tweets
		if data['lang'] == 'en':
			tweets.append(data)
			print "received tweet #", len(tweets)

		# stop when we've collected enough
		if len(tweets) >= 1000:
			self.disconnect()

	def on_error(self, status_code, data):
		print status_code, data
		self.disconnect()
CONSUMER_KEY = '...'
CONSUMER_SECRET = '...'
ACCESS_TOKEN = '...'
ACCESS_TOKEN_SECRET = '...'


stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET,
					ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# start consuming public statuses that contain the keyword 'data'
stream.statuses.filter(track='data')

# if instead we wanted to start consuming a sample of *all* public statuses
# stream. statuses.sample()


top_hashtags = Counter(hashtag['text'].lower()
						for tweet in tweets
						for hashtag in tweets["entities"]["hashtags"])

print top_hashtags.most_common(5)
