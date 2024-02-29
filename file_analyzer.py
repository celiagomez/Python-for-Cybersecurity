import os

def analyze_file(file_path):
    #Check if the file exists
    if not os.path.isfile(file_path):
        print(f"The file '{file_path}' does not exist")
        return
    # Get the file size
    file_size = os.path.getsize(file_path)
    print(f"File size: {file_size} bytes")

    # Get the file creation time
    file_time = os.path.getctime(file_path)
    print(f"File creation time: {file_time}")

    # Count the number of lines in the file
    with open(file_path, 'r') as file:
        lines = 0
        for line in file:
            lines += 1
        print(f"Number of lines: {lines}")

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    analyze_file(file_path)