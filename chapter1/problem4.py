import os

def list_directory_contents(path="."):
    try:
        # Get the list of files and directories in the given path
        contents = os.listdir(path)
        print(f"Contents of '{path}':")
        
        # for loop is used to iterate through and print each contents of the directory in an organized manner.
        
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for accessing '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
directory_path = input("Enter the directory path: ")  # You can use '.' for the current directory
list_directory_contents(directory_path)
