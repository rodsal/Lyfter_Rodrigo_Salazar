import FreeSimpleGUI as sg
from add_new_expense import MovementWindow
from add_category_window import category_window
from month_summary import Month_Summary

def main():
    layout = [
        [sg.Text("Welcome to Lyfter Finance Manager - RS")],
        [sg.Button("Add Expense"), sg.Button("Add Income"), sg.Button("Add Category"), sg.Button("Month Summary")],
        [sg.Exit()]
    ]
    window = sg.Window("Lyfter Finance Manager", layout)

    while True:
        event, _ = window.read()
        if event in (sg.WIN_CLOSED, "Exit"):
            break
        elif event == "Add Expense":
            MovementWindow("Expense").run()
        elif event == "Add Income":
            MovementWindow("Income").run()
        elif event == "Add Category":
            category_window()
        elif event == "Month Summary":
            summary = Month_Summary() 
            summary.show_summary()


    window.close()

if __name__ == "__main__":
    main()
