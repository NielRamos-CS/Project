import string
import random
import time

class WordGuesser:
    def __init__(self, target):
        self.target = target
        self.possible_characters = string.ascii_letters + string.digits + string.punctuation + " "  # Include space
        self.result = ["_"] * len(target)  # List of underscores representing unguessed letters
        self.attempts = 0

    def guess_character(self, target_char, index):
        while True:
            guess = random.choice(self.possible_characters)
            self.attempts += 1
            if guess == target_char:
                return guess
            # Continue looping until the correct character is found

    def guess_word(self):
        for index, target_char in enumerate(self.target):
            guessed_char = self.guess_character(target_char, index)
            self.result[index] = guessed_char
            # Print the current state of the word with spaces between characters
            print(" ".join(self.result), end="\r")
            time.sleep(0.1)  # Sleep for a brief moment to simulate typing effect

        return "".join(self.result)

# User input and calling the class
target_word = input("Enter a word to guess: ")
word_guesser = WordGuesser(target_word)
result = word_guesser.guess_word()

# Final output with spaces between letters
print(f"\nWord guessed correctly: {' '.join(result)}")
print(f"Total attempts: {word_guesser.attempts}")
