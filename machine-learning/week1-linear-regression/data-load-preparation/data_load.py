# Example of loading CSV dataset
import csv

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

# Load dataset
pima_filename = "pima-indians-diabetes.csv"
pima_dataset = load_csv(pima_filename)
print(f"Loaded data file {pima_filename} with {len(pima_dataset)} rows 
      and {len(pima_dataset[0])} columns.")
print(f"The first element is {pima_dataset[0]}.")
# Convert string columns to float
for i in range(len(pima_dataset[0])):
    str_column_to_float(pima_dataset, i)
print(f"After operation: {pima_dataset[0]}")

iris_filename = "iris.csv"
iris_dataset = load_csv(iris_filename)
print(f"Loaded data file {iris_filename} with {len(iris_dataset)} rows 
      and {len(iris_dataset[0])} columns.")
print(f"The first element is {iris_dataset[0]}.")
# Convert string column to float
for i in range(4):
    str_column_to_float(iris_dataset, i)
# Convert class column to int
lookup = str_column_to_int(iris_dataset, 4)
print(f"After operation: {iris_dataset[0]}.")
print(f"The mapping between classes and index is {lookup}.")