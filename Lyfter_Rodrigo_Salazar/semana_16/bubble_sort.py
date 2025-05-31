
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

