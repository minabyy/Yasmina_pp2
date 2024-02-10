#Python Booleans

#Task 1
print(10 > 9)
#Answer: True

#Task 2
print(10 == 9)
#Answer: False

#Task 3
print(10 < 9)
#Answer: False

#Task 4
print(bool("abc"))
#Answer: True

#Task 5
print(bool(0))
#Answer: False

#Python Operators
#Task 1 Multiply 10 with 5, and print the result.
print(10 * 5)
#Result: 50

#Task 2 Divide 10 by 2, and print the result.
print(10 / 2)
#Result: 5

#Task 3 Use the correct membership operator to check if "apple" is present in the fruits object.
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#Task 4 Use the correct comparison operator to check if 5 is not equal to 10.
if 5!=10:
  print("5 and 10 is not equal")

#Task 5 Use the correct logical operator to check if at least one of two statements is True.
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")


#Python Lists

#Task 1 Print the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
print(fruits[2])

#Task 2 Change the value from "apple" to "kiwi", in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#Task 3 Use the append method to add "orange" to the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#Task 4 Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

#Task 5 Use the remove method to remove "banana" from the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#Task 6 Use negative indexing to print the last item in the list.
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#Task 7 Use a range of indexes to print the third, fourth, and fifth item in the list.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#Task 8 Use the correct syntax to print the number of items in the list.
fruits = ["apple", "banana", "cherry"]
print(len(fruits))


#Python Tuples

#Task 1 Use the correct syntax to print the first item in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#Task 2 Use the correct syntax to print the number of items in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#Task 3 Use negative indexing to print the last item in the tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#Task 4 Use a range of indexes to print the third, fourth, and fifth item in the tuple.
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])


#Python Sets

#Task 1 Check if "apple" is present in the fruits set.
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#Task 2 Use the add method to add "orange" to the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#Task 3 Use the correct method to add multiple items (more_fruits) to the fruits set.
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#Task 4 Use the remove method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#Task 5 Use the discard method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")


#Python Dictionaries 

#Task 1 Use the get method to print the value of the "model" key of the car dictionary.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#Task 2 Change the "year" value from 1964 to 2020.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"]
 = 
2020

#Task 3 Use the pop method to remove "model" from the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

#Task 4 Use the pop method to remove "model" from the car dictionary.
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.pop("model")

#Task 5 Use the clear method to empty the car dictionary.
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.clear()


#Python If...else

#Task 1 Print "Hello World" if a is greater than b.
a = 50
b = 10
if a>b:
    print("Hello World")

#Task 2 Print "Hello World" if a is not equal to b.
a = 50
b = 10
if a != b:
    print("Hello World")

#Task 3 Print "Yes" if a is equal to b, otherwise print "No".
a = 50
b = 10
if a == b:
    print("Yes")
else:
    print("No")

#Task 4 Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
a = 50
b = 10
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")

#Task 5 Print "Hello" if a is equal to b, and c is equal to d.
if a == b and c == d:
    print("Hello")

#Task 6 Print "Hello" if a is equal to b, or if c is equal to d.
if a == b or c == d:
    print("Hello")

#Task 7 Complete the code block, print "YES" if 5 is larger than 2. Hint: remember the indentation.
if 5 > 2:
    print("YES")

#Task 8 Use the correct one line short hand syntax to print "YES" if a is equal to b, otherwise print("NO").
a = 2
b = 5
print("YES") if a == b else print("NO")

#Task 9 Use an if statement to print "YES" if either a or b is equal to c.
a = 2
b = 50
c = 2
if a == c or b == c:
    print("YES")

#Python While Loop

#Task 1 Print i as long as i is less than 6.
i = 1
while i < 6:
    print(i)
    i += 1

#Task 2 Stop the loop if i is 3.
i = 1
while i < 6:
    if i == 3:
        break
    i += 1

#Task 3 In the loop, when i is 3, jump directly to the next iteration.
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#Task 4 Print a message once the condition is false.
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


#Python For Loops

#Task 1 Loop through the items in the fruits list.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#Task 2 In the loop, when the item value is "banana", jump directly to the next item.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#Task 3 Use the range function to loop through a code set 6 times.
for x in range(6):
    print(x)

#Task 4 Exit the loop when x is "banana".
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)


#Python Functions

#Task 1 Create a function named my_function.
def my_function():
    print("Hello from a function")

#Task 2 Execute a function named my_function.
def my_function():
    print("Hello from a function")
my_function()

#Task 3 Inside a function with two parameters, print the first parameter.
def my_function(fname, lname):
    print(fname)

#Task 4 Let the function return the x parameter + 5.
def my_function(x):
    return x + 5

#Task 5 If you do not know the number of arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?
def my_function(*kids):
    print("The youngest child is " + kids[2])

#Task 6 If you do not know the number of keyword arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?
def my_function(**kid):
    print("His last name is " + kid["lname"])


#Python Lambda 

#Task 1 Create a lambda function that takes one parameter (a) and returns it.
x = lambda a : a


#Python Classes 

#Task 1 Create a class named MyClass:
class MyClass: x = 5

#task 2 Create an object of MyClass called p1:
class MyClass:
    x = 5
p1 = MyClass()

#Task 3 Use the p1 object to print the value of x:
class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)

#Task 4 What is the correct syntax to assign a "init" function to a class?
class Person: 
    def __init__(self, name, age):
    self.name = name
    self.age = age


#Python Inheritans

#Task 1 What is the correct syntax to create a class named Student that will inherit properties and methods from a class named Person?
class Student(Person):

#Task 2 We have used the Student class to create an object named x. What is the correct syntax to execute the printname method of the object x?
class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()

#Python Modules

#Task 1 What is the correct syntax to import a module named "mymodule"?
import mymodule

#Task 2 If you want to refer to a module by using a different name, you can create an alias. What is the correct syntax for creating an alias for a module?
import mymodule as mx

#Task 3 What is the correct syntax of printing all variables and function names of the "mymodule" module?
import mymodule
print(dir(mymodule))

#Task 4 What is the correct syntax of importing only the person1 dictionary of the "mymodule" module?
from mymodule import person1 