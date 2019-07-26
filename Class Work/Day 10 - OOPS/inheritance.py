class Shape:

    def print(self):
        print("Shape wala print hai")
    
class Rect(Shape):
    
    def print(self):
        print("REct wala")


s = Shape()
s.print()

r = Rect()
r.print()