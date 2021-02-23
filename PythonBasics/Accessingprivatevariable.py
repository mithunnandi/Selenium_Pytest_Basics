class Employee:
     #hidden data member of employee class
    __salary=1000

e1=Employee()

#print(e1.__salary)--This is not the way to access hidden private variable

print(e1._Employee__salary) # Accessing private hidden variable by using tricky syntax
