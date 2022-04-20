#variable length argument is used when you don't know how many function you have to define
#for define varibale length argument in function we will used * and then variable namepython
def function(*mylist):
    for x in mylist:
        print(x)
    return
function(10,2,30,4,0)
function("harsh","sunny","thakor")
function(10,5,2.5,"harsh")