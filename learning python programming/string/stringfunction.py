#function for find,length,split and title
name = "electro coder"
#find function
print(name.find("e"))#find function in which it was showing the position of d
print(name.find("coder"))#find function in which it was showing the position of coder 
#length function
print(len(name)-1)#here will are getting 13 number then we are subtracting one from it for getting the answer 12
print(name.split())#here split will be work as it will split name for eg if you had written Electro coder so there will be space between both so it will split them
print(name.title())

#function for lower,upper,islower and iupper
#name = "electro coder"
print(name.upper()) 
print(name.lower())
print(name.isupper())
print(name.islower())

#function for replace,isdigit,isalpha
name1 = "harsh"
name2 = "8866044887"
name3 = "hello sir my name is jarvis"
name4 = "8866hhjfb"
#replace function in string
print(name1.replace("a","s"))
print(name3.replace("name","kame"))
##isdigit function in string
print(name1.isdigit())
print(name2.isdigit())
print(name4.isdigit())
#isalpha function in string
print(name1.isalpha())
print(name3.isalpha())
print(name4.isdigit())

#function for strip,lstrip,rstrip
name5 = "!!!!!harsh!!!!!"
print(name5.strip("!"))
print(name5.lstrip("!"))
print(name5.rstrip("!"))
name6 = "@@@@harsh@@@"
print(name6.strip("@"))