# introduction
# module
# basic datatypes
# variables (primitive , non-primitive datatype)
# string , different functions in string
# practice session in previous topics
# functions
# oops concepts:
# class , objects
# 4 pillars (abstraction, encapsulation , polymorphism , inheritance)


# variable
# a = 10
# b = True
# print(a)
# print(b)

# str = 'Sourik'
# print(str)
# f = 01.543
# print(f)
# print(type(str))

# a += 1
# a++, ++a

# x = int(input('Please input a value'))
# print(x)
# print(type(x))

# string
# s = "kolkata"
# print(len(s))
# print(s)

# #concatenate
# x = s + 'bangalore'
# print(x)
# print(s[0])
# # print(s[-1])
# # print(s[5])
# # print(s[-4])

# # print(x.count('k'))

# # list = ['india', 10 , 'Virat Kohli', True]
# # print(list)
# # print(list[0])
# # list.append('Hackerrank')

# # print(list)


# l = [98,56, 39, 52 ,76]
# print(l)
# l.sort()
# print(l)
# l.reverse()
# print(l)
# l.insert(2,100)
# print(l)
# l.pop()
# print(l)
# l.remove(76)
# print(l)

#dictionery

# dict01 = { "name" : "LionelMessi" ,
#             "Country" : "Argentina",
#             "jerseynumber" : 10 ,
#             "WorldCup" : 1
#         }
       
# print(dict01)
# print(dict01['Country'])
# print(dict01.keys())
# print(dict01.items())

# dict01.update({"club" : "Barcelona"})
# dict01["Brand"] = "Adidas"
# print(dict01.items())

# s = {1, 1, 5, 6, 8,13}
# print(s)
# s.add(99)
# print(s)
# s.remove(5)
# print(s)

# t = { 8, 88, 13, 25 ,56 }
# print(len(t))

# union = s.union(t)
# print(union)

# intersection = s.intersection(t)
# print(intersection)


# print(t)
# t.pop()
# print(t)

#conditional expression
marks = int(input('Enter mark'))
if marks > 90:
    print('Passed')
elif marks < 90 and marks > 60:
    print('Half passed')
else:
    print('Failed')
   
   

#datatype
# float, boolean , string, integer , none

# error handling
# practice sessions : hackerrank
# pdf notes : harry code repo, harry python notes
# def f1():
#     return "Kolkata"
# x = f1()
# print(x)

# def s1(a,b):
#     return 2*(a+b)
   
# y = s1(10,20)
# print("Result", y)

# def recursivefunction(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * recursivefunction(n-1)
# print(recursivefunction(5))

 # class define
   
    # def __init__(self, model, brand):
    #     self.model = model  # Instance attribute
    #     self.brand = brand  # Instance attribute
       


# class Bike:
   
#     color = "red"
#     wheels = 2
   
#     def speed(self):
#         return "Today is Sunday"
       
# b1 = Bike()

# print(b1.color)
# print(b1.wheels)
# print(b1.speed())
# 4 pillars (abstraction, encapsulation , polymorphism , inheritance)



       
# class Duke(Bike):
#     def speed(self):
#         print("Spped method call")

# objectname = Classname(passArgument)        
# b1 = Bike("Duke 200", 'KTM')
# print(b1.model)
# print(b1.brand)
# # print(b1.category)

# oops (inheritance , encapsulation , abstraction , polymorphism )
# access modifiers
# inheritance : grandfather -> father -> child

# class Parent:
#     def parentMethod(self):
#         print("ParentMethod Called")
       
# class Child(Parent):
#     def childMethod(self):
#         print("ChildMethod called")
       
# c1 = Child()
# print(c1.parentMethod())
# print(c1.childMethod())
# p1 = Parent()
# # print(p1.childMethod())
# print(p1.parentMethod())

#encapsulation
# class Student:
#   def __init__(self, name="Rajaram", marks=50):
#       self.name = name
#       self.marks = marks

# s1 = Student()
# s2 = Student("Bharat", 25)
# print(s1.name, s1.marks)
# print(s2.name,s2.marks)

#polymorphism
# class Shape:
#     def area(self):
#         return "Undefined"

# #multilevel inheritance 1
# class Rectangle(Shape):
#     #constructor in rectangke class
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

# #mulitlevel inheritance 2
# class Circle(Shape):
   
#     #circle contructor
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2
       
# r = Rectangle(10,20);
# print(r.area())
# c = Circle(10)
# print(c.area())

# error handling : exception handling
# try:
#     n = 25
#     res = 250 / n
#     # exception handling
# except ZeroDivisionError:  
#     print("You can't divide by zero!")
   
# else:
#     print("Result is", res)
   
# finally:
#     print("Execution complete.")
   
# print(100/0)
