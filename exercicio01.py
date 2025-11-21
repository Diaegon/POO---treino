#criar uma classe Pessoa com atributos e depois mostrar em tela esses atibutos.
class Pessoa:
    pass

pessoa1 = Pessoa() 
pessoa1.nome = 'Diego'

pessoa1.idade = '29'
pessoa1.profissao = 'Dev'

print(f' o nome da pessoa instanciada é {pessoa1.nome}, ela tem {pessoa1.idade} e trabalha como {pessoa1.profissao}')

#pessoa1 é uma instancia e Pessoa() é a classe, eu posso formar diversas instâncias a partir de classes