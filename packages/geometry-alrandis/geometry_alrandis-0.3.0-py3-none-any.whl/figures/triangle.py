from figures.point import Point
from figures.line import Line

class Triangle:
    def __init__(self, point1:Point, point2:Point, point3:Point):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def a(self):
        return Line(self.point1, self.point2)
    def b(self):
        return Line(self.point2, self.point3)
    def c(self):
        return Line(self.point1, self.point3)
    
    def perimeter(self):
        a = self.a().length()
        b = self.b().length()
        c = self.c().length()
        return round(a + b + c, 4)
    
    def square(self):
        p = self.perimeter()/2
        a = self.a().length()
        b = self.b().length()
        c = self.c().length()
        return round((p * (p - a) * (p -b) * (p - c)) ** 0.5, 4)