import random
from words import words
import string 

class hangman():
    def __init__(self):
        self.word = self.get_valid_word(words)
        self.errors = 0
        self.word_letters = []
        self.used_letters = set()
        for z in self.word:
            self.word_letters.append(z)


    def get_valid_word(self,words):
        self.word = random.choice(words)
        while "-" in self.word or " " in self.word:
            self.word = random.choice(words)

        return self.word.upper()

    def display(self):
        length_of_word = len(self.word)
        hangman_art = {
            0: ("   ",
                "   ",
                "   "),
            1: (" o ",
                "   ",
                "   "),
            2: (" o ",
                "/  ",
                "   "),
            3: (" o ",
                "/| ",
                "   "),
            4: (" o ",
                "/|\\",
                "   "),
            5: (" o ",
                "/|\\",
                "/  "),
            6: (" o ",
                "/|\\",
                "/ \\")}
        for x in hangman_art[self.errors]:
            print(x)
        for y in range(length_of_word):
            if self.word_letters[y] in self.used_letters:
                print(self.word_letters[y], end = " ")
            else:
                print("_", end=" ")
            
        
            
            

    def game(self):
        alphabet = set(string.ascii_uppercase) #set of the english alphabet in upper case
        user_word = set()
        while True:
            guess = input("Guess a letter: ").upper()
            if guess in alphabet - self.used_letters:
                self.used_letters.add(guess)
                if guess in self.word_letters:
                    user_word.add(guess)
                    if len(user_word) == len(self.word_letters):
                        self.display()
                        print("You have won!")
                        return False
                    else:
                        self.display()
                        print(self.used_letters)
                else:
                    self.errors += 1
                    self.display()
                    if self.errors >=6:
                        print("Game over!")
                        print(f"The word was {self.word}")
                        return False
                
my_game = hangman()
my_game.game()
        
