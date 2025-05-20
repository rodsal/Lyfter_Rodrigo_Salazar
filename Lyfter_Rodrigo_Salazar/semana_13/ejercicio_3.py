import datetime

"""
3. Cree una clase de `User` que:
    - Tenga un atributo de `date_of_birth`.
    - Tenga un property de `age`.
    
    Luego cree un decorador para funciones que acepten un `User` como parámetro que se encargue de revisar si el `User` 
    es mayor de edad y arroje una excepción de no ser así.
"""
def is_under_age(func):
    def wrapper(user):       
        today = datetime.date.today()
        calculate_age = today.year - user.date_of_birth.year
        if (today.month, today.day) < (user.date_of_birth.month, user.date_of_birth.day):
            calculate_age -= 1
        if calculate_age < 18:
            raise ValueError ("The user is under age.")
        return func(user)
    return wrapper


class User():

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = datetime.date.today()
        calculate_age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            calculate_age -= 1
        return calculate_age
    

    @is_under_age
    def over_age(self):
        print("Is over 18 years old")

fecha_nacimiento = datetime.datetime(2015,1,1)
new_user = User(fecha_nacimiento)
print(new_user.age)
new_user.over_age()

