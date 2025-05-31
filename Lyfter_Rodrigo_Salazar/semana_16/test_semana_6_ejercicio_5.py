import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from semana_6 import ejercicio_5

def test_excercise_5_count_upper_and_lower_case_in_small_text ():
    #Arrange
    text_to_count = "Hola mi nombre es Rodrigo"
    #Act
    lower_case,upper_case = ejercicio_5.print_upper_lower_cases(text_to_count)
    #Assert
    assert upper_case == 2 and lower_case == 19


def test_excercise_5_input_not_text():
    #Arrange
    input_text = 1233455
    # Act
    with pytest.raises(TypeError):
        ejercicio_5.print_upper_lower_cases(input_text)

def test_excercise_5_all_letters_upper_case():
    #Arrange
    upper_case_text = "ESTE TEXTO ES TODO EN MAYÚSCULA."
    #Act
    lower_case, upper_case = ejercicio_5.print_upper_lower_cases(upper_case_text)
    #Assert
    assert upper_case == 26 and lower_case == 1






