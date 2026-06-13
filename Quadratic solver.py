# Quadratic Equation Solver
# Author: Okikiola Arowolo

import math

print("Quadratic Equation Solver")
print("Equation form: ax² + bx + c = 0")

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Two real solutions:")
    print("x1 =", x1)
    print("x2 =", x2)

elif discriminant == 0:
    x = -b / (2*a)
    print("One real solution:")
    print("x =", x)

else:
    print("No real solutions")
