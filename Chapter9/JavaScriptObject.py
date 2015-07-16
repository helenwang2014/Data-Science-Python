# JavaScript objects look quite similar to Python dicts, which makes their string representations easy to interpret:

# we can parse JSON using Python's json module

import json
serialized = '''{"title" : "Data Science Book", 
			  "author" : "Joel Grus", 
			  "publicationYear": 2014,
			  "topics" : ["data", "science", "data science"]}'''



# parse the JSON to creat a Python dict
deserialized = json.loads(serialized)
if "data science" in deserialized["topics"]:
	print deserialized




