import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from semana_6 import ejercicio_7


def test_excercise_7_small_list_of_numbers():
    #Arrange
    input_list = [23,85,76,92,68,12,3,7]
    # Act
    prime_list = ejercicio_7.return_prime_number(input_list)
    #Assert
    assert prime_list == [23,3,7]


def test_excercise_7_no_prime_numbers_in_the_list():
    #Arrange
    input_list = [56,72,68,90,76,40]
    #Act
    prime_list = ejercicio_7.return_prime_number(input_list)
    #Assert
    assert prime_list == []


def test_excercise_7_list_of_big_numbers():
    #Arrange
    input_list = [2147483647, 100000007, 1000004, 7777777, 100000037, 100000039, 9876543, 100000073, 100000081, 
                  4000000, 100000123, 100000127, 100000193, 100000213, 1234560]
    # Act
    prime_list = ejercicio_7.return_prime_number(input_list)
    #Assert
    assert prime_list == [2147483647, 100000007, 100000037, 100000039, 100000073, 
                          100000081, 100000123, 100000127, 100000193, 100000213]




