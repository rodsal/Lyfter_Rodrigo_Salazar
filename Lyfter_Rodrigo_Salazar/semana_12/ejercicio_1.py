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
    
    def add_money (self, amount):
        self.balance += amount
    
    def substract_money(self, amount):
        self.balance -= amount
    
    @abstractmethod
    def withdraw ():
        pass

class SavingAccount (BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance
    
    def withdraw (self, amount):
        if amount < self.balance:
            if (self.balance - amount) >= self.min_balance:
                self.substract_money(amount)
                print ("You withdraw " + str(amount) + " form your savings account, now you have a balance of " + str(self.balance))
            else:
                raise ValueError ("The balance can´t be lower than " + str(self.min_balance) + " that is the minimun value permitted on the account")
        else:
            raise ValueError ("The amount withdrawn can´t be greater to the amount in your account")
        


savings_1 = SavingAccount(2000,300)
savings_1.withdraw(3000)