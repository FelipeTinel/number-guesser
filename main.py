import random

number = random.randint(1, 100)
user_number = None

while number != user_number:
    user_number = int(input("Insert a number: "))

    if number > user_number:
        print("Your number is lower that the real number!")
    elif number < user_number:
        print("Yout number is bigger that the real number!")
    else:
        print("You choose the correct number!")



