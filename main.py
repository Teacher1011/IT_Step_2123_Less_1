"""class Student:
    print("Hi")
    def __init__(self):
        self.height = 160
        print("I am alive")

first_student = Student()
"""
import math
from datetime import datetime

"""
class Student:
    amount_student = 0
    def __init__(self, height = 160):
        self.height = height
        Student.amount_student += 1
nick = Student()
kate = Student(height=170)
print(nick.amount_student)
print(Student.amount_student)
"""
"""
class Student:
    height = 160
    def __init__(self):
        print(self.height)
        self.height +=10
nick = Student()
kate = Student()
"""
"""
class Student:
    def __init__(self):
        self.height = 170
    height = 160
    def printer (self):
        print(self.height)
nick = Student()
nick.printer()
"""
"""
class Student:
    def __init__(self, name = None, height = 160):
        self.name = name
        self.height = height
    def __bool__(self):
        return self.name != None
    def __len__(self):
        return self.height
    def __del__(self):
        print("Training is over. I am now an expert!")

nick = Student("Nick", height=170)
print(nick.__len__())
print(nick.__bool__())
print(len(nick))
print(bool(nick))
"""
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Ім'я: {self.name}, Вік: {self.age}"

student1 = Student("Ivan",20)
print(student1.get_info())
"""
"""
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return 3.14159 * self.radius**2

circle1 = Circle(5)
print(circle1.calculate_area())
"""
"""
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_age(self):
        current_year = datetime.now().year
        age = current_year - self.year
        return age
book1 = Book("Book #1", "Author #1", 2020)
print(book1.get_age())
"""

import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive()

nick = Student(name="Nick")
for day in range(365):
    if nick.alive == False:
        break
nick.live(day)