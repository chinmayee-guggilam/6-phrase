'''Define a class, which have a class parameter and have a same instance 
parameter'''
#Code
class MyClass:
    class_parameter = "Class Parameter"

    def __init__(self, instance_parameter):
        self.instance_parameter = instance_parameter

    def print_parameters(self):
        print("Class Parameter:", self.class_parameter)
        print("Instance Parameter:", self.instance_parameter)


# Create instances of MyClass
instance1 = MyClass("Instance 1 Parameter")
instance2 = MyClass("Instance 2 Parameter")

# Access and modify the class parameter
print("Class Parameter (before modification):", MyClass.class_parameter)
MyClass.class_parameter = "Modified Class Parameter"
print("Class Parameter (after modification):", MyClass.class_parameter)

# Access the instance parameters
instance1.print_parameters()
instance2.print_parameters()

#Output
'''Class Parameter (before modification): Class Parameter
Class Parameter (after modification): Modified Class Parameter
Class Parameter: Modified Class Parameter
Instance Parameter: Instance 1 Parameter
Class Parameter: Modified Class Parameter
Instance Parameter: Instance 2 Parameter'''
