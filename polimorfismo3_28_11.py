class Super:
    def print(self):
        print("Olá, eu sou o super FODA")
class Sub(Super):
    def hello(self):
        print("Olá, eu sou a sub")
class Subsub (Sub):
    def hello(self):
        print("Olá, sou a subsubclasse! ")
teste = Super()
teste.print()