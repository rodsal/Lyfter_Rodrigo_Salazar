def sum_of_list (in_list):
    total_sum = 0
    for number in in_list:
        total_sum = total_sum + number
    return total_sum

list_to_sum = [47, 62, 29, 29]
print(sum_of_list(list_to_sum))