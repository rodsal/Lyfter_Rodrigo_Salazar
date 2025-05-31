
import sys
import os

# Agrega la raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from semana_6 import ejercicio_3

def test_excercise_3_sum_of_small_numbers ():
    #Arrange
    list_to_sum = [1,2,3]
    #Act
    sum_numbers = ejercicio_3.sum_of_list(list_to_sum)
    #Assert
    assert sum_numbers == 6

def test_excercise_3_sum_of_large_numbers():
    #Arrange
    list_to_sum = [76273, 9302389, 723236, 8723, 16317, 76236, 9372, 7642, 92092]
    #Act
    sum_of_large_nummbers = ejercicio_3.sum_of_list(list_to_sum)
    #Assert
    assert sum_of_large_nummbers == 10312280

def test_excercise_3_sum_of_big_list_of_elements():
    #Arrange
    list_to_sum = [32, 46, 45, 78, 23, 31, 89, 345, 123, 243, 930, 203, 658, 121, 48, 92, 67, 143, 15, 74,
                 56, 82, 342, 311, 462, 70, 20, 2, 90, 66, 632, 811, 156, 139, 1, 78, 172, 134, 29, 10,
                 42, 111, 190, 126, 63, 92, 75, 103, 109, 35, 80, 52, 26, 71, 84, 7, 36, 173, 62, 58, 4,
                 102, 47, 645, 600, 100, 199, 123, 122, 834, 690, 456, 421, 437, 555, 587, 324, 284, 217, 276,
                 423, 461,402, 201, 222, 423, 923, 562, 888, 777, 512, 464, 274, 430, 860, 112, 444, 555, 208,
                 824, 779, 773, 12]
    #Act
    sum_of_large_nummbers = ejercicio_3.sum_of_list(list_to_sum)
    #Assert
    assert sum_of_large_nummbers == 27216







