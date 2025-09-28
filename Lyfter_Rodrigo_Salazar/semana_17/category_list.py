import json
from datetime import datetime

class Categories:
    def __init__(self, file_path="Category_List.json"):
        self.file_path = file_path
        self.categories = self.load_categories()

    def load_categories(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                return data.get("categories", [])
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_categories(self):
        data = {
            "categories": self.categories,
            "lastUpdated": datetime.now().strftime("%Y-%m-%d")
        }
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def add_category(self, new_category):
        if new_category and new_category not in self.categories:
            self.categories.append(new_category)
            self.save_categories()
            return True
        return False
