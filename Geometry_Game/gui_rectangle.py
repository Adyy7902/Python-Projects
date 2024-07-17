from rectangle import Rectangle


class GuiRectangle(Rectangle):
    """
    Creates a rectangle using the randomly generated points on the turtle canvas at the given coordinates
    """
    def draw(self, canvas):
        """Draws the randomly generated rectangle on the turtle canvas at given coordinates"""
        canvas.penup()
        # Goto certain coordinates
        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()
        canvas.forward(self.point2.x-self.point1.x)  # Move 100 pixels forward
        canvas.left(90)  # Turn 90 degrees
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
