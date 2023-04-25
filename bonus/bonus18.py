import PySimpleGUI as sg
from modules.zip_extractor import *

sg.theme('DarkPurple4')

label1 = sg.Text("Select archive:")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select dest dir:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key='folder')

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color='deepskyBlue')

col1 = sg.Column([[label1], [label2]])
col2 = sg.Column([[input1], [input2]])
col3 = sg.Column([[choose_button1],[choose_button2]])

window = sg.Window("Archive Extractor",
                   layout=[[col1, col2, col3],
                           [extract_button, output_label]])

while True:
    event, values = window.read()
    archpath = values['archive']
    dest_dir = values['folder']
    extract_archive(archpath, dest_dir)
    window['output'].update(value="Extraction complete!")

window.close()