class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def __gt__(self,other):
        return self.area()>other.area()
rect1=Rectangle(10,5)
rect2=Rectangle(8,7)
print(f"Rectangle 1:Area={rect1.area()},Perimeter={rect1.perimeter()}")
print(f"Rectangle 2:Area={rect2.area()},Perimeter={rect2.perimeter()}")
if rect1>rect2:
    print("Rectangle 1 has a larger area.")
elif rect2>rect1:
    print("Rectangle 2 has a larger area.")
else:
    print("Both rectangles have equal area.")

