import PySimpleGUI as sg

"""
layout = [[sg.Text("What is your name?")],
          [sg.InputText()],
          [sg.Button("OK")]]
window = sg.Window("Title of the window").Layout(layout)
button, values = window.Read()
sg.Popup("Hello {} welcome to PySimpleGUI".format(values[0]))
"""

#sg.SetOptions(icon="C:\\Users\\schne\\Coding\\Python\\icons8-glücklich-filled-50.png")

layout = [
    [sg.Text("Datei zum Auslesen")],
    [sg.InputText(), sg.FileBrowse()],
    [sg.Submit("Ok"), sg.Cancel("Abbrechen")]
]
(button, (source_filename,)) = sg.Window("Datei-Test").Layout(layout).Read()

print(button, source_filename)