user_input_liters = float(input("Enter in liters: "))

def convert_liters_to_cubic_meters(liters_arg):
    return liters_arg/1000


cubic_meters = convert_liters_to_cubic_meters(user_input_liters)

print(f"Cubic meters: {cubic_meters}")


password = input("Enter password: ")

def password_strength(password_input):

    result = {"length": False, "hasCapitalLetter": False, "hasNumber": False}

    if len(password_input) >= 8:
        result['length'] = True

    for i in password_input:
        if i.isupper():
            result["hasCapitalLetter"] = True
        if i.isdigit():
            result["hasNumber"] = True

    if all(result.values()):
        return "Strong Password"
    else:
        return "Weak Password"


print(password_strength(password))

