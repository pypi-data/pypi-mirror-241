from figures.point import Point

class Line():
    def __init__(self, point1:Point, point2:Point):
        self.point1 = point1
        self.point2 = point2
    def length(self):
        return ((self.point2.x - self.point1.x)**2 + (self.point2.y - self.point1.y)**2)**0.5