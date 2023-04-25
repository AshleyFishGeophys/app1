try:
    width = float(input("Enter rectangle width: "))
    height = float(input("Enter rectangle height: "))

    if width == height:
        exit("That looks like a square.")

    area = width * height
    print(f"Area is: {area}")

except ValueError:
    print("Please enter a number")

