#Calculator made by HARSH THAKOR(ELECTROCODER)
import math
print("Welcome to Electrocoder")
print("Calculator made by HARSH THAKOR (ELECTROCODER)")
print("Enter your choice from the given below:-")
print("1:DMAS CALCULATION")
print("2:NUMBERIC CALCULATION")
choice = int(input("Enter your choice:-"))#here we are giving choice to user
if choice == 1:
    print("DMAS CALCULATION BEGIN")
    number1 = float(input("Enter the first value:-"))
    number2 = float(input("Enter the second value:-"))
    print("Select one of the function which you have to use:-")
    print("1:-Addition")
    print("2:-Subtraction")
    print("3:-Multiplication")
    print("4:-Division")
    print("5:-Modulo Division")
    print("6:-Truncation Division")
    print("7:-Expontenial")
    choice1 = int(input("Enter your choice:-"))
    if choice1 == 1:
        add = lambda  x,y:x+y
        print(number1,"+",number2,"=",add(number1,number2)) 
    if choice1 == 2:
        sub = lambda  x,y:x-y
        print(number1,"-",number2,"=",sub(number1,number2)) 
    if choice1 == 3:
        mul = lambda  x,y:x*y
        print(number1,"*",number2,"=",mul(number1,number2)) 
    if choice1 == 4:
        div = lambda  x,y:x/y
        print(number1,"/",number2,"=",div(number1,number2)) 
    if choice1 == 5:
        mdiv = lambda  x,y:x%y
        print(number1,"%",number2,"=",mdiv(number1,number2)) 
    if choice1 == 6:
        tdiv = lambda  x,y:x//y
        print(number1,"//",number2,"=",tdiv(number1,number2)) 
    if choice1 == 7:
        exp1 = lambda  x,y:x**y
        print(number1,"**",number2,"=",exp1(number1,number2)) 

if choice == 2:
    print("NUMBERIC CALCULATION BEGIN")
    number3 = float(input("Enter the value:-"))
    print("1:Degrees")
    choice2 = int(input("Enter your choice:-"))
    if choice2 == 1:
        deg = math.degrees(number3)
        print(deg)