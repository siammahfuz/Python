#What is a function?
#f(x) = x^2 + 2
#f(1) = 4
#f(0) = 2

from html.entities import name2codepoint


def greet(name):
    print(f"Hey good morning, {name}")
    #return 0


name = "Siam"
name1 = "Shovon"
name2 = "Sazon"

greet(name)
greet(name1)
greet(name2)

print(greet)


def add(num1, num2):
    sum1 = num1 + num2
    return sum1

a = 45
b = 6
c = add(a, b)
print(c)

