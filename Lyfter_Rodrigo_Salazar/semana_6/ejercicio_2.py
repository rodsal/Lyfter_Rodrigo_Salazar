def multiply_numbers(num_a, num_b):
    multiply = num_a * num_b
    return multiply

print(multiply_numbers)

global_varibale = 5

def funcion_1():
    global_varibale = 7
    return global_varibale
print(funcion_1())