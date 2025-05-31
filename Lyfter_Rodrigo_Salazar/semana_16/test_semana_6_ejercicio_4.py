import pytest
import sys
import os

# Agrega la raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from semana_6 import ejercicio_4

def test_excercise_4_revert_a_small_text ():
    #Arrange
    text_to_reverse = "Hola mi nombre es Rodrigo"
    #Act
    reversed_text = ejercicio_4.revert_text(text_to_reverse)
    #Assert
    assert reversed_text == "ogirdoR se erbmon im aloH"


def test_excercise_4_input_not_text():
    #Arrange
    input_text = 1233455
    # Act
    with pytest.raises(TypeError):
        ejercicio_4.revert_text(input_text)

def test_excercise_4_revert_long_text():
    #Arrange
    long_text = "Era un pueblecito rayano, Ribamoura, vivero de contrabandistas, donde esta profesión de riesgo y lucro hacía a la gente menos dormida de lo que suelen ser los pueblerinos."
   
    #Act
    revert_long_text = ejercicio_4.revert_text(long_text)
    #Assert
    assert revert_long_text == ".sonirelbeup sol res neleus euq ol ed adimrod sonem etneg al a aícah orcul y ogseir ed nóiseforp atse ednod ,satsidnabartnoc ed oreviv ,aruomabiR ,onayar oticelbeup nu arE"






