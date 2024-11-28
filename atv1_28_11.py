class Super:
    def __init__(self):
        self.nome= input("Digite o seu nome: ")
        self.end = input("Digite seu endereço: ")
        self.tel = input("Digite o seu telefone: ")
        self.email= input("Digite seu E-mail: ")
        
        

class Sub(Super):
    def dado1(self):
        self.rg = input("Digite o seu rg: ")
        self.cpf= input("Digite seu cpf: ")  
        
class Subsub(Super):
    def dado1(self):
        self.CNPJ = input("Digite o seu CNPJ: ")
        self.ie= input("Digite sua IE: ")  
