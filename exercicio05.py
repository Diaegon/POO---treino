#criar uma classe Biblioteca que possui uma estrutura molde básica para cadastro de um livros
#de acordo com seu título, porém que espera a inclusão de um número não definido de titulos.
#em seguida cadastre 5 livros na biblioteca
from pprint import pprint
class Biblioteca:
    def __init__(self, livro, **kwargs):
        self.livro = livro

dic = {'livro6': 'livro6', 'livro7':'livro7' }

plateleira1 = Biblioteca('livro1')
plateleira1.livro2 = 'livro2'
plateleira1.livro3 = 'livro3'
plateleira1.livro4 = 'livro4'
plateleira1.livro5 = 'livro5'

print(plateleira1.livro5, plateleira1.livro4)
pprint(type(plateleira1.livro2))
#pequeno raciocionio sobre argumentos de funcoes no python, uma função com argumentos que precisam ser passados como parametros
#podem ser passados os parametros pela posição do argumento dentro do parentesis da funão ou pelo seu keyword.

#a resolução do exercicio propoe o uso do **kwargs para a criação de atributos dinâmicos dentro da classe. mas não faz sentido
#usar o **kwargs para passar os atributos dinamicamente dentro do escopo da classe, uma vez que o **kwargs é usado para
#passar argumentos de forma dinamica para funções. então o uso do **kwargs dentro do escopo da classe não faz sentido.


