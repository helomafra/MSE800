# Week3- Activity 2: count the words in the demo text file
 
# Develop a new project that reads demo.txt and returns the total number of words. 
# Share the GitHub repository link and a screenshot of the result.

class FileWordsCount:
    def __init__(self, path):
        self.path = path

    def count_words(self):
        with open(self.path, "r") as file:
            content = file.read()
            return len(content.split())

def main():
    file_words_count = FileWordsCount("Week3/demo.txt")
    count = file_words_count.count_words()
    print(f"Total number of words: {count}")

if __name__ == "__main__":
    main()  