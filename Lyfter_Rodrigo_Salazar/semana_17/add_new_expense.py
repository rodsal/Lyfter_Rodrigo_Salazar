import FreeSimpleGUI as sg
from category_list import Categories
from data_persistency import Movements

class MovementWindow:
    def __init__(self, type):
        self.type = type
        self.categories = Categories()
        self.movements = Movements()

    def run(self):
        layout = [
            [sg.Text(f"Enter {self.type} title:"), sg.Input(key="-TITLE-", size=(20, 1))],
            [sg.Text(f"Enter {self.type} amount:"), sg.Input(key="-AMOUNT-", size=(10, 1))],
            [sg.Text("Select Category:"), sg.Combo(self.categories.categories, key="-CATEGORY-", default_value="---")],
            [sg.Button("Submit"), sg.Button("Show Table"), sg.Exit()]
        ]
        window = sg.Window(f"{self.type} Window", layout)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "Exit"):
                break
            elif event == "Submit":
                title = values["-TITLE-"].strip()
                amount = values["-AMOUNT-"].strip()
                category = values["-CATEGORY-"]
                if not title or not amount or category == "---":
                    sg.popup_error("Please fill all fields correctly.")
                    continue
                try:
                    amount = float(amount)
                except ValueError:
                    sg.popup_error("Amount must be a number.")
                    continue
                self.movements.add_movement(title, amount, category, self.type)
                sg.popup(f"{self.type} added successfully.")
                window["-TITLE-"].update("")
                window["-AMOUNT-"].update("")
                window["-CATEGORY-"].update("---")
            elif event == "Show Table":
                movements = self.movements.movements
                if not movements:
                    sg.popup("No movements recorded.")
                else:
                    headings = ["Title", "Amount", "Category", "Type", "Date"]
                    data = [[m["title"], m["amount"], m["category"], m["type"], m["date"]] for m in movements]
                    table_layout = [
                        [sg.Table(values=data, headings=headings, auto_size_columns=True, justification="center", num_rows=min(20, len(data)))],
                        [sg.Button("Close")]
                    ]
                    table_window = sg.Window("Movements Table", table_layout)
                    while True:
                        table_event, _ = table_window.read()
                        if table_event in (sg.WIN_CLOSED, "Close"):
                            break
                    table_window.close()

        window.close()
