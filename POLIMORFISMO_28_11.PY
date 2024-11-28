class Super:
    def hello(self):
        print("Olá, eu sou a superclasse! ")

teste = Super()
teste.hello()

class Sub(Super):
    def hello(self):
        print("Olá, eu sou a subclasse! ")     
teste=Sub()
teste.hello()