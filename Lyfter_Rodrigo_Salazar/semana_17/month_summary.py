import FreeSimpleGUI as sg
from data_persistency import Movements
from datetime import datetime

class Month_Summary():
    def __init__(self):
        self.movements = Movements().load_movements()

    def filter_month_movements (self, movements):
        today = datetime.today()
        month = today.month
        year = today.year
        month_movements = []

        for movement in movements:
            movement_date = datetime.strptime(movement["date"], "%Y-%m-%d %H:%M:%S")
            if movement_date.month == month and movement_date.year == year:
                month_movements.append(movement)
        
        return month_movements

    def show_summary (self):
        month_movements = self.filter_month_movements(self.movements)

        income_movements = self.get_movement_per_type(month_movements, "income")
        expense_movements = self.get_movement_per_type(month_movements, "expense")

        total_income = self.calculate_amount(income_movements)
        total_expense = self.calculate_amount(expense_movements)
        total_difference = total_income - total_expense

        
        layout = [
            [sg.Text("Resumen del mes actual", font=("Helvetica", 14))],
            [sg.Text(f"Total de ingresos: ${total_income:.2f}", text_color="green")],
            [sg.Text(f"Total de gastos:   ${total_expense:.2f}", text_color="red")],
            [sg.Text(f"Saldo disponible:  ${total_difference:.2f}", font=("Helvetica", 12, "bold"))],
            [sg.Button("Cerrar")]
        ]

        window = sg.Window("Resumen mensual", layout)
        while True:
            event, _ = window.read()
            if event in (sg.WIN_CLOSED, "Cerrar"):
                break
        window.close()


    def get_movement_per_type (self, movements, movement_type):
        type = []
        for movement in movements:
            if movement["type"].strip().lower() == movement_type:
                type.append(movement)
        return type
    
    def calculate_amount (self, movement_type):
        total = 0.0
        for movement in movement_type:
            total = total + float(movement["amount"])
        return total
    



