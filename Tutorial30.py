print('Welcome to List Comprehensions')

myFood = ['Apple', 34, 'Oranges', 'Water melons']

nonInt =[]

#without using List comprehensions
for item in myFood:
    if not item.isdigit():
      nonInt.append(item)
print(nonInt)


#Using list comprehensions
nonInt2 = [item for item in myFood if str(item).isdigit()]
print(nonInt2)