#Always remember that for tuples () this brackets are used
#In tuples operation like reverse,append,delete,insert,sort,replace we can't use it will show an attribute error
#lets make a tuple..
car = ("Ford","Maruti","Honda","Suzuki","Elentra")
print(car)
name=(("harsh","sunny","thakor"),("ktm","mathur","popeye"))
print(name)
print(name[0][0])
name.append("Harshthakor")#It will show an error because we can't use append in tuple.
print(name)
name.reverse()
print(name)