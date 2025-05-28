def bubble_sort(list_ordered):
    for main_index in range(len(list_ordered)-1):           # O (n)
        changes_made = False                                # O (1)
        for index in range(len(list_ordered)-1-main_index): # O (n)
            current_item = list_ordered[index]              # O (1)
            next_item = list_ordered[index+1]               # O (1)
            if current_item > next_item:                    # O (1)
                list_ordered[index+1] = current_item        # O (1)
                list_ordered[index] = next_item             # O (1)
                changes_made = True                         # O (1)
        if not changes_made:                                # O (1)
            break                                           # O (1)
    return list_ordered                                     # O (1)

# Big O notation = O (n)

