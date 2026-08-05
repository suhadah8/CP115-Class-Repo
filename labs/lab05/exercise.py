# Import entire modules
import math
import random
import datetime

# Using imported modules
circle_area = math.pi * (5 ** 2)
random_number = random.randint(1, 100)
current_date = datetime.date.today()

# Import specific functions from modules
from math import sqrt, pow, sin, cos
from random import choice, shuffle
from datetime import datetime, timedelta

# Using imported functions directly (no module prefix needed)
square_root = sqrt(25)
power_result = pow(2, 8)
random_choice = choice(['apple', 'banana', 'cherry'])



print("Hello", "Python", "World")
#end=" " replaced the usual new line with a space.
print("Hello", "Python", "World", sep="-")

print("Hello", end=" ")
print("World")

name = "suha"
age = 18
print(f"My name is {name} and I am {age} years old.")
print(current_date)
print(square_root)

first = int(input("First number: "))
second = int(input("Second number: "))
print(first + second)