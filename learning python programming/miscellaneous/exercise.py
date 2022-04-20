actual_number = 45

guess = 0

while True:
    guess = guess +1
    guess_number = int(input("Enter your guessing number:-"))
    if guess_number < actual_number:
        print("Your guessing is lower then actual number")
    elif guess_number > actual_number:
        print("Your guessing is higher then actual number")
    else:
        print(f"your attempt for this games is {guess}")
        break
print("Thank You for playing")