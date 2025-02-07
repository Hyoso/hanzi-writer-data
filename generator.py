import json
import os

# Define the path to the directory containing the JSON files
directory = 'D:\Github projects\hanzi-writer-data'

# List of characters you want to include
characters = ['一', '二']

# Initialize an empty dictionary to hold the combined data
combined_data = {}

# Loop through each character and load its data
for char in characters:
    file_path = os.path.join(directory, f'{char}.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        combined_data[char] = json.load(file)

# Write the combined data to a new JSON file
output_file = 'combined_characters.json'
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(combined_data, file, ensure_ascii=False, indent=4)

print(f'Combined JSON file created: {output_file}')