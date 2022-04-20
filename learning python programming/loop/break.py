#while loop for break
count = 0
while count <= 5:
    if count ==3:
        break
    else:
        print(count)
    count = count +1
print("Good Bye...")

#while loop for continue
for letter in "harsh":
    if letter == "r":
        break
    else:
        print(letter)
print("Thank You...")