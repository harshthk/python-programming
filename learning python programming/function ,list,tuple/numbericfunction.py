#numeric functions like absolute ceil floor round and trunc
a = abs(5)#here absolute is used for showing the position of value from the zero
print(a)
b = round(4.5456465456456456,4)#here round function is used for the rounding the value 
print(b)  
c = round(3.54785184,4)
print(c)
##now for using function ceil floor and trunc we have to import math
import math
d = math.ceil(4.2)#here if we give value 4.2 and used function ceil then it will give answer 5 because it automatically select next higher number
print(d)
e = math.ceil(-3.5)#here if we give value -3.5 and used function ceil then it will give answer -3 
print(e)
f = math.floor(4.5)#here if we give value 4.5 and used function floor then it will giver answer 4 becaus it will automatically select next lower number
print(f)
g = math.floor(-3.5)
print(g)
h = math.trunc(4.5)#here if we give value 4.5 and used function trunc then it will give answer 4.5 then it will give answer 4 because it will ignore point 
print(h)
i = math.trunc(-3.5)
print(i)