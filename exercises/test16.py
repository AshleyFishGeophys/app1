import PySimpleGUI as sg
from modules.converters import *

label_feet = sg.Text("Enter feet:")
input_feet = sg.Input(key='feet')

label_inches = sg.Text("Enter inches:")
input_inches = sg.Input(key='inches')

button_convert = sg.Button("Convert")
output_text = sg.Text(key="output")

exit_button = sg.Button('Exit')

window = sg.Window("Convertor",
                   layout=[[label_feet, input_feet],
                           [label_inches, input_inches],
                           [button_convert, exit_button, output_text]])

while True:
    event, values = window.read()
    match event:
        case "Convert":
            try:
                meters = convert_to_meters(int(values['feet']), float(values['inches']))
                window['output'].update(value=f"{meters} m", text_color="white")
            except ValueError:
                sg.popup("Please enter in feet and/or inches", font=('Helvetica', 10))

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

window.close()
