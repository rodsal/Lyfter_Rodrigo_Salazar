import pytest
from semana_16.bubble_sort import bubble_sort

def test_bubble_sort_with_samll_list():
    #Arrange
    list_to_order = [23, 1, 86, 46, 32, 15, 29]
    #Act
    result = bubble_sort(list_to_order)
    #Asssert
    assert result == [1, 15, 23, 29, 32, 46, 86]

def test_bubble_sort_with_big_list_more_than_100_elements():
    #Arrange
    list_to_order = [32, 46, 45, 78, 23, 31, 89, 345, 123, 243, 930, 203, 658, 121, 48, 92, 67, 143, 15, 74,
                 56, 82, 342, 311, 462, 70, 20, 2, 90, 66, 632, 811, 156, 139, 1, 78, 172, 134, 29, 10,
                 42, 111, 190, 126, 63, 92, 75, 103, 109, 35, 80, 52, 26, 71, 84, 7, 36, 173, 62, 58, 4,
                 102, 47, 645, 600, 100, 199, 123, 122, 834, 690, 456, 421, 437, 555, 587, 324, 284, 217, 276,
                 423, 461,402, 201, 222, 423, 923, 562, 888, 777, 512, 464, 274, 430, 860, 112, 444, 555, 208,
                 824, 779, 773, 12]
    #Act
    result = bubble_sort(list_to_order)
    #Asssert
    assert result == [1, 2, 4, 7, 10, 12, 15, 20, 23, 26, 29, 31, 32, 35, 36, 42, 45, 46, 47, 48, 52, 56, 58, 62, 63, 66, 67, 70, 71, 74, 75, 78, 78, 80, 82, 84, 89, 90, 92, 92, 100, 102, 103, 109, 111, 112, 121, 122, 123, 123, 126, 134, 139, 143, 156, 172, 173, 190, 199, 201, 203, 208, 217, 222, 243, 274, 276, 284, 311, 324, 342, 345, 402, 421, 423, 423, 430, 437, 444, 456, 461, 462, 464, 512, 555, 555, 562, 587, 600, 632, 645, 658, 690, 773, 777, 779, 811, 824, 834, 860, 888, 923, 930]


def test_bubble_sort_with_empty_list():
    #Arrange
    list_to_order = []
    #Act
    result = bubble_sort(list_to_order)
    #Asssert
    assert result == []


def test_bubble_sort_with_items_in_list_not_numbers():
    #Arrange
    list_to_order = [2,4,10, "f"]
    #Act
    with pytest.raises(TypeError):
        bubble_sort(list_to_order)





