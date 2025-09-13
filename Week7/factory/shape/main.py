from shape_factory import ShapeFactory

def main():
  shape_factory = ShapeFactory()
  shape = shape_factory.get_shape("circle")
  shape.draw()
  shape = shape_factory.get_shape("square")
  shape.draw()
  shape = shape_factory.get_shape("triangle")
  shape.draw()


if __name__ == "__main__":
  main()