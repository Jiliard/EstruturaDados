#Alunos: Eduardo Boçon e Jiliard Peifer.


class objeto():

    def __init__(self, dado):
        self.__dado = dado
        self.__prox = None
        self.__anter = None
    
    def getDado(self):
        return self.__dado

    def setDado(self, dado):
        self.__dado = dado
    
    def getProx(self):
        return self.__prox

    def setProx(self, prox):
        self.__prox = prox

    def getAnter(self):
        return self.__anter
    
    def setAnter(self, anter):
        self.__anter = anter


class lista():

    def __init__(self, tamanho = 30):
        self.__prim = None
        self.__ult = None
        self.__cursor = None
        self.__tamanho = tamanho
        self.__quantidade = 0
      
    #feito
    def __avancarKPosicoes(self, k):
        for i in range(k):
            self.__cursor = self.__cursor.getProx()

    #feito
    def __retrocederKPosicoes(self, k):
        for i in range(k):
            self.__cursor = self.__cursor.getAnter()

    #feito
    def __irParaOPrimeiro(self):
        while self.__cursor.getAnter() != None:
            self.__cursor = self.__cursor.getAnter()

    #feito
    def __irParaOUltimo(self):
        while self.__cursor.getProx() != None:
            self.__cursor = self.__cursor.getProx()

    #feito
    def __Vazio(self) -> bool:
        if self.__prim == None:
            return True
        return False

    #feito
    def __Cheio(self) -> bool:
        if self.__quantidade >= self.__tamanho:
            return True
        return False
    
    #feito
    def __PosicaoDe(self, el) -> int:
        self.__irParaOPrimeiro()
        self.__ult.setProx(el)

        contador = 1

        while True:
            if self.__cursor.getDado() == el.getDado():
                break

            contador += 1
            self.__avancarKPosicoes(1)

        if self.__cursor == self.__ult.getProx():
            self.__ult.setProx(None)
            print("Exceção")

        else:
            self.__ult.setProx(None)
            return contador

    #feito
    def acessarAtual(self):
        return self.__cursor.getDado()
    
    #feito
    def InserirComoPrimeiro(self, el):
        novo = objeto(el)

        if self.__prim == None:
            self.__ult = novo
            self.__cursor = novo

        else:
            novo.setProx(self.__prim)
            self.__prim.setAnter(novo)

        self.__prim = novo

        self.__quantidade += 1

    #feito
    def InserirComoUltimo(self, el):
        novo = objeto(el)

        if self.__ult == None:
            self.__prim = novo
            self.__cursor = novo

        else:
            self.__ult.setProx(novo)

        self.__ult = novo

        self.__quantidade += 1

    #feito    
    def InserirNaPosicao(self, el, pos):
        self.__irParaOPrimeiro()
        self.__avancarKPosicoes(pos)
        self.InserirAntesDoAtual(el)

        self.__quantidade += 1

    #feito
    def InserirAntesDoAtual(self, el):
        novo = objeto(el)

        novo.setAnter(self.__cursor.getAnter())
        novo.setProx(self.__cursor)

        self.__cursor.getAnter().setProx(novo)
        self.__cursor.setAnter(novo)

        self.__quantidade += 1

    #feito
    def InserirDepoisDoAtual(self, el):
        novo = objeto(el)

        novo.setAnter(self.__cursor)
        novo.setProx(self.__cursor.getProx())

        self.__cursor.getPro().setAnter(novo)
        self.__cursor.setProx(novo)

        self.__quantidade += 1

    #feito
    def ExcluirAtual(self):
        self.__cursor.getAnter().setProx(self.__cursor.getProx())
        self.__cursor.getProx().setAnter(self.__cursor.getAnter())

        self.__avancarKPosicoes(1)

        self.__quantidade -= 1

    #feito
    def ExcluirPrim(self):
        if self.__Vazio():
            print("EXCEÇÃO")

        else:
            self.__prim = self.__prim.getProx()
            self.__prim.setAnt(None)

        self.__quantidade -= 1

    #feito
    def ExcluirUlt(self):
        if self.__Vazio():
            print("Exceção")

        else:
            self.__ult = self.__ult.getAnter()
            self.__ult.setProx(None)

        self.__quantidade -= 1

    #feito
    def ExcluirElemento(self, el):
        self.__irParaOPrimeiro

        self.__ult.setProx(el)

        while True:
            if self.__cursor.getDado() == el.getDado():
                break

            self.__avancarKPosicoes(1)

        if self.__cursor == self.__ult.getProx():
            print("Exceção")

        else:
            self.ExcluirAtual()
            self.__quantidade -= 1
        
        self.__ult.setProx(None)

    #feito
    def ExcluirDaPos(self, pos):
        self.__irParaOPrimeiro()    
        self.__avancarKPosicoes(pos - 1)

        self.ExcluirAtual()

        self.__quantidade -= 1

    #feito
    def Buscar(self, el):
        self.__irParaOPrimeiro()

        self.__ult.setProx(el)

        while True:
            if self.__cursor.getDado() == el.getDado():
                break

            self.__avancarKPosicoes(1)
            
        if self.__cursor == self.__ult.getProx():
            busca = False

        else:
            busca = True
        
        self.__ult.setProx(None)
        return busca

 
    def AcessaPrimeiro(self):
        return self.__prim.getDado()
    
    
    def AcessaUltimo(self):
        return self.__ult.getDado()
    
    
    def MostrarTudo(self):
        iterador = self.__prim

        while True:
            print(iterador.getDado())
            if iterador.getProx() == None: break
            iterador = iterador.getProx()

lista = lista()

lista.InserirComoUltimo(1)

lista.InserirComoUltimo(2)

lista.InserirComoUltimo(3)

lista.MostrarTudo()
