import csv

with open("../files/weather.csv", "r") as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")

# data[1:] removes first row and looks at all subsequent rows.
for row in data[1:]:
    if row[0] == city:
        print(row[1])
