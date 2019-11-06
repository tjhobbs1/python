class Person:
    """Person class"""
    def __init__(self, lname, fname, addy=''):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.address = addy

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Student:
    """Student Class"""
    def __int__(self,major,start_date,gpa):
        self.major = major
        self.start_date = start_date
        self.gpa = gpa

    def change_major(self,major):
        self.major = major

    def update_gpa(self, gpa):
        self.gpa = gpa




# Drivers
student1 = Person('Hobbs','Ty')
student1.major = 'CIS'
student1.start_date = "June"
student1.gpa = 3.14
student1.change_major('Culinary')


