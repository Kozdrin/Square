from rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)


square_1 = Square(5)
square_2 = Square(10)

circle_1 = Circle(9)


figures =  [rect_1, rect_2, square_1, square_2, circle_1]
for figure in figures:
      if isinstance(figure,Square):
            print(figure.get_area_square())
      if isinstance(figure,Rectangle):
            print(figure.get_area())
      if isinstance(figure, Circle):
            print(int(figure.get_circle_square()))