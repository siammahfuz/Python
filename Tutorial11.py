# Dictionary in Python

dict1 = {
    "name": "Siam",
    "Profession":"Software Engineer ",
    "l": [1, 2, 3, 4, 5]
}

print(dict1["name"])
print(dict1["l"])

#Dictionary functions

print(dict1.get("Profession"))
a = dict1.keys()
a = dict1.values()
a = dict1.items()
print(a)

#dict1.pop("name")// This is for the remove name

#remove last inserted items

dict1["item"] = "value of item"
print(dict1)
dict1.clear()