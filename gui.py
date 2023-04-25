import time
import PySimpleGUI as sg
from modules.functions import *
import os
path = 'files/todos.txt'

if not os.path.exists(path):
    with open(path, 'w') as file:
        pass

sg.theme('DarkPurple4')

label = sg.Text("Enter a TODO:")
clock_label = sg.Text('', key='clock')

input_box = sg.InputText(tooltip="Type in a TODO item", key="todo")
list_box = sg.Listbox(values=get_todos(path), key="todos",
                      enable_events=True, size=[45, 10])

add_button = sg.Button('Add')
# add_button = sg.Button(size=50, image_source='add.png', mouseover_colors='LightBlue2',
#                        tooltip='Add Todo', key='Add')
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
# complete_button = sg.Button(size=50, image_source='complete.png', mouseover_colors='LightBlue2',
#                        tooltip='Complete Todo', key='Complete')
exit_button = sg.Button('Exit')

# layout = [[]] ... each [] inside of the main layout [] is a new row
# Each row in the gui has to be its own list. Must be PySimpleGUI types
window = sg.Window("My TODO App",
                   layout=[[clock_label],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = get_todos(path)
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            write_todos(todos, path)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = get_todos(path)
                idx = todos.index(todo_to_edit)
                todos[idx] = new_todo
                write_todos(todos, path)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item to first!", font=("Helvetica", 20))

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = get_todos(path)
                todos.remove(todo_to_complete)
                write_todos(todos, path)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item to first!", font=("Helvetica", 20))

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case 'Exit':
            break

        case sg.WIN_CLOSED:
            break

window.close()
