import os

# File Creation 
def create_file():
    try:
        # Check if the file already exists
        if not os.path.exists("my_file.txt"):
            # Create a new file 'my_file.txt' in write mode if it doesn't exist
            with open("my_file.txt", "w") as file:
                # Write three lines of text, including strings and numbers
                file.write("Line 1: Hello, this is the first line.\n")
                file.write("Line 2: Power Learn Project is fun!\n")
                file.write("Line 3: The number is 19.\n")
            print("File created and written successfully.")
            return False  # Indicates that the file was created on this run
        else:
            print("File already exists, skipping creation.")
            return True  # Indicates that the file already existed before this run
    except Exception as e:
        print(f"An error occurred while creating/writing the file: {e}")
    finally:
        print("File creation step complete.\n")

# File Reading and Display
def read_file():
    try:
        # Open the file in read mode
        with open("my_file.txt", "r") as file:
            # Read and display the file content
            content = file.read()
            print("Reading file content:")
            print(content)
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: Permission denied to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File reading step complete.\n")

# File Appending (only appends on subsequent runs)
def append_file():
    try:
        # Open the file in append mode, but only if it exists
        with open("my_file.txt", "a") as file:
            # Append three additional lines to the file
            file.write("Line 4: Adding more content.\n")
            file.write("Line 5: Appending is useful!\n")
            file.write("Line 6: The final number is 77.\n")
        print("File appended successfully.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")
    finally:
        print("File appending step complete.\n")

if __name__ == "__main__":
    # Create the file and write initial content if it doesn't exist
    file_existed = create_file()  

    # Read the file to show its content
    read_file()

    # Only append if the file already existed before this run (i.e., on subsequent runs)
    if file_existed:
        append_file()
        read_file()  # Show updated content after appending
