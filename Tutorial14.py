#Loops in Pytho
#There are 2 types of loops in Python 1. For loops 2. While loops

# A loop is used to execute a set of statement as long as a given condition is true

for i in range(10000000):
    print(i)

# Iterating a list using for loops
myList =["This", "That", "Siam", "Perfect", 25]
for item in myList:
    print(item)


#Iterating a tuple
myTuple =(1, 2, 3, 4,5, 'Siam')
for item in myTuple:
    print(item)

myDict = {
    "name" : "Siam",
    "Color": "Blue",
    "marks": 100
}
#if you try to iterate through the dictionary, you will get keys bu default
#Iterating to get keys as well as the corresponding values

for key, value in myDict.item():
    print(f"The key is {key} and the value is {value}")

Mydict = {
    "Siam" : 5,
    "kanto" : 8,
    "Naeem" : 10,
    "Shakib" : 4,
    "Tamim" : 3
}

for key, value in Mydict.items():
    print(f"The grade for {key} is {value}")
