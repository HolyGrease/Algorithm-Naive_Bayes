from itertools import groupby

def naive_bayes(dataset, row):
	classes = list(set(dataset.get_target_column()))

	return [(naive_bayes_helper(dataset, row, value), value) for value in classes]

def naive_bayes_helper(dataset, row, cl):
	total = len(dataset.get_target_column())
	total_class = dataset.get_target_column().count(cl)

	# Probability of cl
	probability = total_class / total
	#
	for index, value in enumerate(row):
		# If provavility of value 0, return 0
		m = len(list(set(dataset.get_column(index))))

		# Concat column and target column
		pairs = zip(dataset.get_column(index), dataset.get_target_column())
		# Group by value
		grouped_by_class = {
			key: list(value) 
			for key, value in groupby(sorted(pairs, key=lambda x: x[1]), lambda x: x[1])}[cl]
		# Group by cl
		grouped_by_value_and_class = {
			key: len(list(value))
			for key, value in groupby(sorted(grouped_by_class, key=lambda x: x[0]), lambda x: x[0])}
		#
		if not value in grouped_by_value_and_class:
			probability *= 1 / (total_class + m)
			continue
		n = grouped_by_value_and_class[value]
		#
		probability *= (n + 1) / (total_class + m)

	return probability