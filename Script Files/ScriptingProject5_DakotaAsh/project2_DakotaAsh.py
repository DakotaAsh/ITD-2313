a = int(input("Enter the first side of the triangle: "))
b = int(input("Enter the second side of the triangle: "))
c = int(input("Enter the third side of the triangle: "))
if ((a*a + b*b == c*c) or
    (b*b + c*c == a*a)):
    print("This is a right triangle.")
else:
    print("This is not a right triangle.")
