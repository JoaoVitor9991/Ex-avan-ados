class Super:
    def hello(self):
        print("Olá, eu sou a super")
class Sub(Super):
    def hello(self):
        print("Olá, eu sou a sub")
class Subsub (Sub):
    def hello(self):
        print("Olá, sou a subsubclasse! ")
teste = Subsub()
teste.hello()