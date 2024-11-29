class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def combustivel(self):
        return "Desconhecido"

    def passageiros(self):
        return 0



class Carro(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.tipo = "Carro"

    def combustivel(self):
        return "Gasolina"

    def passageiros(self):
        return 5



class Moto(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.tipo = "Moto"

    def combustivel(self):
        return "Gasolina"

    def passageiros(self):
        return 2



class Caminhao(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.tipo = "Caminhão"

    def combustivel(self):
        return "Diesel"

    def passageiros(self):
        return 2



def veiculos():
    veiculos = [
        Carro("Ford", "Fiesta"),
        Moto("Yamaha", "MT-07"),
        Caminhao("Mercedes-Benz", "Actros")
    ]

    for veiculo in veiculos:
        print(f"Tipo: {veiculo.tipo}")
        print(f"Marca: {veiculo.marca}")
        print(f"Modelo: {veiculo.modelo}")
        print(f"Tipo de Combustível: {veiculo.combustivel()}")
        print(f"Capacidade de Passageiros: {veiculo.passageiros()}")
        print("=" * 30)



veiculos()