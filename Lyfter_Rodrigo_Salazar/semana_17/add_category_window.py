import FreeSimpleGUI as sg
from category_list import Categories

def category_window ():
    categories = Categories()
    layout = [
        [sg.Text("Enter a new Category:"), sg.Input(key="-NEWCATEGORY-", size=(20, 1))],
        [sg.Button("Add Category"), sg.Button("Show Categories"), sg.Exit()]
    ]
    window = sg.Window("Add Category", layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Exit"):
            break
        elif event == "Add Category":
            new_category = values["-NEWCATEGORY-"].strip()
            if categories.add_category(new_category):
                sg.popup("New category added successfully.")
            else:
                sg.popup_error("Invalid or duplicate category.")
        elif event == "Show Categories":
            sg.popup("Current Categories:", "\n".join(categories.categories))

    window.close()
