

def raw_majority_vote(labels):
	votes = Counter(labels)
	winner, _ = votes.most_common(1)[0]
	return winner

def majority_vote(labels):
	# assume that labels are ordered from nearest to farthest
	vote_counts = Counter(labels)
	winner, winner_count = vote_counts.most_common(1)[0]
	num_winners = len([counter		
						for count in vote_counts.values()
						if count == winner_count])
	if num_winners == 1:
		return winner
	else:
		return majority_vote(labels[:1]) 

def knn_classify(k, labeled_points, new_point):
	by_distance = sorted(labeled_points,
						key =lambda (point, _): distance(point, new_point))

	k_nearest_labels = [label for _, label in by_distance[:k]]

	return majority_vote(k_nearest_labels)
# ==============================================================

# each entry is ([longitude, latitude], favorite_language)
from matplotlib import pyplot as plt 
from collections import Counter

import re

segments = []
points = []

lat_long_regex = r"<point lat=\"(.*)\" lng=\"(.*)\""

with open("states.txt", "r") as f:
    lines = [line for line in f]

for line in lines:
    if line.startswith("</state>"):
        for p1, p2 in zip(points, points[1:]):
            segments.append((p1, p2))
        points = []
    s = re.search(lat_long_regex, line)
    if s:
        lat, lon = s.groups()
        points.append((float(lon), float(lat)))

def plot_state_borders(plt, color='0.8'):
    for (lon1, lat1), (lon2, lat2) in segments:
        plt.plot([lon1, lon2], [lat1, lat2], color=color)


cities = [([-122.3, 47.53], "Python"), #Seattle
		  ([-96.85, 32.85], "Java"), # Austin
		  ([-89.33, 43.13], "R"),    #Madison
		  ]

# key is language, value is pair(longitudes, latitudes)
plots = {"Java": ([], []), "Python": ([],[]), "R": ([], [])}

markers = {"Java": "o", "Python": "s", "R": "^"}
colors = {"Java": "r", "Python": "b", "R": "g"}

for (longitude, latitude), language in cities:
	plots[language][0].append(longitude)
	plots[language][1].append(latitude)

# create a scatter series for each language
for language, (x, y) in plots.iteritems():
	plt.scatter(x,y, color=colors[language], marker=markers[language], label=language, zoreder=10)
	plot_state_borders(plt)
	plt.legend
	plt.axis([-130,-60,20,55])
	plt.title("Favorite Programming Languages")
	plt.show()


# ==================================================

'''
for k in [1,3,5,7]:
	num_correct = 0 

	for city in cities:
		locaiton, actual_language = city
		other_cities = [other_city
						for other_city in cities
						if other_city != city]
		predicted_language = knn_classify(k, other_cities, location)

		if predicted_language == actual_language:
			num_correcct += 1
	print k, "neighbor[s]:", num_correct, "correct out of", len(cities)



