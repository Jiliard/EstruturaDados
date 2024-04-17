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

    def __init__(self):
        self.__prim = None
        self.__ult = None
        self.__cursor = N
      
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

    def __Vazio(self) -> bool:
        if self.__prim == None:
            return True
        return False
    
    #feito
    def InserirComoPrimeiro(self, el):
        novo = objeto(el)

        if self.__prim == None:
            self.__ult = novo
            self.__cursor = novo

        else:
            novo.setprox(self.__prim)

        self.__prim = novo

    #feito
    def InserirComoUltimo(self, el):
        novo = objeto(el)

        if self.__ult == None:
            self.__prim = novo
            self.__cursor = novo

        else:
            self.__ult.setprox(novo)

        self.__ult = novo

    #feito    
    def InserirNaPosicao(self, el, pos):
        novo = objeto(el)

        iterador = self.__prim
        atual = 2

        while atual < pos:
            iterador = iterador.getprox()
            atual +=1

        novo.setprox(iterador.getprox()) 
        iterador.setprox(novo)

    #feito
    def InserirAntesDe(self, el, ref):
        novo = objeto(el)
        iterador = self.__prim

        while iterador.getprox().getdado().getdado() != ref:
            iterador = iterador.getprox()

        novo.setprox(iterador.getprox()) 
        iterador.setprox(novo)

    #feito
    def InserirDepoisDe(self, el, ref):
        novo = objeto(el)
        iterador = self.__prim

        while iterador.getdado().getdado() != ref:
            iterador = iterador.getprox()

        novo.setprox(iterador.getprox()) 
        iterador.setprox(novo)

    #feito
    def RemoverPrimeiro(self):
        if self.__Vazio():
            print("EXCEÇÃO")

        else:
            self.__prim = self.__prim.getprox()
            self.__prim.setAnt(None)

    #feito
    def RemoverUltimo(self):
        if self.__Vazio():
            print("Exceção")
        else:
            self.__ult = self.__ult.getAnter()
            self.__ult.setProx(None)

    #feito
    def AcessaPrimeiro(self):
        return self.__prim.getdado()
    
    #feito
    def AcessaUltimo(self):
        return self.__ult.getdado()
    
    #feito
    def MostrarTudo(self):
        iterador = self.__prim

        while True:
            print(iterador.getdado())
            if iterador.getprox() == None: break
            iterador = iterador.getprox()

lista = lista()

lista.InserirComoUltimo(1)

lista.InserirComoUltimo(2)

lista.InserirComoUltimo(3)

lista.MostrarTudo()

