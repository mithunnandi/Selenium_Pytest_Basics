class Addition:

    wheels=9


    # parameterized constructor
    def __init__(self, f, s):
        print("WELCOME")
        self.first = f
        self.sec = s

    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.sec))
        print("Addition of two numbers = " + str(self.add))

    def calculate(self):
        self.add = self.first + self.sec


# creating object of the class
# this will invoke parameterized constructor
obj = Addition(1000, 2000)

# perform Addition
obj.calculate()
print(obj.wheels)

# display result
obj.display()