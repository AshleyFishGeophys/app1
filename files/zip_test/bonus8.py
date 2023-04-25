password = input("Enter new password: ")
result = {}

if len(password) >= 8:
    result['length'] = True
else:
    result['length'] = False

result['numOfDigits'] = False
for i in password:
    if i.isdigit():
        result['numOfDigits'] = True

result['hasUpperCase'] = False
for i in password:
    if i.isupper():
        result['hasUpperCase'] = True

if all(result.values()):
    print('Password is strong.')
else:
    print('Password is weak.')

