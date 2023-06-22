
class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width
    def set_height(self, height):
        self.height = height
    def set_width(self, width):
        self.width = width
    def get_area(self):
        return round(self.width * self.height, 2)
    def get_perimeter(self):
        return round(2 * (self.width + self.height), 2)
    def get_diagonal(self):
        return round((self.width ** 2 + self.height ** 2) ** .5, 2)
    def get_picture(self):
        self.picture = "\n"
        if self.width <= 50 and self.height <= 50:
            for i in range(self.height):
                self.picture += "* " * self.width + "\n"
            return self.picture
        else:
            return "Too big for a picture"
    def get_amount_inside(self, another_shape):
        self.another_shape_area = another_shape.get_area()
        self.current_shape_area = self.get_area()
        return round(self.current_shape_area / self.another_shape_area, 2)
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side_length):
        self.side = side_length
        super().__init__(self.side, self.side)
    def set_side(self, side_length):
        self.side = side_length
        self.height = side_length
        self.width = side_length
    def __str__(self):
        return f"Square(side={self.side})"

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

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))