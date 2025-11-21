#criar classe que armazena algumas carcterísticas de um carro e em seguida criar dois carros distintos.
class Carro:
    ano = 2025
    cor = 'vermelho'
    modelo = 'sedan'
    opcionais = 'rodao'
#com a classe feita, criamos nossa instancia.

carro1 = Carro()
carro2 =  Carro()

carro2.ano = 2017
carro2.cor = "preto"
carro2.modelo = "hatch"
carro2.opcionais = 'paredao'

print(f"o ano do carro 1 é {carro1.ano}, a cor é {carro1.cor} o modelo é {carro1.modelo} e o opcional é {carro1.opcionais} ")
print(f"o ano do carro 2 é {carro2.ano}, a cor é {carro2.cor} o modelo é {carro2.modelo} e o opcional é {carro2.opcionais} ")