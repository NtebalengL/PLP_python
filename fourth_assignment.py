#Week four assignment
def modify_content(content):
    """
    Modify the file content in some way.
    Example: Convert all text to uppercase.
    """
    return content.upper()

def main():
    filename = input("Enter the name of the file you want to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()

        modified_content = modify_content(content)

        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"File processed successfully! Modified file saved as '{new_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
