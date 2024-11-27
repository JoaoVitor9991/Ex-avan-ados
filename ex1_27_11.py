class Account:
    def __init__(self, number: int, holder: str, balance: float):
        self.number = number
        self.holder= holder
        self.balance = balance

    def withdraw(self, amount: float):
        if amount > 0 and amount <= self.balance:
            self.balance =- amount 
            


    def deposit(self, amount:float):
        if amount >0:
            self.balance += amount
        else:
            print("Valor inválido. ")
    def __str__(self):
        return f"Conta{self.number}, {self.balance}, Balance: {self.balance:.2f}"

     
