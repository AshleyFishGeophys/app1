try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    percent = (value/total_value) * 100
    print(f"That is {percent}%")

except ZeroDivisionError:
    exit("Your total value cannot be zero. Run the program again.")

except ValueError:
    exit("You need to enter a number. Run the program again.")


