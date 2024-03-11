import math


class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def set_width(self, new_width):
    self.width = new_width

  def set_height(self, new_height):
    self.height = new_height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
    return ((self.width**2 + self.height**2)**0.5)

  def get_picture(self):
    if self.width > 50:
      return "Too big for picture."

    pic = ""
    for i in range(self.height):
      for j in range(self.width):
        pic += "*"
      pic += "\n"
    return pic

  def get_amount_inside(self, shape):
    area1 = self.get_area()
    area2 = shape.get_area()

    return math.floor(area1 / area2)

  pass


# subclass inehiting from Rectangle class
class Square(Rectangle):

  def __init__(self, side_length):
    super().__init__(side_length, side_length)

  def __str__(self):
    return f"Square(side={self.width})"

  def set_side(self, new_side):
    self.width = new_side
    self.height = new_side

  def set_width(self, width):
    self.set_side(width)

  def set_height(self, height):
    self.set_side(height)

  pass


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
