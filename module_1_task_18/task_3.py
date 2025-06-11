from task_2 import Rectangle

class RectangleArea(Rectangle):
    def area(self):
        return self.width * self.height


result = RectangleArea(5,10)

print(f"Area: {result.area()}")