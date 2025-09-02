#1.Define a class with arithmetic operations
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b
    
    def div(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Division by zero not allowed"


# Create two objects
obj1 = Calculator(10, 5)
obj2 = Calculator(20, 4)

# Add new attributes dynamically
obj1.model_num = "M1234"
obj1.made_in = "India"

obj2.color = "Red"
obj2.discount = "10%"

# Call arithmetic methods
print("Object 1 Operations:")
print("Add:", obj1.add())
print("Sub:", obj1.sub())
print("Mul:", obj1.mul())
print("Div:", obj1.div())

print("\nObject 2 Operations:")
print("Add:", obj2.add())
print("Sub:", obj2.sub())
print("Mul:", obj2.mul())
print("Div:", obj2.div())

# Print required details
print("\nDetails:")
print("Obj1 -> Model Num:", obj1.model_num, ", Made In:", obj1.made_in)
print("Obj2 -> Color:", obj2.color, ", Discount:", obj2.discount)



#2. define self
#self---self is a reference to the current instance of the class.
#It is used to access the attributes (variables) and methods (functions) of that specific object.
class Example:
    def __init__(self, name):
        self.name = name   # self.name → instance variable

    def show(self):
        print("Name is:", self.name)

obj = Example("Chandaswi")
obj.show()
