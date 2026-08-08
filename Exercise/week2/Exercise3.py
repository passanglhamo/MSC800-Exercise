import random


class WordGuessingGame:
    def __init__(self):
        self.word_list = ["python", "java", "javascript", "ruby", "computer", 
                          "programming", "algorithm", "data", "function", "variable"]
        self.secret_word = random.choice(self.word_list)
        self.guessed_letters = []
        self.max_attempts = 6
        self.attempts_left = self.max_attempts

    # This method displays the secret word with guessed letters revealed.
    def display_word(self):
        displayed_word = ''.join([letter if letter in self.guessed_letters else '_' for letter in self.secret_word])
        print(f"Word: {displayed_word}")   

   # This method checks whether the player has guessed every letter.
    def is_word_guessed(self):
        return all(letter in self.guessed_letters for letter in self.secret_word)
    
    # This is the main method of the game.    
    def play(self):
        print("Welcome to the Word Guessing Game!")
        print(f"You have {self.max_attempts} attempts to guess the secret word.")
        while self.attempts_left > 0:
            self.display_word()
            guess = input("Guess a letter: ").lower()
            # Check whether the input is valid
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a singlealphabet.")
                continue
            # Check if the letter was already guessed
            if guess in self.guessed_letters:
                print("You already guessed that letter. Try again.")
                continue
            self.guessed_letters.append(guess)
            # Check if the letter is in the secret word
            if guess in self.secret_word:
                print(f"Good job! '{guess}' is in the word.")
            else:
                self.attempts_left -= 1
                print(f"Sorry, '{guess}' is not in the word. Attempts left: {self.attempts_left}")
            if self.is_word_guessed():
                print(f"Congratulations! You've guessed the word: {self.secret_word}")
                return
        print(f"Game over! The secret word was: {self.secret_word}")    

if __name__== "__main__":
    word_game = WordGuessingGame()
    word_game.play()