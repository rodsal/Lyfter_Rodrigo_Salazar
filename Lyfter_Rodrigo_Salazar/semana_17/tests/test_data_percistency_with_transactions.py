import unittest
import sys
from datetime import datetime
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_persistency import Movements

movements = Movements()

def test_add_movement_in_format_json ():
    #Arrange
    title = "Gasto inesperado"
    amount = 13000
    category = "Entretenimiento"
    type = "Expense"
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #Act
    move = movements.add_movement(title,amount,category,type)
    #Assert
    assert move == {
                    "title": "Gasto inesperado",
                    "amount": 13000,
                    "category": "Entretenimiento",
                    "type": "Expense",
                    "date": date
                }