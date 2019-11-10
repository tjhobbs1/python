from pip._vendor.pyparsing import basestring


class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major

        if isinstance(gpa, basestring):
            raise ValueError
        self.gpa = gpa

    def __str__(self):
        return f'Name: {self.last_name},{self.first_name} Major: {self.major} GPA: {self.gpa}'

# student1 = Student('hobbs','ty','BIS',3.23)
#
# print(str(student1))












