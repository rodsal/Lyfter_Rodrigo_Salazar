"""
Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, 
y arroje una excepción de no ser así.
"""

def is_number(func):
    def wrapper(*args):       
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError ("There are parameters that are not numbers")
        return func(*args)
    return wrapper

@is_number
def number_counter(*args):
    counter = 0
    for arg in args:
        counter = counter + arg
    return counter


calculate_number = number_counter(10,4,6,7,8, 4.5, 4.7)
print(calculate_number)




