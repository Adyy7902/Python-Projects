class Point:

  def __init__(self,x,y):
    self.x = x
    self.y = y

  def falls_in_rectangle(self, rectangle):
    """
    Checks whether the user-given rectangle points lies inside the randomly generated rectangle points
    """
    if rectangle.point1.x < self.x < rectangle.point2.x and rectangle.point1.y < self.y < rectangle.point2.y:
      return True
    else:
      return False

  def distance_from_point(self, point):
    """
    Returns the distance of user-given rectangle points to that of randomly generated rectangle points
    """
    return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
