#read and write in the text file 
file=open("E:\IOT\python programming\python1.txt","r+")
file.write("hello \n how \n are \n friend")
file.close()
#read the text file and output will be shown
file=open("E:\IOT\python programming\python1.txt","r")
print(file.read())
