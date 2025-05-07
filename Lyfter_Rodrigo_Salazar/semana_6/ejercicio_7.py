def return_prime_number(list_of_numbers):
    prime_number_list = []
    for number in list_of_numbers:
        if is_prime_number(number):
            prime_number_list.append(number)
    return prime_number_list

def is_prime_number(number):
    if number < 2:
        return False
    for division in range(2, number):
        if number % division == 0:
            return False
    return True

list_to_validate = [1, 4, 6, 7, 13, 9, 67]
print(return_prime_number(list_to_validate))