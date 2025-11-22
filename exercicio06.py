#crie uma calculadora simples com as 4 operações básicas (soma, subtração, multiplicação e divisão) usando apenas POO.

class Calculadora:
    def __init__(self):
        pass

    def soma(self, a, b):
        return a + b
    def subtracao(self, a, b):
        return a - b
    def multiplicacao(self, a, b):
        return a * b
    def divisao(self, a, b):
        if b != 0:
            retorno = a / b
        else:
            retorno =  "Erro: Divisão por zero não é permitida."
        return retorno

calc = Calculadora()
print(f"a soma de 66 e 33 é {calc.soma(66,33)}")
print(f"a divisao de 66 e 0 é {calc.divisao(66,0)}")
print(f"a subtração de 100 e 45 é {calc.subtracao(100,45)}")
print(f"a multiplicação de 12 e 11 é {calc.multiplicacao(12,11)}")

#o exercicio é simples, mas é uma boa prática para entender o conceito de classes e métodos em POO.