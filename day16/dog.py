class Dog:
    def __init__(self , name , age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")



my_dog = Dog("Jeff", 12)

print(my_dog.name)

my_dog.roll_over()
my_dog.sit()
