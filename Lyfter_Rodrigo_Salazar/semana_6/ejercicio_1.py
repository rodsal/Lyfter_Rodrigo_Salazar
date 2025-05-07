def return_sum_with_text():
    sum = sum_of_numbers(5,6)
    return "La suma de los dos numeros es: " + str(sum)


def sum_of_numbers(num_1,num_2):
    return num_1 + num_2

print (return_sum_with_text())