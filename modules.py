from lib.classes import Student
s1 = Student("Himanshu", 21, "GU12345")  # ✅ Creates an object
s1.show()  # ✅ Calls instance method with self = s1   
#Because student.show() is an instance method, it needs an object to provide the self value.
import lib.classes as classes

# Then access like:
p =classes.Perso("Ram", 40)
p.greet()

s =classes.Student("Himanshu", 21, "GU12345")
s.show()
s.show_id()
#this for imoprt .py from other folder

#this for both .py file same folder


""" import classes

# Then access like:
p = classes.Perso("Ram", 40)
p.greet()

s = classes.Student("Himanshu", 21, "GU12345")
s.show()
s.show_id()
#from classes import Perso, Student """