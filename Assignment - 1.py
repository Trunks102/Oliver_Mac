#1. Create variables with any Object using various Naming Conventions
my_variable = "lower case"
MY_VARIABLE = "UPPER CASE"
My_Variable = "Snake Case"

import math
print(dir(math))

#2. Explore dir() and help()
import math
print(help(math))

import math
print(dir(math))

#3. List out available attributes for dir()
class MyClass:
    def method1(self):
        pass
    def method2(self):
        pass
print(dir(MyClass))

instance = MyClass()
print(dir(instance))

#4. Attributes using help() in python
import math
help(math)

class MyClass:
    def method1(self):
        pass
    def method2(self):
        pass
help(MyClass)

obj = MyClass
help(obj)