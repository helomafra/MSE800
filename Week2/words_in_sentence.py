# Week 2 - Activity 5: Develop a project to work with Strings
# Develop a project using class and methods to get a sentence from user input and find the number of words in it. Share your GitHub link at the end.

class WordsInSentence:
    def get_input(self):
      sentence = input("Enter a sentence: ")
      return sentence

    def count_words(self, sentence):
        return len(sentence.split())

def main():
    words_in_sentence = WordsInSentence()
    sentence = words_in_sentence.get_input()
    count = words_in_sentence.count_words(sentence)
    print(f"The number of words in the sentence is {count}")

if __name__ == "__main__":
    main()