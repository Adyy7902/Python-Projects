from point import Point


class GuiPoint(Point):
    """
    Creates a point on the turtle canvas, to show what coordinates user chose, and shows if it lies inside the randomly
    generated rectangle or not
    """
    def draw(self, canvas, size = 5, color = 'red'):
        """Draws the user selected coordinate as a point on the canvas"""
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)
