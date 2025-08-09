import random

def generate_random_word():
    word_list = [
        # Programming/Computer related
        "python", "programming", "computer", "algorithm", "data", 
        "science", "machine", "learning", "artificial", "intelligence",
        "software", "development", "coding", "debugging", "testing",
        "database", "network", "security", "cloud", "web", "mobile",
        "application", "interface", "system", "user", "password",
        "encryption", "authentication", "authorization", "session",
        
        # General words
        "hello", "world", "beautiful", "amazing", "wonderful", "fantastic",
        "excellent", "brilliant", "creative", "innovative", "powerful",
        "efficient", "effective", "successful", "productive", "organized",
        "structured", "logical", "analytical", "strategic", "tactical",
        
        # Nature words
        "ocean", "mountain", "forest", "river", "desert", "valley",
        "meadow", "garden", "flower", "tree", "grass", "sky", "sun",
        "moon", "star", "cloud", "rain", "snow", "wind", "storm",
        
        # Animal words
        "elephant", "giraffe", "penguin", "dolphin", "butterfly",
        "dragonfly", "hummingbird", "peacock", "tiger", "lion",
        "dolphin", "whale", "shark", "octopus", "jellyfish"
    ]
    
    return random.choice(word_list)

def getInput():
    while True:
        try: 
            guess = input("Enter a letter: ").strip().lower()
            # Check if input is a single letter
            if len(guess) != 1:
                print("Please enter only one letter!")
                continue
            # Check if input is a letter (a-z)
            if not guess.isalpha():
                print("Please enter a letter (a-z)!")
                continue
            return guess
        except (ValueError, TypeError) as e:
            print(f"Invalid input: {e}")
            continue

def fill_blanks(word, guessed_letters):
    result = word
    for letter in word:
        if letter.lower() not in guessed_letters:
            result = result.replace(letter, "_")
    
    return " ".join(result)

class Guess: 
    def check_guess(self, guess, word, lives):
        if guess in word.lower():
            print(f"Correct! {guess} is in the word")
            return lives
        else:
            print(f"Incorrect! {guess} is not in the word. You have {lives} lives left.")
            return lives - 1

    def all_letters_guessed(self, word, guessed_letters):
        return set(word.lower()).issubset(guessed_letters)

def main():
    guess_class = Guess()
    word = generate_random_word()
    lives = 10
    guessed_letters = set()
    
    print(f"Welcome to Hangman! The word has {len(word)} letters.")
    print(fill_blanks(word, guessed_letters))
    
    while lives > 0:
        guess = getInput()
        
        # Check if letter was already guessed
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'! Try a different letter.")
            continue
            
        lives = guess_class.check_guess(guess, word, lives)
        guessed_letters.add(guess)
        print(fill_blanks(word, guessed_letters))
        
        # Check win condition
        if guess_class.all_letters_guessed(word, guessed_letters):
            print(f"Congratulations! You win! The word was: {word}")
            break
        
        # Check lose condition
        if lives == 0:
            print(f"Game over! You lose! The word was: {word}")
            break

if __name__ == "__main__":
    main()