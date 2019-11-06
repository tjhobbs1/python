class Shape:
    """Shape class"""
    colors = ['BLUE', 'GREEN', 'ORANGE', 'PURPLE', 'RED', 'YELLOW']

    def __init__(self, color='BLUE'):
        self._color = color

    def change_color(self, new_color):
        if new_color not in self.colors:
            raise InvalidColorError
        self._color = new_color

    def display_color(self):
        return str(self._color)



class InvalidColorError(Exception):
    """InvalidColorError is derived class of Excpetion base class"""
    pass

class Rectangle(Shape):   # Base class is Shape
    """Rectangle derived class of Shape base class"""
    def __init__(self, color='RED', l=0, w=0):  # default values
        super().__init__(color)  # calls the base constructor
        self._length = l
        self._width = w

    def area(self):
        return self._length * self._width

    def display_color(self):
        return str('Rectangle color ' + self._color)

# Driver
r = Rectangle('BLUE', 3, 4.5)
try:
    r.change_color('PURPLE')
except InvalidColorError:
    print('Invalid color, color not changed!')
print(r.display_color())
