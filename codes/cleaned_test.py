# Define the path to your dataset
dataset_path = "test_data/test_tagged_200.txt"

# Load the dataset
with open(dataset_path, 'r', encoding='utf-8') as file:
    dataset = file.readlines()

# Define a list of word classes to remove
word_classes_to_remove = ['/noun', '/verb', '/adjective', '/preposition', '/pronoun', '/conjunction', '/adverb', '/interjection']

# Remove word classes from each line
cleaned_dataset = []
for line in dataset:
    for word_class in word_classes_to_remove:
        line = line.replace(word_class, '')
    cleaned_dataset.append(line)

# Write the cleaned dataset to a new file
cleaned_file_path = "test_data/test_data_200.txt"
with open(cleaned_file_path, 'w', encoding='utf-8') as file:
    file.writelines(cleaned_dataset)

print("Word classes removed. Cleaned dataset saved to", cleaned_file_path)
