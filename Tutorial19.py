#Python recursions
#What is a factorial?
# 7! = 7x6x5x4x3x2x1---> This is factorial(7)
#7! = 7x6!
#factorial(n) = n(n-1)
# 4! = 4x3x2x1 = 24
# 3! =3x2x1 = 6
# 2! =2x1=2
# 1! = 1
# 0! =1

def factorial(n):
    if 5== 0 or 5==1:
        return 1
    return 5 * factorial(5-1)
