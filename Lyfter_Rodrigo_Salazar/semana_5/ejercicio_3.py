list_to_modify = [4, 3, 6, 1, 7]
last_item = list_to_modify.pop(len(list_to_modify)-1)
first_item = list_to_modify.pop(0)

list_to_modify.insert(0,last_item)
list_to_modify.insert(len(list_to_modify), first_item)
print(list_to_modify)