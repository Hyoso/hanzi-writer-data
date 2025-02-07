import json
import os

def generate_json_for_characters(directory, characters, output_file):
    combined_data = {}

    for char in characters:
        file_path = os.path.join(directory, f'{char}.json')
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    combined_data[char] = json.load(file)
            except Exception as e:
                print(f'Error reading file for character "{char}": {e}')
        else:
            print(f'File not found for character: {char}')

    # Debugging: Print combined data to verify
    print("Combined Data:", combined_data)

    # Write the combined data to a JSON file
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(combined_data, file, ensure_ascii=False, indent=4)
        print(f'Generated JSON file: {output_file}')
    except Exception as e:
        print(f'Error writing to file: {e}')

# Example usage
directory = 'D:\Github projects\hanzi-writer-data\data'
characters = ['一', '二', '三']
output_file = 'generated_characters.json'
generate_json_for_characters(directory, characters, output_file)