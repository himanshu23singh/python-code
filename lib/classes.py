# class Person:
 
#     # Constructor method (runs when object is created)
#     def __init__(self, name, age):
#         self.name = name  # instance variable
#         self.age = age

#     # A method to greet
#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")#here self is compulsary

# # Creating an object of the class
# p1 = Person("Himanshu", 21)

# Calling the method
# p1.greet()



class Perso:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old. [From Person]")

# Child class
class Student(Perso):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Calls Person's __init__
        self.student_id = student_id

    def show(self):  # Overriding the greet method
        super().greet()  # Call parent class greet()
        print(f"I am also a student with ID: {self.student_id} [From Student]")

    def show_id(self):
        print(f"My student ID is {self.student_id}")

# Create object
s1 = Student("Himanshu", 21, "GU12345")

# Call methods
s1.show()      # Both parent and child greet will be shown
s1.show_id()    # Only in child