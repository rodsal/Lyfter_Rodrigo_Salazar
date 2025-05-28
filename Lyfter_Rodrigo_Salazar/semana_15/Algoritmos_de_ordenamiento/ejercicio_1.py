"""
Crea un bubble_sort por tu cuenta sin revisar el código de la lección.
"""

def bubble_sort(list_ordered):
    for main_index in range(len(list_ordered)-1):
        changes_made = False
        for index in range(len(list_ordered)-1-main_index):
            current_item = list_ordered[index]
            next_item = list_ordered[index+1]
            if current_item > next_item:
                list_ordered[index+1] = current_item
                list_ordered[index] = next_item
                changes_made = True
        if not changes_made:
            break
    return list_ordered

list_sort = [33, 4, 32, 52, 9, 15]
print(bubble_sort(list_sort))

