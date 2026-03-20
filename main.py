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



if __name__ == "__main__":

    number_guesser = NumberGuesser()

    a, b = map(int, input("Insert two numbers: ").split())

    number_guesser.start_game(a, b)



# number = random.randint(1, 100)
# user_number = None

# while number != user_number:
#     user_number = int(input("Insert a number: "))

#     if number > user_number:
#         print("Your number is lower that the real number!")
#     elif number < user_number:
#         print("Yout number is bigger that the real number!")
#     else:
#         print("You choose the correct number!")



