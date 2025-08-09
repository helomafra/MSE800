# Week 2 - Activity 3: Write a project to look for a character in an string using Class
# You can develop the code using the attached file as a hint, then add a method to print the string's length and convert it to uppercase.
 
class StringManipulation:
    def length(self, text):
        return len(text)

    def uppercase(self, text):
        return text.upper()

    def find_character(self, text, character):
        return text.find(character)

def main():
    text = "coding"
    character = "g"
    string_manipulation = StringManipulation()

    char_position = string_manipulation.find_character(text, character)
    print(f"The character {character} is in the text at position {char_position}")

    text_length = string_manipulation.length(text)
    print(f"The length of the string is {text_length}")

    text_uppercase = string_manipulation.uppercase(text)
    print(f"The uppercase of the string is {text_uppercase}")

if __name__ == "__main__":
    main()