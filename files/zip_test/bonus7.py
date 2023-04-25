date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10? ")
thoughts = input("Let your thoughts flow: \n")

with open(f"../daily_journal/{date}.txt", 'w') as file:
    file.write(f"mood from 1-10: {mood}\n\n")
    file.write(thoughts)
