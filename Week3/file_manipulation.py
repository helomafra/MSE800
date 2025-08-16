# Week3- Activity 1: Work with .txt file
# Using the attached text file, open, read, and write the complete information for the demo.txt. 
# Share the GitHub link here(with adding the screenshot of the result).

class FileManipulation:
    def __init__(self, path):
        self.path = path

    def write(self, data):
        with open(self.path, "w") as file:
            file.write(data)
    
    def read(self): 
        with open(self.path, "r") as file: 
            content = file.read()
            return content

def main():
    file_manipulation = FileManipulation("Week3/demo.txt")
    
    # Print the content of the file before manipulation
    print(f"Content of the file before manipulation: {file_manipulation.read()}")
    
    # Write to the file
    file_manipulation.write("Hello, World!")
    print("Data written to file successfully!")
    
    # Read from the file
    content = file_manipulation.read()
    print(f"Content read from file: {content}")

if __name__ == "__main__":
    main()

