class RetornaLista():
    def __init__(self):
        #passando o input como um objeto do método construtor, assim que instanciamos a classe no programa
        #ele inicializa o objeto pedindo a entrada dos dados.
        #  self.input = input("Digite 5 números quaisquer entre 0 - 99, separados por virgula")
        #podemos passar também um método que constroi o objeto e a partir dele ja checa se ele tem o tamanho correto.
        #self.orquestra_fluxo_e_retorna()
        #troquei a classe orquestra_fluxo... pelo método executar, onde no caso só vai executar com uma chamada 
        #de quem está executando o código e não automaticamente
        pass

    def executar(self):
        self._inicializa_fluxo()
        
    #defini os métodos internos que não são acessíveis fora da classe. 
    def _inicializa_fluxo(self):    
        while True:
            if not self._inicializa_objeto():
                continue

            if not self._checagem_tamanho(self.numeros):
                continue

            if not self._checagem_numeros(self.numeros):
                continue

            print(self.numeros)
            break

   
    def _inicializa_objeto(self):
        self.input = input("Digite 5 números quaisquer entre 0 - 99, separados por virgula")
        self.lista_numeros = self.input.split(",")
        try:
            self.numeros = list(map(int,self.lista_numeros))
        except ValueError:
            print("os valores devem ser numeros inteiros")
            return False

        return self.numeros
        
    
    def _checagem_numeros(self,parametro):
        for item in parametro:
            if item > 99 or item < 0:
                print(f"o numero fora do range: {item}")
                return False
        return True

    def _checagem_tamanho(self,parametro):
        if len(parametro) != 5:
            print("quantidade de numeros diferente")
            return False
        return True

teste = RetornaLista()
teste.executar()