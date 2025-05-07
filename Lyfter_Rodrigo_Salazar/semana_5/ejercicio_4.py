number_list = [1,2,3,4,5,6,7,8,9,10,11,11,11,11,11]
pair_number_list = []
for number in number_list:
    if number % 2 == 0:
        pair_number_list.append(number)
print(pair_number_list)