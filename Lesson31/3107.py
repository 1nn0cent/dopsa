class Shape:
    def area(self):
        pass  

    def perimeter(self):
        pass  


class Polygon(Shape):
    def number_of_sides(self):
        pass  


class Triangle(Polygon):
    def calculate_height(self):
        pass  


class IsoscelesTriangle(Triangle):
    def is_equal_sides(self):
        pass  


class EquilateralTriangle(IsoscelesTriangle):
    def all_sides_equal(self):
        pass  


class Quadrilateral(Polygon):
    def diagonals(self):
        pass  


class Parallelogram(Quadrilateral):
    def opposite_sides_equal(self):
        pass  


class Rectangle(Parallelogram):
    def right_angles(self):
        pass  


class Square(Rectangle):
    def all_sides_equal(self):
        pass  
