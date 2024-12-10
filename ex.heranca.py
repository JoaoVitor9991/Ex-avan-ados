class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def tipo_combustivel(self):
        return "Desconhecido"

    def capacidade_passageiros(self):
        return 0



class Carro(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.tipo = "Carro"

    def tipo_combustivel(self):
        return "Gasolina"

    def capacidade_passageiros(self):
        return 5



class Moto(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.tipo = "Moto"

    def tipo_combustivel(self):
        return "Gasolina"

    def capacidade_passageiros(self):
        return 2



class Caminhao(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.tipo = "Caminhão"

    def tipo_combustivel(self):
        return "Diesel"

    def capacidade_passageiros(self):
        return 2



def demonstrar_veiculos():
    veiculos = [
        Carro("Ford", "Fiesta"),
        Moto("Yamaha", "MT-07"),
        Caminhao("Mercedes-Benz", "Actros")
    ]

    for veiculo in veiculos:
        print(f"Tipo: {veiculo.tipo}")
        print(f"Marca: {veiculo.marca}")
        print(f"Modelo: {veiculo.modelo}")
        print(f"Tipo de Combustível: {veiculo.tipo_combustivel()}")
        print(f"Capacidade de Passageiros: {veiculo.capacidade_passageiros()}")
        print("=" * 30)



demonstrar_veiculos()