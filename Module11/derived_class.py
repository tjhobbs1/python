"""
Program:  derived_class.py
Author:  Ty Hobbs
Last Day Modified:  11/05/2019

The purpose of the program is to demonstrate the use of derived classes in Python. """

class Person:
    """
    This is a class for making an Person object.  It is the parent to Student

    Attributes:
        last_name (String): The last name of the Person
        first_name (String):  The first name of the Person
        address (String):  The address of the Person

    """
    def __init__(self, lname, fname, addy=''):
        """The Constructor
        Params:
        last_name (String): The last name of the Person
        first_name (String):  The first name of the Person
        address (String):  The address of the Person

        """
        self._last_name = lname
        self._first_name = fname
        self._address = addy

    def __repr__(self):
        return f'{self._last_name} {self._first_name} {self._address}'

    def __str__(self):
        return f'{self._first_name} {self._last_name}\n' \
               f'{self._address}'

    def display(self):
        #Returns a String object of the Person Class.
        return self._last_name + ", " + self._first_name + ":" + self._address

class Student(Person):
    """
    This is class for making a Student object.  It inherits from the Person class.
    Attributes:
        student_id (int):  The student Id of the student
        lname (String):  The last name of the student
        fname (String):  The first name of the student.
        major (String):  The major of the student
        gpa (Float):  The GPA of the student.
    """
    def __init__(self,student_id,lname,fname, major='Computer Science',gpa='0.0'):
        """The Consturctor for the Student Class
        Params:
         student_id (int):  The student Id of the student
        lname (String):  The last name of the student
        fname (String):  The first name of the student.
        major (String):  The major of the student
        gpa (Float):  The GPA of the student.
        """
        super().__init__(lname,fname) # Call init on parent class
        self._student_id = student_id
        self._major = major
        self._gpa = gpa

    def __repr__(self):
        return f'{self._student_id} {self._major} {self._gpa}'

    def __str__(self):
        return f'{self._student_id}\n' \
               f'{self._major}\n' \
               f'{self._gpa}'


    def display(self):
        """Returns a display of the Student object"""
        return f'{self._last_name},{self._first_name}:({self._student_id}) {self._major} gpa:{self._gpa}'

# Driver
my_student = Student(900111111, 'Song', 'River')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
print(my_student.display())

del my_student

