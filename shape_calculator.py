class Rectangle:

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    # initialising width and height variables
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # set and get methods
    def set_width(self, value):
        self.width = value

    def set_height(self, value):
        self.height = value

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        picture = ""

        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture += ("*" * self.width + "\n") * self.height

        return picture

    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()


# Square is subclass of Rectangle
class Square(Rectangle):

    def __str__(self):
        return f"Square(side={self.width})"

    def __init__(self, side):
        Rectangle.width = side
        Rectangle.height = side

    def set_side(self, value):
        Rectangle.set_width(self, value)
        Rectangle.set_height(self, value)
