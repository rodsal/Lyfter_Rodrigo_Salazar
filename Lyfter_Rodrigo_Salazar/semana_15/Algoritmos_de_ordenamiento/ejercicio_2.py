"""
Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero 
(como en la imagen de abajo).
"""

def bubble_sort_reverse(list_ordered):
    for main_index in range(0, (len(list_ordered))):
        changes_made = False
        for index in range(len(list_ordered)-1, main_index, -1):
            current_item = list_ordered[index]
            item_before = list_ordered[index-1]
            if current_item < item_before:
                list_ordered[index-1] = current_item
                list_ordered[index] = item_before
                changes_made = True
        if not changes_made:
            break
    return list_ordered

list_reverse = [6, 5, 4, 3, 2, 1]
print(bubble_sort_reverse(list_reverse))
