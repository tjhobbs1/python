class Person:
    """Person class"""
    def __init__(self, lname, fname, ssn=''):         # Constructor sets all to no value
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        ssn_characters = set("1234567890-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        if ssn and not ssn_characters.issuperset(ssn):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.ssn = ssn           # Social Security Number

    def change_last_name(self, name):
        self.last_name = name

    def change_first_name(self, name):
        self.first_name = name

    def display(self):
        return self.last_name + ", " + self.first_name + ":" + self.ssn


# # Driver
# # Valid person
# person1 = Person('Duck', 'Donald') # ssn not required
# print(person1.display())
# # Valid person and ssn
# person2 = Person('Duck', 'Donald', '111-11-1111')
# print(person2.display())
# # Invalid person
# try:
#     person3 = Person('123', 'Donald', '111-11-1111')
# except ValueError:
#     print("Error found, person not created")
