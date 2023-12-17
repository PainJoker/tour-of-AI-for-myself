# Example of building evaluation metrics for models
from math import sqrt

# Calculate accuracy percentage between two lists
def accuracy_metric(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(len(actual)) * 100

# Calculate a confusion matrix
def confusion_matrix(actual, predicted):
    unique = set(actual)
    matrix = [list() for x in range(len(unique))]
    for i in range(len(unique)):
        matrix[i] = [0 for x in range(len(unique))]
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
    for i in range(len(actual)):
        x = lookup[actual[i]]
        y = lookup[predicted[i]]
        matrix[y][x] += 1
    return unique, matrix 

# Calculate mean absolute error(MAE)
def MAE_metric(actual, predicted):
    sum_error = 0.0
    for i in range(len(actual)):
        sum_error += abs(predicted[i] - actual[i])
    return sum_error / float(len(actual))

def RMSE_metric(actual, predicted):
    sum_error = 0.0
    for i in range(len(actual)):
        sum_error += (predicted[i] - actual[i]) ** 2
    return sqrt(sum_error / float(len(actual)))
    
# Test accuracy for classification problems
actual = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
predicted = [0, 1, 1, 0, 0, 1, 0, 1, 1, 1]
accuracy = accuracy_metric(actual, predicted)
print(f"The accuracy is {accuracy}%.")
unique, matrix = confusion_matrix(actual, predicted)
print(f"Classification set: {unique}.")
print(f"Confusion matrix is {matrix}.")

# Metrics for regression problems
actual = [0.1, 0.2, 0.3, 0.4, 0.5]
predicted = [0.11, 0.19, 0.29, 0.41, 0.5]
mae = MAE_metric(actual, predicted)
print(f"The Mean Absolute Error is {mae:5.4f}.")
rmse = RMSE_metric(actual, predicted)
print(f"The Root Mean Square Error is {rmse:5.4f}.")