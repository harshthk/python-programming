# continue for while loop...
count = 0
while count <=5:
    count =count+1
    if count ==3:
        continue
    print(count)
print("Good Bye...")

#decrement while loop with continue
count = 10
while count >0:
    count = count-1
    if count == 5:
        continue
    print(count)
print("Good Bye...")

#continue for for loop
for letter in "harsh":
    if letter == "r":
        continue
    print(letter)
print("Thank You...")