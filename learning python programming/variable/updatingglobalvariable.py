#updating global variable
num = 10
def function():
    global num # here we are writing global because we are telling python that num is a global variable
    num = num + 1
    print("num for function is",num)
function()

#error will be shown because we don't write global in define function
summ = 10
def var(): #local variable 'summ' referenced before assignment
    summ = summ +1
    print("sum for var is",var)
var()