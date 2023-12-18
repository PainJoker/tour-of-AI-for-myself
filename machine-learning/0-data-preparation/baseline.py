# Example of constructing baseline model
from random import seed, randrange

# Random decision making algorithm
def random_output(train, test):
    train_output = [row[-1] for row in train]
    unique = list(set(train_output))
    predicted = list()
    for i in range(len(test)):
        index = randrange(len(unique))
        predicted.append(unique[index])
    return predicted 

# zero rule algorithm for classification
def zero_rule_algorithm_classification(train, test):
    output_values = [row[-1] for row in train]
    prediction = max(set(output_values), key=output_values.count)
    predicted = [prediction for i in test]
    return predicted
    
# zero rule algorithm for regression
def zero_rule_algorithm_regression(train, test):
    output_values = [row[-1] for row in train]
    mean = sum(output_values) / float(len(output_values))
    predicted = [mean for row in test]
    return predicted
    
seed(1)
train = [[0], [1], [0], [1], [1], [1]]
test = [[None], [None], [None], [None]]
predictions = random_output(train, test)
print(f"By random prediction, we have the results: {predictions}.")
predictions = zero_rule_algorithm_classification(train, test)
print(f"By zero rule prediction for classification, we have the results: {predictions}.")

train = [[10], [15], [12], [15], [18], [20]]
predictions = zero_rule_algorithm_regression(train, test)
print(f"By zero rule prediction for regression, we have the results: {predictions}.")
