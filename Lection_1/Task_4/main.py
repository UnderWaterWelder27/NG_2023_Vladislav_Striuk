from math import *

# a*x^2 + b*x + c = 0

a = float(input("Enter variable (a) >> "))
b = float(input("Enter variable (b) >> "))
c = float(input("Enter variable (c) >> "))
discriminator = pow(b, 2) - 4 * a * c

print(f"Discriminator = {discriminator}")

if a == 0:
    print(f"Variable \'a\' must not be zero ! But... \n " f"x = {-c / b}")
elif discriminator < 0:
    print("There is no solution ((")
elif discriminator == 0:
    print(f"There is one root \n x = {-b / (2 * a)}")
else:
    print(f"There is two roots \n "
          f"x1 = {(-b + sqrt(discriminator)) / (2 * a)} \n "
          f"x2 = {(-b - sqrt(discriminator)) / (2 * a)}")
