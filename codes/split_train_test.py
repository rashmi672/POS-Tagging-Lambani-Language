from sklearn.model_selection import train_test_split

# Define the path to your dataset
dataset_path = "codes\dataset.txt"

# Load the dataset
with open(dataset_path, 'r', encoding='utf-8') as file:
    dataset = file.readlines()

# Define the ratio for splitting (e.g., 80% train, 20% test)
train_ratio = 0.9

# Split the dataset into train and test sets
train_data, test_data = train_test_split(dataset, train_size=train_ratio, test_size=1 - train_ratio)

# Remove newline character from the last line of train and test data
if train_data:
    train_data[-1] = train_data[-1].rstrip('\n')
if test_data:
    test_data[-1] = test_data[-1].rstrip('\n')


# Write train data to a file
with open("codes/train_data.txt", 'w', encoding='utf-8') as file:
    file.writelines(train_data)

# Write test data to a file
with open("codes/test_data.txt", 'w', encoding='utf-8') as file:
    file.writelines(test_data)
