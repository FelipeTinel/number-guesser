import random


class NumberGuesser:

    def __init__(self):

        self.random_number = None
        self.user_number = None
        self.tries = 0

    
    def _tries_counter(self):
        self.tries += 1
        print(f"Tries: {self.tries}")

    def start_game(self, min_number, max_number):
        
        self.random_number = random.randint(min_number, max_number)

        while self.user_number != self.random_number:

            self.user_number = int(input("Try a number: "))

            if self.user_number < self.random_number:
                print("The number that you tried is lower that the correct one!\n")
                self._tries_counter()

            elif self.user_number > self.random_number:
                print("The number that you tried is bigger that the correct one!\n")
                self._tries_counter()

            else:
                print(f"You find it! With {self.tries} tries!")







