import random
user = random.randint(1,100)
print(user)
guess = 0
intermidate = 5
advance = 2
extraodinary = 1
while True:
    guess = guess +1
    guess_number = int(input("Enter your guessing number:-"))
    if guess_number < user:
        print("Your guessing number is lower then actual number")
    elif guess_number > user:
        print("Your guessing nunber is greater then actual number")
    else:
        print(f"Your attempt for this game is {guess}")
        if guess == extraodinary:
            print("You win this game and you get discount of 100%")
        elif guess == advance:
            print("You win this game and you get discount of 50%")
        elif guess == intermidate:
            print("You win this game and you get discount of 25%")
        else:
            print("You try your level best but you loose this game")
        break
    
print("Thank you for playing")
 
