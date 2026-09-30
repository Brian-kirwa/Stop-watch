#composition
class Engine:
    def __init__(self,horse_power):
        self.horse_power = horse_power
class Wheel:
    def __init__(self,size):
        self.size = size
class Car:
    def __init__(self,make,model,horse_power,wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels =[Wheel(wheel_size) for wheel in range(4)]
    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power} (hp){self.wheels[0].size} in"
car1=Car("ford","mustang",500,18)
car2=Car("Toyota","Cavette",600,28)
print(car1.display_car())
print(car2.display_car())
#nested class
class Company:
    class Employee:
     def __init__(self,name,position):
         self.name=name
         self.position=position
     def get_details(self):
         return f"{self.name} {self.position}"
    def __init__(self,company_name):
        self.company_name=company_name
        self.employee=[]
    def add_employee(self,name,position):
        new_employee=self.Employee(name,position)
        self.employee.append(new_employee)
    def list_employee(self):
        return [employee.get_details() for employee in self.employee]
company1=Company("gostigram")
company2=Company("")
company1.add_employee("Toyota","Manager")
company1.add_employee("Eugene","Cook")
company1.add_employee("James","Banana")
for employee in company1.list_employee():
    print(employee)
#static  method and instance method
class Employee:
    def __init__(self,name, position):
        self.name = name
        self.position = position
    def get_info(self):#instance method
        return f"{self.name} = {self.position}"
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook","Janitor"]
        return position in valid_positions #membership operator
employee1 = Employee("James", "Manager")
employee2 = Employee("Kelvin", "Cashier")
employee3 = Employee("Lucy", "Cook")
print(Employee.is_valid_position("Bodyguard"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
#Class methods
class Student:
    count=0
    total_gpa=0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa = gpa
    def get_info(self):#instance method
        return f"{self.name} {self.gpa}"
    @classmethod
    def get_count(cls):
        return f"total number of students:{cls.count}"
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.count/cls.count}"
student1=Student("James", 100)
student2=Student("Jim", 8)
student3=Student("Michael", 2)
print(Student.get_count())
print(Student.get_average_gpa())
#magic & dunder methods
class Book:
    def __init__(self, title, author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    def __add__(self, other):
        return self.num_pages + other.num_pages
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key== "author":
            return self.author
        elif key== "num_pages":
            return self.num_pages
        else:
            return f"Key {key}  was not found"

book1 = Book("My first book", author="kk", num_pages=364)
book2 = Book("My first book", author="kk", num_pages=33)
book3 = Book("My third book", author="mm", num_pages=394)
print(book1)
print(book1==book2)
print(book1<book3)
print(book1>book3)
print(book1+book3)
print("first"in book3)
print(book3["num_pages"])
import time
#Time module Timer
my_time=int(input("Enter the time in seconds: "))
for x in range(my_time,0,-1):
    seconds=x%60
    minutes=int(x/60) %60
    hours=int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIMES UP!")

#shopping cart program in python
foods=[]
prices=[]
total=0
while True:
    food=input("Enter a food to buy (q to quit): ")
    if food.lower()== "q":
        break
    else:
        price=float(input(f"Enter a price of a {food}: $"))
        foods.append(food)
        prices.append(price)
print("------- YOUR CART--------")
for food in foods:
    print(food,end=" ")

for price in prices:
    total +=price
print()
print(f"Your total cost is ${total}")
num_pad=((1,2,3),
         (4,5,6),
         (7,8,9),
         ("*",0,"#"))
for row in num_pad:
    for num in row:
        print(num,end=" ")
    print()

