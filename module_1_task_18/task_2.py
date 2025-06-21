class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


get_rectangle = Rectangle(10, 10)
print(f"{get_rectangle.width}, {get_rectangle.height}")