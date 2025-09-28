import json
from datetime import datetime

class MovementManager:
    def __init__(self, file_path="movements.json"):
        self.file_path = file_path
        self.movements = self.load_movements()

    def load_movements(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_movements(self):
        with open(self.file_path, "w") as file:
            json.dump(self.movements, file, indent=4)

    def add_movement(self, title, amount, category, tipo):
        movement = {
            "title": title,
            "amount": amount,
            "category": category,
            "type": tipo,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.movements.append(movement)
        self.save_movements()
        return movement
