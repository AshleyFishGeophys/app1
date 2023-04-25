def calculate_age(year_of_birth, current_year=2023):
    return current_year - year_of_birth

birth_year = int(input("What is your year of birth? "))

age = calculate_age(birth_year)

if age >= 120:
    print(f"You are super old! {age}yrs!")
else:
    print(f"You are {age}yrs old!")



def names_in_list(user_names):
    return [x.strip for x in user_names.split(',')]


def num_of_names_inputed(list_of_names):
    return len(list_of_names)


user_input_names = input("Enter names separated by commas: ")

list_names = names_in_list(user_input_names)

print(num_of_names_inputed(list_names))
