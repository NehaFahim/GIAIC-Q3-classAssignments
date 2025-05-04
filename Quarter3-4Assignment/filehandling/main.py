# Step 1: Write data to a file
def write_to_file():
    with open("my_file.txt", "w") as file:
        file.write("Hello Neha!\n")
        file.write("This is your file handling assignment.\n")
    print("✅ File created and written successfully.")

# Step 2: Read data from the file
def read_from_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("\n File Content:\n" + content)
    except FileNotFoundError:
        print("Error: File not found.")

# Step 3: Append new data to the file
def append_to_file():
    with open("my_file.txt", "a") as file:
        file.write("New line added using append mode.\n")
    print("Data appended to the file.")

# Run all steps
write_to_file()
read_from_file()
append_to_file()
read_from_file()
