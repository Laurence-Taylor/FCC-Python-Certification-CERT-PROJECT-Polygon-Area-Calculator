import math

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        answer=''
        if self.__class__.__name__ == 'Rectangle':
            list =[f'{key}={val}' for key, val in vars(self).items()]
            answer = f'{self.__class__.__name__}({list[0]}, {list[1]})'  
        else:
            list = [val for val in vars(self).values()]
            answer = f'{self.__class__.__name__}(side={list[0]})'
        return answer
    
    def set_width(self, width):
        if self.__class__.__name__ == 'Rectangle':
            self.width = width
        else:
            self.width = width
            self.height = width

    def set_height(self, height):
        if self.__class__.__name__ == 'Rectangle':
            self.height = height
        else:
            self.width = height
            self.height = height

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return 2*self.width + 2*self.height

    def get_diagonal(self):
        return (self.width**2+self.height**2)**.5

    def get_picture(self):
        w, h = vars(self).values()
        if w > 50 or h > 50:
            return 'Too big for picture.'
        else:
            picture=''
            for i in range(h):
                for j in range(w):
                    picture += '*'
                picture += '\n'
            return picture
    
    def get_amount_inside(self, other):
        # width and height of the rectangle
        w_r, h_r = vars(self).values()
        # width and height of the other shapre
        w_o, h_o = vars(other).values()
        return (w_r//w_o)*(h_r//h_o)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

sq.set_side(5)
rect = Rectangle(4, 8)
rect2 = Rectangle(3, 6)
print(rect.get_amount_inside(rect2))
