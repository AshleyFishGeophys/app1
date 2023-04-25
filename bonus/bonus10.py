def get_average():
    with open("../files/data.txt") as file:
        data = file.readlines()
    values = data[1:]
    values = [float(i) for i in values]

    return sum(values) / len(values)


average = get_average()
print(f"Average is: {average}")