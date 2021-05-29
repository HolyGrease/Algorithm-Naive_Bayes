from dataset import Dataset
from naive_Bayes import naive_bayes

def main():
	# Load dataset
	iris = Dataset.get_iris()
	# Print first 10 rows
	iris.print(10)
	# Shuffle dataset
	iris = iris.shuffle()
	# Split dataset on train and test
	# train dataset include 80% of original dataset
	train, test = iris.split_by_ratio(0.8)
	# Variable to count correct predictions
	correct = 0
	for row in test.data:
		# Get correct value
		assert_value = row.pop(test.target)
		# Make prediction
		predicted_classes = naive_bayes(train, row)
		# Get most probable class
		predicted_class = max(predicted_classes)[1]
		# If prediction is correct
		if predicted_class == assert_value:
			correct += 1
		# Print compare log to termainal
		print("{:<15} ?= {:<15}".format(assert_value, predicted_class))
	# Count and print accuracy
	print("Acurracy: {:1.2}".format(correct / test.get_rows_number()))

if __name__ == '__main__':
	main()