# This is an example of programming to an interface, which is defined in the Shape class. 

class Shape:
    """This class is the interface class"""
    def get_area(self):
        raise NotImplementedError("Subclasses must implement area() method.")

    def get_perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter() method.")


# Define a class that implements the Shape interface
class Rectangle(Shape):  # Notice the Shape class is an argument.
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)


# Define another class that implements the Shape interface
class Circle(Shape):  # notice the shape class is an argument.
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius

    def get_perimeter(self):
        return 2 * 3.14 * self.radius


# Here we define another class that does not conform to the interface requirement
# This class does not have a get_perimeter method. 
class Triangle(Shape):
    
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return self.base * self.height


# Create instances of the classes and demonstrate the usage
rectangle = Rectangle(5, 3)
print("Rectangle:")
print("Area:", rectangle.get_area())
print("Perimeter:", rectangle.get_perimeter())

circle = Circle(2)
print("\nCircle:")
print("Area:", circle.get_area())
print("Perimeter:", circle.get_perimeter())

# Instance that has not conformed to the interface.
triangle = Triangle(5,8)
print("\nTriangle")
print(f'Area is {triangle.get_area()}')

# This line will cause ann error - mo method in the Triangle class for perimeter
# print(f'Perimeter is {triangle.get_perimeter()}')
