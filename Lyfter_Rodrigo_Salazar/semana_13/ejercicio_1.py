"""
Cree un decorador que haga print de los parámetros y retorno de la función que decore.
"""

def paramter_print(func):
    def wrapper(name, age):
        print("Name: " + str(name) + " - Age: " + str(age))
        return func(name, age)
    return wrapper

@paramter_print
def employee_under_age(name, age):
    legal_age = False
    name_len = len(name)
    print(name_len)
    if age > 18:
        print("The employee is on legal age ")
        legal_age = True
    else:
        raise ValueError("The emplyee is under age")
    return legal_age, name_len


employee_under_age("Rodrigo", 27)


