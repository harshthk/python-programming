#defining the Arithmetic operator for calculator
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def tdiv(x,y):
    return x//y
def mdiv(x,y):
    return x%y
def exp(x,y):
    return x**y
#Entering number manually
number1=float(input("Enter the value of number1:"))
number2=float(input("Enter the value of number2:"))
#Printing the choice
print("Select one of your choice given below:")
print("1:Addition")
print("2:Subtraction")
print("3:Multipliaction")
print("4:Division")
print("5:Truncating Divison")
print("6:Modulo Division")
print("7:Exponential")
choice = input("Enter your choice:")
#Selecting choice from the above choicoe
if choice == "1":
    print(number1,"+",number2,"=",add(number1,number2))
if choice == "2":
    print(number1,"-",number2,"=",sub(number1,number2))
if choice == "3":
    print(number1,"*",number2,"=",mul(number1,number2))
if choice == "4":
    print(number1,"/",number2,"=",div(number1,number2))
if choice == "5":
    print(number1,"//",number2,"=",tdiv(number1,number2))
if choice == "6":
    print(number1,"%",number2,"=",mdiv(number1,number2))
if choice == "7":
    print(number1,"**",number2,"=",exp(number1,number2))