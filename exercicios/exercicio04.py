#criar uma classe de nome inventário com atributos de classe pre definidos, item1 e item2 a serem cadastrados
#manualmente pelo usuário simulando um carrinho de compras:

class Inventario:
    def __init__(self, item1, item2):
        self.item1 = item1
        self.item2 = item2

cliente1 = Inventario("bombeta branca e vinho", "moletom da adidas")
print(f'{cliente1.item1} e {cliente1.item2}')

#aqui percebemos uma coisa interessante. forçamos que no momento de instanciar uma classe precisamos passar parametros
#ao colocar como parametro os itens na função construtora.