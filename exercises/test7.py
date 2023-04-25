# Have user flip a coin by saying heads or tails, then print the current percentage of heads flipped

while True:
    with open('../files/sides.txt', 'r') as file:
        sides = file.readlines()

    heads_or_tails = input("Throw the coin and enter heads or tails here: ?") + '\n'

    sides.append(heads_or_tails)

    with open('../files/sides.txt', 'w') as file:
        file.writelines(sides)

    num_heads = sides.count('heads\n')
    percent_heads = num_heads / len(sides) * 100

    print(f"Heads: {percent_heads}%")


