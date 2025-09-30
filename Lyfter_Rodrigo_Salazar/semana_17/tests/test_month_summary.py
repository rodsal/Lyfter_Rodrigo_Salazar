import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from month_summary import Month_Summary
summary = Month_Summary()

movements = [
    {
        "title": "Diario Mitad Agosto",
        "amount": 64900.0,
        "category": "Supermercado",
        "type": "Expense",
        "date": "2025-08-28 16:40:09"
    },
    {
        "title": "Comida Domingo",
        "amount": 15439.0,
        "category": "Comida Afuera",
        "type": "Expense",
        "date": "2025-09-28 16:41:32"
    },
    {
        "title": "Comida Sabado",
        "amount": 5340.0,
        "category": "Comida Afuera",
        "type": "Expense",
        "date": "2025-09-28 16:42:06"
    },
    {
        "title": "Comida Viernes",
        "amount": 32567.0,
        "category": "Comida Afuera",
        "type": "Expense",
        "date": "2025-09-28 16:48:04"
    },
    {
        "title": "Salario",
        "amount": 737464738.0,
        "category": "Salario",
        "type": "Income",
        "date": "2025-09-28 16:49:59"
    }]

def test_filter_month_movements ():
    #Arrange
    
    #Act
    month_movement = summary.filter_month_movements(movements)
    #Assert
    assert month_movement == [
                                {
                                    "title": "Comida Domingo",
                                    "amount": 15439.0,
                                    "category": "Comida Afuera",
                                    "type": "Expense",
                                    "date": "2025-09-28 16:41:32"
                                },
                                {
                                    "title": "Comida Sabado",
                                    "amount": 5340.0,
                                    "category": "Comida Afuera",
                                    "type": "Expense",
                                    "date": "2025-09-28 16:42:06"
                                },
                                {
                                    "title": "Comida Viernes",
                                    "amount": 32567.0,
                                    "category": "Comida Afuera",
                                    "type": "Expense",
                                    "date": "2025-09-28 16:48:04"
                                },
                                {
                                    "title": "Salario",
                                    "amount": 737464738.0,
                                    "category": "Salario",
                                    "type": "Income",
                                    "date": "2025-09-28 16:49:59"
                                }]
    
def test_get_expense_movements_type ():
    #Arrange
    
    #Act
    expense_movements = summary.get_movement_per_type(movements,"expense")
    #Assert
    assert expense_movements == [
                                {
                                    "title": "Diario Mitad Agosto",
                                    "amount": 64900.0,
                                    "category": "Supermercado",
                                    "type": "Expense",
                                    "date": "2025-08-28 16:40:09"
                                },
                                {
                                    "title": "Comida Domingo",
                                    "amount": 15439.0,
                                    "category": "Comida Afuera",
                                    "type": "Expense",
                                    "date": "2025-09-28 16:41:32"
                                },
                                {
                                    "title": "Comida Sabado",
                                    "amount": 5340.0,
                                    "category": "Comida Afuera",
                                    "type": "Expense",
                                    "date": "2025-09-28 16:42:06"
                                },
                                {
                                    "title": "Comida Viernes",
                                    "amount": 32567.0,
                                    "category": "Comida Afuera",
                                    "type": "Expense",
                                    "date": "2025-09-28 16:48:04"
                                }]
    
def test_get_income_movements_type ():
    #Arrange
    
    #Act
    expense_movements = summary.get_movement_per_type(movements,"income")
    #Assert
    assert expense_movements == [
                                    {
                                        "title": "Salario",
                                        "amount": 737464738.0,
                                        "category": "Salario",
                                        "type": "Income",
                                        "date": "2025-09-28 16:49:59"
                                    }]

def test_calculate_income_amount ():
    #Arrange
    income_movements = [
                            {
                                "title": "Salario",
                                "amount": 7374647.0,
                                "category": "Salario",
                                "type": "Income",
                                "date": "2025-09-28 16:49:59"
                            },
                            {
                                "title": "Salario 2",
                                "amount": 3456237,
                                "category": "Salario",
                                "type": "Income",
                                "date": "2025-09-28 16:49:59"
                            }]
    
    #Act
    income_total = summary.calculate_amount(income_movements)

    #Assert
    assert income_total == 10830884.0

def test_calculate_expense_amount ():
    #Arrange
    expense_movements = [
                            {
                                "title": "Diario Mitad Agosto",
                                "amount": 64900.0,
                                "category": "Supermercado",
                                "type": "Expense",
                                "date": "2025-08-28 16:40:09"
                            },
                            {
                                "title": "Comida Domingo",
                                "amount": 15439.0,
                                "category": "Comida Afuera",
                                "type": "Expense",
                                "date": "2025-09-28 16:41:32"
                            },
                            {
                                "title": "Comida Sabado",
                                "amount": 5340.0,
                                "category": "Comida Afuera",
                                "type": "Expense",
                                "date": "2025-09-28 16:42:06"
                            },
                            {
                                "title": "Comida Viernes",
                                "amount": 32567.0,
                                "category": "Comida Afuera",
                                "type": "Expense",
                                "date": "2025-09-28 16:48:04"
                            }]
    
    #Act
    expense_total = summary.calculate_amount(expense_movements)

    #Assert
    assert expense_total == 118246.0
