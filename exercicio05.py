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

#aqui eu uso como atributo de classe o **kwargs onde ele permite que nos possamos passar valores novos para 
#uma instancia a partir de uma instancia.key de forma que a instancia.key recebe um valor. isso dentro do 
# escopo da classe, funcionaria da mesma forma em uma função comum. caso quisessemos passar os argumentos na forma
# de posicao usariamos *args (nesse caso não faz sentido mas vale ressaltar, pois a loógica funciona para o 
# escopo de funções também.) 
