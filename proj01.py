#Escreva um programa que recebe do usuario 5 números quaisquer no intervalo de 0 a 99, separados por vírgula.
#tanto em formato de listam quanto em conjunto numérico.

#no segundo momento aprimore o código para validações, primeiro se foram inseridos 5 e depois se eles estão no intervalo de 0 a 99.

#no terceiro momento refatore o código para que ele utilize POO.


#primeira parte

entrada = input("Digite 5 números quaisquer entre 0 - 99, separados por virgula")
entrada = entrada.split(",")
saida = []

while len(entrada) != 5:
    entrada = input("Digite 5 números quaisquer entre 0 - 99, separados por virgula")
    entrada = entrada.split(",")
    if len(entrada) == 5:
        tupla_valores = tuple(entrada)

print(tupla_valores)


for item in saida:
    if item > 99:
        print("Entrada inválida: todos os números devem estar no intervalo de 0 a 99. Tente novamente.")
        entrada = input("Digite 5 números quaisquer entre 0 - 99, separados por virgula")
        entrada = entrada.split(",")

for item in saida:
    if item < 0:
        print("Entrada inválida: todos os números devem estar no intervalo de 0 a 99. Tente novamente.")
        entrada = input("Digite 5 números quaisquer entre 0 - 99, separados por virgula")
        entrada = entrada.split(",")

print(f"A entrada é{saida}")
