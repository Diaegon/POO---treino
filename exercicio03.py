#criar uma classe pessoa com metodo construtor e alguns objetos de classe vazios dentro, que representem as características 

class Pessoa:
    def __init__(self):
        self.nome = None
        self.idade = None
        self.altura = None
        self.peso = None
        self.sexo = None
#a priori percebemos que ao criar uma classe os atributos são todos self, então são atributos da instancia. não precis
#repassar parametros para a mesma. 
#
#E não podemos crir varivaveis/objetos vazios em pyhton, temos q repassar algum valor, utilizamos a palavra None
#para informar ao interpretador que no momento da instancia esse atributo vai ser vazio, porém poderá se alterado
#no decorrer e sua estrutura é iterável.

diego = Pessoa()
diego.nome = "diego" 
print(diego.nome)