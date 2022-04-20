# firstly we will learn local variable
def num1():
    n = 10
    print("n for num1 is",n)
def num2():
    n = 20 
    print("n for num2 is",n)
    num1()
num2()

# Secondly we will learn global variable
s = 10

def sum1():
    print("s for sum1 is",s)
def sum2():
    print("s for sum2 is",s)
    sum1()
sum2()

#thirdly we will learn global variable
y = 10 

def yum1():
    print("y for yum1 is",y)
def yum2():
    y = 20
    print('y for yum2 is',y)
    yum1()
yum2()