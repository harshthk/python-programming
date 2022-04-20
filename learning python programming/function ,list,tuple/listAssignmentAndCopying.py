#this is how Assignment work
list1 =[10,20,30,40,50,60,70]
list2 = list1
print(list2)
list1[0] = "harsh"
print(list2)
#this is how copying work
list3 = list(list1)
print(list3)
list1[0] = 5
print(list1)
print(list3)
result = [x**2 for x in [1,2,3,4,5]]
print(result)