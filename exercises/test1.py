
# 1. Prompts the user to input the country they are from.
user_input = input("What is your country of origin? ")

# Strings are case-sensitive in Python
match user_input.lower():
    # 2. If the user enters the word USA, the program prints out Hello.
    case 'usa':
        print("Hello")
    # 3. If the user enters the word  India, the program prints out Namaste.
    case 'india':
        print("Namaste")
    # 4. If the user enters the word Germany, the program prints out Hallo.
    case 'germany':
        print("Hallo")
