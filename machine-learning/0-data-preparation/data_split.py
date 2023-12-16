# Example of splitting a contrived dataset into train and test
from random import seed, randrange
from math import floor

# Split a dataset into a train and test set
def train_test_spilt(dataset, split=0.60):
    train_set = list()
    train_size = split * len(dataset)
    test_set = list(dataset) # pop later to get done
    while len(train_set) < train_size:
        index = randrange(len(test_set))
        train_set.append(test_set.pop(index))
    return train_set, test_set

# Split a dataset into k folds
def cross_validation_spilt(dataset, folds=3):
    dataset_split = list()
    dataset_copy = list(dataset)
    fold_size = floor(len(dataset) / folds)
    for i in range(folds):
        fold = list()
        while len(fold) < fold_size:
            index = randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        dataset_split.append(fold)
    return dataset_split
 
seed(1)
dataset = [i for i in range(10)]
print(f"Contrived dataset is {dataset}.")
train_set, test_set = train_test_spilt(dataset)
print(f"Training set is {train_set}.\nTest set is {test_set}.")
dataset_split = cross_validation_spilt(dataset, folds=4)
print(f"After divided into 4 folds: {dataset_split}.")