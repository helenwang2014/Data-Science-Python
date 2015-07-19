# look at the correlation matrix, in which the entry in row i and column j is the correlation between the ith dimension and jth dimension of the data



'''

def correlation_matrix(data):
	return the num_columns x num_columns matrix whose (i, j)th entry
	is the correlation between column i and j of data 

	_, num_columns = shape(data)

	def matrix_entry(i, j):
		return correlation(get_column(data, i), get_column(data, j))

	return make_matrix(num_columns, num_columns, matrix_entry)

'''
import numpy as np
import matplotlib.pyplot as plt 
data = [[]]
_, num_columns = np.shape(data)
fig, ax = plt.subplots(num_columns, num_columns)

for i in range(num_columns):
	for j in range(num_columns):

		# scatter column_j on the x-axis vs column_i on the y-axis
		if i != j: ax[i][i].scatter(get_column(data, j), get_column(data, i))

		# unless i == j, in which case show the series name
	else: ax[i][i].annotate("series " + str(i), (0.5,0.5), 
							xycoords='axes fraction', 
							ha="center", va="center")

		# then hide axis labels except left and bottom charts
	if i < num_columns - 1: ax[i][i].xaxis.set_visible(False)
	if j > 0: ax[i][j].yaxis.set_visible(False)


	# fix the bottom right and top left axis labels, which are wrong becasue their charts only have text in them
	ax[-1][-1].set_xlim(ax[0][-1].get_xlim())
	ax[0][0].set_ylim(ax[0][1].get_ylim())

	plt.show()


