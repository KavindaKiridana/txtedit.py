import os

def remove_blank_lines():
    # Ask for file path
    file_path = input("Enter the path for the txt file to edit (e.g. D:\\user\\Downloads\\YourFileName.txt): ")
    
    try:
        # Read the original content
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Get the directory of the original file
        directory = os.path.dirname(file_path)
        
        # Create the path for the modified file
        modified_file_path = os.path.join(directory, 'modified.txt')
        
        # Remove blank lines (lines that only contain whitespace)
        non_blank_lines = [line for line in lines if line.strip()]
        
        # Write the modified content to the new file
        with open(modified_file_path, 'w', encoding='utf-8') as file:
            file.writelines(non_blank_lines)
        
        print(f"Blank lines have been removed and the file saved as 'modified.txt' in the same directory.")
        print(f"Path: {modified_file_path}")
        
    except FileNotFoundError:
        print("Error: File not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    remove_blank_lines()