class MyClass:
    def __init__(self, value):
        self.value = value

    def get_class_name(self):
        return self.__class__.__name__

# Create an instance of MyClass
my_object = MyClass(10)

# Call the method to get the class name
class_name = my_object.get_class_name()
print(class_name)