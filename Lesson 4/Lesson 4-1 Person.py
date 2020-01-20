from datetime import date


class Person:

    def __init__(self, name, date_brth):
        self.name = name
        self.date_brth = date_brth

    def age(self):
        today = date.today()
        age = today.year - self.date_brth.year
        if today.month < self.date_brth.month:
            age -= 1
        elif today.month == self.date_brth.month and today.day < self.date_brth.day:
            age -= 1
        return age

    def get_info(self):
        print(f'Name: {self.name}, Birthday: {self.date_brth}')


class Abiturient(Person):

        def __init__(self, name, date_brth, faculty):
            super().__init__(name, date_brth)
            self.name = name
            self.date_brth = date_brth
            self.faculty = faculty

        def get_info(self):
            print(f'Name: {self.name}, Birthday: {self.date_brth}, Faculty: {self.faculty}')


class Student(Person):

    def __init__(self, name, date_brth, faculty, course):
        super().__init__(name, date_brth)
        self.name = name
        self.date_brth = date_brth
        self.faculty = faculty
        self.course = course

    def get_info(self):
        print(f'Name: {self.name}, Birthday: {self.date_brth}, Faculty: {self.faculty}, Course: {self.course}')


class Teacher:

    def __init__(self, name, date_brth, faculty, post, experience):
        self.name = name
        self.date_brth = date_brth
        self.faculty = faculty
        self.post = post
        self.experience = experience

    def get_info(self):
        print(f'Name: {self.name}, Birthday: {self.date_brth}, Faculty: {self.faculty}, '
              f'Post: {self.post}, Experience: {self.experience}')

    def age(self):
        today = date.today()
        age = today.year - self.date_brth.year
        if today.month < self.date_brth.month:
            age -= 1
        elif today.month == self.date_brth.month and today.day < self.date_brth.day:
            age -= 1
        return age


vasyl = Person('Vasya Petrov', date(2012, 4, 5))
grisha = Abiturient('Grisha Lastochkin', date(1999, 3 ,15), 'FTIT')
ivan = Teacher('Ivan Prokofiev', date(1975, 12, 17), 'FTIT', 'rector', 10)
petya = Student('Petia Igorev', date(2003, 4, 19), 'FTIT', 4)

person_list = [vasyl, grisha, petya, ivan]
for i in range(len(person_list)):
    person_list[i].get_info()

for i in range(len(person_list)):
    age = person_list[i].age()
    if 50 > age > 15:
        print(age, person_list[i].name)
        print()

