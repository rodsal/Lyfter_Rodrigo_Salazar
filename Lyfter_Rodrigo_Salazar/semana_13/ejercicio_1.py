"""
Cree un decorador que haga print de los parámetros y retorno de la función que decore.
"""

def paramter_print(func):
    def wrapper(name, age):
        print("Name: " + str(name) + " - Age: " + str(age))
        func(name, age)
    return wrapper

@paramter_print
def employee_under_age(name, age):
        name_len = len(name)
        print(name_len)
        if age > 18:
            print("The employee is on legal age ")
        else:
            raise ValueError("The emplyee is under age")


employee_under_age("Rodrigo", 27)


