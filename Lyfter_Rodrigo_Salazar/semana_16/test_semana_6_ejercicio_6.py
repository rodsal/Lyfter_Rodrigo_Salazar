import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from semana_6 import ejercicio_6


def test_excercise_6_all_text_with_same_start_letter():
    #Arrange
    input_text = "este-es-el-escribir-estando-estudiando"
    # Act
    text_ordered = ejercicio_6.order_text_by_alphabet(input_text)
    #Assert
    assert text_ordered == "el-es-escribir-estando-este-estudiando"


def test_excercise_6_all_letters_different():
    #Arrange
    input_text = "padre-jocote-amar-gota-empatia-tribial-hyundai-camarote"
    #Act
    text_ordered = ejercicio_6.order_text_by_alphabet(input_text)
    #Assert
    assert text_ordered == "amar-camarote-empatia-gota-hyundai-jocote-padre-tribial"


def test_excercise_6_input_not_text():
    #Arrange
    input_text = ""
    # Act
    text_ordered = ejercicio_6.order_text_by_alphabet(input_text)
    #Assert
    assert text_ordered == ""




