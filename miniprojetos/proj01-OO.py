class RetornaLista():
    def __init__(self):
        #passando o input como um objeto do método construtor, assim que instanciamos a classe no programa
        #ele inicializa o objeto pedindo a entrada dos dados.
        #  self.input = input("Digite 5 números quaisquer entre 0 - 99, separados por virgula")
        #podemos passar também um método que constroi o objeto e a partir dele ja checa se ele tem o tamanho correto.
        self.orquestra_fluxo_e_retorna()
        pass

    def orquestra_fluxo_e_retorna(self):
        self.inicializa_fluxo()
        print("aqui passou")
        self.retorno = [int(item) for item in self.lista_numeros ]
        print(self.retorno)
        

    def inicializa_fluxo(self):    
        while True:
            self.inicializa_objeto()
            checagem_tamanho = self.checagem_tamanho(self.lista_numeros)
            checagem_numeros = self.checagem_numeros(self.lista_numeros)
            if checagem_tamanho and checagem_numeros:
                break

    #recebe e valida
    def inicializa_objeto(self):
        self.input = input("Digite 5 números quaisquer entre 0 - 99, separados por virgula")
        self.lista_numeros = self.input.split(",")
        return self.lista_numeros
        
    
    def checagem_numeros(self,parametro):
        for item in parametro:
            if int(item) > 99 or int(item) < 0:
                print(f"o numero fora do range: {item}")
                return False
        return True

    def checagem_tamanho(self,parametro):
        while len(parametro) != 5:
            print("quantidade de numeros diferente")
            return False
        return True

teste = RetornaLista()