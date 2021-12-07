class Polygon:
    def __init__(self,sides):
        self.sides=sides

    def area(self,length):
        return length*length


class Square(Polygon):
    pass
class Triangle:
    def area(self):

sqr=Square(4)
print(sqr.sides)
