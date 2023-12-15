# Example of loading CSV dataset
import csv
from math import sqrt

# Load a CSV file
def load_csv(filename):
    dataset = list()
    with open(filename, mode='r') as file:
       csv_reader = csv.reader(file) # Return rows in file
       for row in csv_reader:
           if not row: # Strip empty line
               continue
           dataset.append(row)
    return dataset

def str_column_to_float(dataset, col):
    for row in dataset:
        row[col] = float(row[col])

# Convert string column to integer     
def str_column_to_int(dataset, col):
    class_values = [row[col] for row in dataset]
    unique = set(class_values) # Eliminate the dupulicate classes in datasets
    lookup = dict()
    for i, value in enumerate(unique): # Add a counter in the class set
        lookup[value] = i # Convert to a dict
    for row in dataset:
        row[col] = lookup[row[col]] # Replace the string
    return lookup

# Find the max and min of each attr in dataset
def dataset_maxmin(dataset):
    maxmin = list()
    for i in range(len(dataset[0])):
        col_value = [row[i] for row in dataset]
        col_max = max(col_value)
        col_min = min(col_value)
        maxmin.append([col_max, col_min])
    return maxmin
    
# Rescale dataset columns to the range [0-1]
def normalize_dataset(dataset, maxmin):
    for row in dataset:
        for i in range(len(dataset[0])):
            row[i] = (row[i]-maxmin[i][1]) / (maxmin[i][0]-maxmin[i][1])
    
# Calculate column means
def col_means(dataset):
    means = [0 for i in range(len(dataset[0]))]
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        means[i] = sum(col_values) / float(len(col_values))
    return means

# Calculate column standard deviation
def col_stdevs(dataset, means):
    stdevs = [0 for i in range(len(dataset[0]))]
    for i in range(len(dataset[0])):
        variance = [pow(row[i]-means[i]) for row in dataset]
        stdevs[i] = sum(variance)
    stdevs = [sqrt(item)/float(len(dataset[0])-1) for item in stdevs]    
    return stdevs

# Standardize the dataset
# Assume the sampling data is normally distributed
def standardize_dataset(dataset, means, stdevs):
    for row in dataset:
         for i in range(len(dataset[0])):
             row[i] = (row[i] - means[i]) / stdevs[i]

# Load dataset
pima_filename = "pima-indians-diabetes.csv"
pima_dataset = load_csv(pima_filename)
print(f"Loaded data file {pima_filename} with {len(pima_dataset)} rows \
and {len(pima_dataset[0])} columns.")
print(f"The first element is {pima_dataset[0]}.")
# Convert string columns to float
for i in range(len(pima_dataset[0])):
    str_column_to_float(pima_dataset, i)
print(f"After operation: {pima_dataset[0]}.")
# Obtain the range of attr
pima_maxmin = dataset_maxmin(pima_dataset)
print(f"The max and min of each attr are {pima_maxmin}.")
# Normalize the columns
normalize_dataset(pima_dataset, pima_maxmin)
print(f"After normalization, the first list is {pima_dataset[0]}.")

iris_filename = "iris.csv"
iris_dataset = load_csv(iris_filename)
print(f"\nLoaded data file {iris_filename} with {len(iris_dataset)} rows \
and {len(iris_dataset[0])} columns.")
print(f"The first element is {iris_dataset[0]}.")
# Convert string column to float
for i in range(4):
    str_column_to_float(iris_dataset, i)
# Convert class column to int
lookup = str_column_to_int(iris_dataset, 4)
print(f"After operation: {iris_dataset[0]}.")
print(f"The mapping between classes and index is {lookup}.")