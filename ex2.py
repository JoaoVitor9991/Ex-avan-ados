from ex1_27_11 import * 

class BussinerAccount(Account):
    def __init__(self, number: str, holder: str, balance:float, loanLimit:float):
        super().__init__(number, holder, balance)
        self.loanLimit = loanLimit
    def loan(self, amount:float):
        if amount > 0 and amount <= self.loanLimit:
            self.balance += amount
        else:
            print("Valor inválido ou sem limite. ")
    def __str__(self):
        return f"Bussines Conta {self.number}, {self.holder}, Balance: {self.balance:.2f}, LonLimit:{self.loanLimit}"

acc = Account(123, "João", 400.0)
print(f"Primeiro Print: {acc}")
acc.deposit(5.50)
print(f"Segundo Print: {acc}")
acc.withdraw(2000) 
print(f"Terceiro Print: {acc}")


b_acc = BussinerAccount(321, "GYm", 1000, 200.000)
print(f"BC: {b_acc}")
b_acc.loan(239)
print(f"2 BC: {b_acc}")        
