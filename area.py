area_square=lambda side:side**2
area_rectangle=lambda length,width:length*width
area_triangle=lambda base,height:0.5*base*height
side=float(input("Enter side of square:"))
length=float(input("Enter length of rectangle:"))
width=float(input("Enter width of rectangle:"))
base=float(input("Enter base of triangle:"))
height=float(input("Enter height of triangle:"))
print(f"Area of Square:{area_square(side)}")
print(f"Area of Rectangle:{area_rectangle(length,width)}")
print(f"Area of Triangle:{area_triangle(base,height)}")

