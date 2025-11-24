#Escreva um programa que recebe do usuario 5 números quaisquer no intervalo de 0 a 99, separados por vírgula.
#tanto em formato de listam quanto em conjunto numérico.

#no segundo momento aprimore o código para validações, primeiro se foram inseridos 5 e depois se eles estão no intervalo de 0 a 99.

#no terceiro momento refatore o código para que ele utilize POO.


#primeira parte



def check_numeros(tupla_valores):
    for item in tupla_valores:
        if int(item) > 99:
            print("Entrada inválida: todos os números devem estar no intervalo de 0 a 99. Tente novamente.")
            return False
    for item in tupla_valores:
        if int(item) < 0:
            print("Entrada inválida: todos os números devem estar no intervalo de 0 a 99. Tente novamente.")
            return False
    return True

def transforma_inteiro(tupla_valores):
    lista_final = []
    for item in tupla_valores:
        lista_final.append(int(item))
    return lista_final

def check_tamanho():
    entrada = input("Digite 5 números quaisquer entre 0 - 99, separados por virgula")
    entrada = entrada.split(",")
    while len(entrada) != 5:
        entrada = input("Digite 5 números quaisquer entre 0 - 99, separados por virgula")
        entrada = entrada.split(",")
        tupla_valores = tuple(entrada)
        checagem = check_numeros(tupla_valores)
        if checagem == True and len(entrada) == 5:
            saida = transforma_inteiro(tupla_valores)
            print(saida)
        else:
            check_tamanho()

    if len(entrada) == 5:
        tupla_valores = tuple(entrada)
        checagem = check_numeros(tupla_valores)
        if checagem == True:
            saida = transforma_inteiro(tupla_valores)
            print(saida)
        else:
            check_tamanho()

check_tamanho()


#aqui vemos que o programa retorna o que foi pedido no projeto, porém o código está confuso e bastante acoplado
#a necessidade de fazer toda a lógica usando funções me fez deduzir que esse projeto seria resolvido de forma mais simples
#utilizando programação orientada a objeto. partimos para o próximo passo do projeto.