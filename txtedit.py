import os
import re

def edit_txt_file():
    # Ask for file path
    file_path = input("Enter the path for the txt file to edit (e.g. D:\\user\\Downloads\\YourFileName.txt): ")
    
    try:
        # Read the original content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Get the directory of the original file
        directory = os.path.dirname(file_path)
        
        # Create the path for the modified file
        modified_file_path = os.path.join(directory, 'modified.txt')
        
        # Remove all instances of '[ xx:xx:xx] ' pattern where x can be digits, zero, or "X"
        # This pattern matches exactly the format described in the requirement
        modified_content = re.sub(r'\[\s*[0-9X]+:[0-9X]+:[0-9X]+\]\s*', '', content)
        
        # Remove empty lines
        lines = modified_content.split('\n')
        non_empty_lines = [line for line in lines if line.strip()]
        modified_content = '\n'.join(non_empty_lines)
        
        # Write the modified content to the new file
        with open(modified_file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        
        print(f"Text file has been edited and saved as 'modified.txt' in the same directory.")
        print(f"Path: {modified_file_path}")
        
    except FileNotFoundError:
        print("Error: File not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    edit_txt_file()