import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from category_list import Categories

categories = Categories()

def test_add_new_category ():
    #Arrange
    new_category = "Nueva Categoría2"
    #Act
    add = Categories.add_category(categories,new_category)
    #Assert
    assert add == True


def test_add_category_already_added ():
    #Arrange
    category = "Salario"
    #Act
    add = Categories.add_category(categories,category)
    #Assert
    assert add == False
