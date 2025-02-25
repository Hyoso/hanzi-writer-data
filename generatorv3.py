import json
import os

def generate_json_for_characters(directory, characters, output_folder='generated'):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    for char in characters:
        input_file = os.path.join(directory, f'{char}.json')
        output_file = os.path.join(output_folder, f'{char}.json')
        
        if os.path.exists(input_file):
            try:
                # Read the existing JSON data
                with open(input_file, 'r', encoding='utf-8') as f:
                    original_data = json.load(f)
                
                # Create new structure with character as root key
                new_data = {
                    char: {
                        "strokes": original_data.get("strokes", []),
                        "medians": original_data.get("medians", []),
                        "radStrokes": original_data.get("radStrokes", [])
                    }
                }
                
                # Write the modified data to the new JSON file
                with open(output_file, 'w', encoding='utf-8') as f_out:
                    json.dump(new_data, f_out, ensure_ascii=False, indent=4)
                print(f'Saved: {output_file}')
            except Exception as e:
                print(f'Error processing {char}: {e}')
        else:
            print(f'Input file not found: {input_file}')

# Example usage
directory = r'D:\Github projects\hanzi-writer-data\data'
characters = ['黄', '诗', '雅']
generate_json_for_characters(directory, characters)