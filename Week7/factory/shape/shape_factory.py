#Week 7 Activity 3:  Design Pattern - Factory
  # What problems might arise if a program directly creates objects within multiple places instead of using a Factory class?  
# Answer: In this case, if we want to add a new shape, we need to modify the ShapeFactory class and the main class.
# If we use a Factory class, we can add a new shape without modifying the ShapeFactory class and the main class.

from abc import ABC, abstractmethod

# Old way
# class Circle:
#   def draw(self):
#     print("Drawing Circle")

# class Square:
#   def draw(self):
#     print("Drawing Square")

# class ShapeFactory:
#   def get_shape(self, shape_type):
#     if shape_type == "circle":
#       return Circle()
#     elif shape_type == "square":
#       return Square()
#     else:
#       return None


# New way - Factory Pattern implementation
# 1. Abstract Product (Shape interface)\
# The abstract class that defines the interface for all shapes
class Shape(ABC):
  @abstractmethod
  def draw(self):
    pass

# 2. Concrete Products
# Implementations of the Shape interface
class Circle(Shape):
  def draw(self):
    print("Drawing Circle")

class Square(Shape):
  def draw(self):
    print("Drawing Square")

class Triangle(Shape):
  def draw(self):
    print("Drawing Triangle")

# 3. Factory Class
# The factory class that creates the shapes
class ShapeFactory:
  def get_shape(self, shape_type):
    if shape_type == "circle": 
      return Circle()
    elif shape_type == "square":
      return Square()
    elif shape_type == "triangle":
      return Triangle()
    else:
      return None