'''Assignment on Class -04

1. A = { 55, 6, 8, 9, 11} , B = {44, 55, 89,54} apply set union.
2. Which data type not allow duplicate item. Give an example.
3. B={‘Django’: 16, ‘Project’: 8, ‘Students’: 20} print keys.
4. Create a function & call the function.
5. Create Class & Object.
6. Give an example of Inheritance.'''


#1. A = { 55, 6, 8, 9, 11} , B = {44, 55, 89,54} apply set union.
A = { 55, 6, 8, 9, 11}
B = {44, 55, 89,54}
C = A.union(B)
print('Union of set operation: ',C)


#2. Which data type not allow duplicate item. Give an example.
     #Sets cannot have two items with the same value.
     #Example
duplicateset = {"apple", "banana", "cherry", "apple"}

print('Not allowed duplicate item: ',duplicateset)


#3. B={‘Django’: 16, ‘Project’: 8, ‘Students’: 20} print keys.
B={'Django': 16, 'Project': 8, 'Students': 20}
#print keys

x = B['Django']
print(x)

#get
x = B.get('Project')
print(x)
x = B.get('Students')
print(x)
#key()
x = B.keys()
print(x)
#value
x = B.values()
print(x)

#4. Create a function & call the function.

def my_function():
  print("Hello from a function")

my_function()


#5. Create Class & Object.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " , self.name,"and age is", self.age)

p1 = Person("Rakib", 25)
p1.myfunc()

#6. Give an example of Inheritance.
'''Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.'''

# create a parent class
class A:
  def parent(self):
    print('Rakib1')

  def parents(self):
    print('Uddin2')


class B(A):
  def child(self):
    print('Rakib3')

  def childs(self):
    print('Rakib4')


a = A()
a.parents()

b = B()
b.parents()

