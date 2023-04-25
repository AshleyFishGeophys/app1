filenames = ['document', 'report', 'presentation']

for idx, item in enumerate(filenames):
    print(f"{idx}-{item.capitalize()}.txt")


ips = ['100.122.133.105', '100.122.133.111']

index = int(input("Input an index of the IP you want: "))
print(f"You chose {ips[index]}")