#replace operator in listoperation...
list1 = [1,2,3,4,5,6,7,8,9]
list1[2]=4.5
print(list1)

#insert operator in listoperation...
list2 = [1,2,3,4,5,6,7,8,9]
list2.insert(3,"hello") #inserting string at the position2
list2.insert(5,4.5)
print(list2)

#sort operation in list...
car =["BMW","Maruti","Volvo","Suzuki","Volkwegen","Fiat"]
car.sort()#sort operation in listoperation  (for string)
print(car)

number =[25,45,55,35,65,75,15,5,10,15]
number.sort()#sort operation in listoperation (for numbers)
print(number)

number1=["2.0","2.5","3.5","1.5","1.2"]
number1.sort()#sort operation in listoperation (for decimal number)
print(number1)

#delete operation in list...
name=["harsh","sunny","thakor"]
del name[1]#delete function in listoperation
print(name)
name.append("POPEYE")#append function in listoperation
print(name)
name.reverse()
print(name)
