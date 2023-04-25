# List comprehension tests

# Capitalize first and last name in list
names = ['john smith', 'jay santi', 'eva kuki']
print([name.title() for name in names])

# print the num of characters in each item in usernames
usernames = ["john 1990", "alberta1970", "magnola2000"]
print([len(entry) for entry in usernames])

# Convert each item into a float in user_entries
user_entries = ['10', '19.1', '20']
print([float(num) for num in user_entries])

# Print the sum of numbers from user_entries
nums = [float(i) for i in user_entries]
print(sum(nums))

