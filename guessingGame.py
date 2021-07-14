import random
number = random.randint(1,9)
chances = 0

while chances < 5:
    guess1 = int(input("Enter Your Guess:"))
    if guess1 == number:
        print("Outstanding, You guessed the number in the 1st Chance")
        chances = chances + 1
        break
    else:
        print("Oh! you missed but don't worry you still have four more guesses")

    guess2 = int(input("Enter Your Guess:"))
    if guess2 == number:
        print("Excellent, You guessed the number in the 2nd Chance")
        chances = chances + 1
        break
    else:
        print("Oh! you missed but don't worry you still have three more guesses")

    guess3 = int(input("Enter Your Guess:"))
    if guess3 == number:
        print("Very Good, You guessed the number in the 3rd Chance")
        chances = chances + 1
        break
    else:
        print("Oh! you missed but don't worry you still have two more guesses")

    guess4 = int(input("Enter Your Guess:"))
    if guess4 == number:
        print("Good, You guessed the number in the 4th Chance")
        chances = chances + 1
        break
    else:
        print("Oh! you missed, now you have your last chance")

    guess5 = int(input("Enter Your Guess:")) 
    if guess5 == number:
        print("Well, You finally guessed the number")
        chances = chances + 1
        break
    else:
        print("OH!! You lost, better luck next time and the number is, ", number)
        break



