from random import randint as ri
from gui_point import GuiPoint
from gui_rectangle import GuiRectangle
from point import Point

import turtle

rectangle = GuiRectangle(Point(ri(0, 400), ri(0, 400)),
                         Point(ri(10, 400), ri(10, 400)))

print(f"Rectangle Coordinate: ({rectangle.point1.x}, {rectangle.point1.y}) and ({rectangle.point2.x},"
      f" {rectangle.point2.y})")

user_point = GuiPoint(float(input("Guess X:")),
                      float(input("Guess Y:")))

# Create rectangle object
myturtle = turtle.Turtle()
rectangle.draw(canvas=myturtle)
user_point.draw(canvas=myturtle, size = 10, color = 'green')
turtle.done()
