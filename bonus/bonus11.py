from modules.parsers import *
from modules.converters import *

feet_inches = input("Enter feet in inches: ")

parsed = parse(feet_inches)
feet = parsed["feet"]
inches = parsed["inches"]

print(f"Feet: {feet}, inches: {inches}")

result = convert_to_meters(feet, inches)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use slide.")