#different ways to connect dictionaries...
dic1 = {1:"HARSH",2:"SUNNY",3:"KTM"}
print(dic1)
#first making the empty dict and then adding the value...
dict2 = {}
dict2[1] = "harsh"
dict2[2] = "sunny"
dict2[3] = "ktm"
print(dict2)

#making dict using tuples...
dict3 = dict([(1,"harsh"),(2,"sunny"),(3,"ktm")])
print(dict3)

#making dict parallel
a = [1,2,3] 
b = ["harsh","sunny","ktm"]
dict4 = {}
for i in range(len(a)):
    dict4[a[i]]=b[i]
    print(dict4)