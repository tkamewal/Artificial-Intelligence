def capitalize_first_letter(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        
    modified_content = ' '.join(word.capitalize() for word in content.split())
    
    with open(file_path, 'w') as file:
        file.write(modified_content)

# Example usage
file_path = 'example.txt'  # Replace 'example.txt' with the path to your file
capitalize_first_letter(file_path)

print(f"First letter of every word in '{file_path}' has been capitalized.")
