# App to have a user make, view, complete, and edit a to-do list.
import time
from modules.functions import *


while True:
    # Get user input, then do an action based off of the input. lower() allows for any form of the input
    user_action = input("Type add, show, edit, complete, or exit: ").lower()
    user_action = user_action.strip()

    if user_action.startswith('add'):
        # Allows users to store items in a txt file
        todo = user_action[4:] + '\n'

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        for idx, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{idx + 1}) {item}")

    elif user_action.startswith('edit'):
        try:
            num = int(user_action[5:])
            todos = get_todos()

            todos[num - 1] = input("Enter new todo item: ") + '\n'

            write_todos(todos)


        except IndexError:
            print("Your command is not valid. Need to enter in todo number to edit.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos()

            todo_removed = todos[number - 1].strip('\n')
            # .pop() removed the item in the list from the selected index
            todos.pop(number - 1)

            write_todos(todos)

            print(f"TODO completed: {todo_removed}")

        except ValueError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        print("BYE!")

        break

    else:
        print('Command is not valid!')

