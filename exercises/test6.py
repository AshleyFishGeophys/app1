# Part 1 - read contents of file
file = open('../files/essay.txt', 'r')
print(file.read())
file.close()

# Part 2 - give number of characters in file
file2 = open('../files/essay.txt')
print(len(file2.read()))
file2.close()


# Part 3 - Prompt user to add a member to members.txt. When done, exit while loop
while True:
    user_action = input("Type add or exit: ")

    match user_action.strip():
        case 'add':
            add_member = input("Add a new member: ") + '\n'
            file3 = open('../files/members.txt', 'r')
            members = file3.readlines()
            file3.close()
            members.append(add_member)
            file3 = open('../files/members.txt', 'w')
            file3.writelines(members)
            file3.close()
        case 'exit':
            break
print('members.txt was successfully updated!')



# Part 4 - generate txt files and save contets to files
file_list = ['test6_pt1.txt', 'test6_pt2.txt', 'test6_pt3.txt']
contents = ['Hello', 'Hola', 'Bonjour']

for file_name, item in zip(file_list, contents):
    file_open = open(f"../files/{file_name}", 'w')
    file_open.write(item)

# Part 5 - open files and print contents
file_names = ['a.txt', 'b.txt', 'c.txt']
for idx, name in enumerate(file_names):
    file_name = open(f"../files/{name}", 'r')
    print(file_name.read())
