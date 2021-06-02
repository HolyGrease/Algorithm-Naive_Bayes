# Example of creating Dataset object
Firstly, import Dataset:

	from dataset import Dataset

Secondly, get some data:

	data = [
		[5.1, 3.5, 1.4, 0.2, "Iris-setosa"],
		[5.0, 3.2, 1.2, 0.2, "Iris-setosa"],
		[6.4, 3.2, 4.5, 1.5, "Iris-versicolor"],
		[6.7, 3.1, 4.4, 1.4, "Iris-versicolor"],
		[6.7, 3.0, 5.2, 2.3, "Iris-virginica"]]

Thirdly, set columns (attributes) names:

	column_names = [
		"Sepal length", "Sepal width",
		"Petal length", "Petal width",
		"Class"]

Now we can create Dataset object. Arguments:
- data - just list of list
- target index - index of target attribute, attribute that contains classes values
- column or attributes names - list of attributes names
- name - Dataset name
<a/>

	iris = Dataset(data, 4, column_names, "Iris")

Also you can just get iris dataset by calling method

	get_iris().

You can specify path to dataset file by passing this path as argument, for example:

	get_iris("data\\iris.data")

Default value of path 
> resources\\data\\iris\\iris.data.

	iris = get_iris()

# Classification
Don't forget to import

	from naive_Bayes import naive_bayes

For classification just call naive_bayes function. This function gets 2 arguments:
- dataset - train dataset used for classification
- row - instance to classify

As return function gives list of values (for each class in train dataset):
>
> [(probability_1, class_1), (probability_2, class_2), ...]
>
To get the most probable class use function max() and get by index class value

	predicted_classes = naive_bayes(train, row)
	predicted_class = max(predicted_classes)[1]