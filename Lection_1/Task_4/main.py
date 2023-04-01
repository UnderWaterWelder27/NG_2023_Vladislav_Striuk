from math import *

# a*x^2 + b*x + c = 0
# a - senior coefficient
# b - coefficient at x
# c - free member

senior_coefficient = float(input("Enter variable (a) >> "))
coefficient_at_x = float(input("Enter variable (b) >> "))
free_member = float(input("Enter variable (c) >> "))
discriminator = pow(coefficient_at_x, 2) - 4 * senior_coefficient * free_member

print(f"Discriminator = {discriminator}")

if senior_coefficient == 0:
    print(f"Variable \'a\' must not be zero ! But... \n " f"x = {-free_member / coefficient_at_x}")
elif discriminator < 0:
    print("There is no solution ((")
elif discriminator == 0:
    print(f"There is one root \n x = {-coefficient_at_x / (2 * senior_coefficient)}")
else:
    print(f"There is two roots \n "
          f"x1 = {(-coefficient_at_x + sqrt(discriminator)) / (2 * senior_coefficient)} \n "
          f"x2 = {(-coefficient_at_x - sqrt(discriminator)) / (2 * senior_coefficient)}")
