from src.square import Square
from src.triangle import Triangle
from src.rectangle import Rectangle
from src.circle import Circle

square = Square(10)
triangle = Triangle(13, 14, 15)
rectangle = Rectangle(5, 7)
circle = Circle(3)

print(square.area)          # 100
print(triangle.area)        # 84
print(triangle.add_area(square))  # 184
print(rectangle.perimeter)  # 24
print(circle.area)          # 28.27...
