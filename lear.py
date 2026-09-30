#class variables
class Student:
    class_year=2025
    num_student=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.num_student+=4
student1=Student("James",18)
student2=Student("kelvin",29)
print(student1.name)
print(student2.name)
print(Student.class_year)
print(Student.num_student)
print(f"The year of {Student.class_year}  has  {Student.num_student} students")
#inheritance
class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive=True
    def eat(self):
        print(f"{self.name} eating")
    def sleep(self):
        print(f"{self.name} sleeping")
class Dog(Animal):
    def speak(self):
        print("wolf")
class Cat(Animal):
    def speak(self):
        print("Meow")
class Mouse(Animal):
    def speak(self):
        print("Squeek")
dog=Dog("Scooby")
cat=Cat("Galfield")
mouse=Mouse("Bob")
print(dog.is_alive,)
cat.eat()
cat.speak()
#multiple and multilevel inheritance
class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f"This animal {self.name} is eating")
    def sleep(self):
        print(f"This animal {self.name}is sleeping")
class Prey(Animal):
    def flee(self):
        print(f"This animal{self.name} is fleeing")
class Predator(Animal):
    def hunt(self):
        print(f"This animal{self.name} is hunting")
class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):
    pass
rabbit=Rabbit("Bob")
hawk=Hawk("Tobby")
fish=Fish("Tilapia")
rabbit.flee()
#abstract class method
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print("Car is going")

    def stop(self):
        print("Car is stopping")


class Truck(Vehicle):
    def go(self):
        print("Truck is going")

    def stop(self):
        print("Truck is stopping")


truck = Truck()
truck.go()
truck.stop()
#super function
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    def describe(self):
        print(f"{self.color} and {'filled'if self.is_filled else  not 'filled'}")
class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius=radius
#method overidding
    def describe(self):
        print(f"Its a circle with an area of {3.14*self.radius} cm^2")
        super().describe()
class Square(Shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width,height):
        super().__init__(color,is_filled)
        self.width = width
        self.height = height
circle=Circle("red",True,5)
print(circle.color)
circle.describe()
#polymorphism
from abc import ABC,abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14 * self.radius
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
            return  self.side^2

class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return 0.5* self.base*self.height
class Pizza(Circle):
    def __init__(self,topping,radius):
        super().__init__(radius)
        self.topping=topping
shapes=[Circle(4),Square(5),Triangle(6,7),Pizza("peppetroni",2)]
for shape in shapes:
    print(f"{shape.area()}cm^2")
#Duck Typing
class Animal:
    alive=True
class Dog(Animal):
    def speak(self):
        print("WOOF")
class Cat(Animal):
    def speak(self):
        print("MEOW")
class Car:
    alive=False
    def speak(self):
        print("HONK")
animals=[Dog(),Cat(),Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
#aggregation
class Library:
    def __init__(self,name):
        self.name = name
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
    def list_books(self):
        return [f"{book.title} by {book.author}"for book in self.books]
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
library=Library("New yolk public library")
book1=Book("Harry Potter","J.K")
book2=Book("Hobbi","Tolkein")
book3=Book("The color of magic","Terry")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
for book in library.list_books():
    print(book)
