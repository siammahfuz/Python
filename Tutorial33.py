#Employee  --> Salary,

# Employee
# student

#noun  --> Classes 
#adjective ---->attributes
#verb -->methods


class Employee:
    salary = 34
    name = "siam"
    def getSalary(self):
        return self.salary


e1 = Employee() #Creating an object of e1 of class employee
e1.salary = 766
print(e1.salary)