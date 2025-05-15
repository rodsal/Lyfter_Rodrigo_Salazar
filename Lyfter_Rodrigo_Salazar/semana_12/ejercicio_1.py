"""
1. Cree una clase de `BankAccount` que:
    1. Tenga un atributo de `balance`.
    2. Tenga un método para ingresar dinero.
    3. Tengo un método para retirar dinero.
    
    Cree otra clase que herede de esta llamada `SavingsAccount` que:
    
    1. Tenga un atributo de `min_balance` que se pueda asignar al crearla.
    2. Arroje un error si al intentar retirar dinero, el retiro haría que el `balance` quede debajo del `min_balance`. 
    Es decir que sí se pueden hacer retiros **siempre y cuando** el `balance` quede arriba del `min_balance`.
"""

from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance):
         self.balance = balance

    @abstractmethod
    def _substract_money(self, amount):
        self.balance -= amount

class SavingAccount (BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance
    
    def _substract_money(self, amount):
        if amount < self.balance:
            if (self.balance - amount) >= self.min_balance:
                super()._substract_money(amount)
                print ("Se retiró " + str(amount) + " de la cuenta con un balance de = " + str(self.balance))
            else:
                print("El balance no puede ser menor a " + str(self.min_balance) + " que es lo permitido en la cuenta")
        else:
            print("El monto a retirar no puede ser mayor al monto que tiene en el balance")
        


savings_1 = SavingAccount(2000,300)
savings_1._substract_money(1700)