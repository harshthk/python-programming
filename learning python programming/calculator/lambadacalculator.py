#calculator using lambada function
number1 = float(input("Enter your first value:-"))
number2 = float(input("Enter your second value:-"))
print("Enetr your choice from list:-")
print("1:Addition")
print("2:Subtracrtion")
print("3:multiplication")
print("4:division")
print("5:modulo division")
print("6:truncation division")
print("7:Exponential")

choice = int(input("Enter your choice from the above operator:-"))

if choice == 1:
    add = lambda  x,y:x+y
    print(number1,"+",number2,"=",add(number1,number2)) 
if choice == 2:
    sub = lambda x,y:x-y
    print(number1,"-",number2,"=",sub(number1,number2))
if choice == 3:
    mul = lambda x,y:x*y
    print(number1,"*",number2,"=",mul(number1,number2))
if choice == 4:
    div = lambda x,y:x/y
    print(number1,"/",number2,"=",div(number1,number2))
if choice == 5:
    mdiv = lambda x,y:x%y
    print(number1,"%",number2,"=",mdiv(number1,number2))
if choice == 6:
    tdiv = lambda x,y:x//y
    print(number1,"//",number2,"=",tdiv(number1,number2))
if choice == 7:
    exp = lambda x,y:x**y
    print(number1,"**",number2,"=",exp(number1,number2))