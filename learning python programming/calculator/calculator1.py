def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
first_number = float(input("Enter the value of number1:"))
second_number = float(input("Enter the value of number2:"))
print("Enter your choice given below")
print("1:Addition")
print("2:Subtraction")
print("3:Multiplication")
print("4:Division")
choice = input("Enter your choice(1/2/3/4):")
if choice == "1":
    print(first_number,"+",second_number,"=",add(first_number,second_number))
if choice == "2":
    print(first_number,"-",second_number,"=",sub(first_number,second_number))
if choice == "3":
    print(first_number,"*",second_number,"=",mul(first_number,second_number))
if choice == "4":
    print(first_number,"/",second_number,"=",div(first_number,second_number))