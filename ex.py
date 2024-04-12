class objeto():

    def __init__(self, dado):
        self.__dado = dado
        self.__prox = None
    
    def getdado(self):
        return self.__dado

    def setdado(self, dado):
        self.__dado = dado
    
    def getprox(self):
        return self.__prox

    def setprox(self, prox):
        self.__prox = prox


class lista():

    def __init__(self):
        self.__prim = None
        self.__ult = None
        self.__cont = 0
    
    #feito
    def InserirComoPrimeiro(self, el):
        novo = objeto(el)

        if self.__cont == 0:
            self.__ult = novo

        else:
            novo.setprox(self.__prim)

        self.__prim = novo
        self.__cont += 1

    #feito
    def InserirComoUltimo(self, el):
        novo = objeto(el)

        if self.__cont == 0:
            self.__prim = novo

        else:
            self.__ult.setprox(novo)

        self.__ult = novo
        self.__cont += 1

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
        self.__cont += 1

    #feito
    def InserirAntesDe(self, el, ref):
        novo = objeto(el)
        iterador = self.__prim

        while iterador.getprox().getdado().getdado() != ref:
            iterador = iterador.getprox()

        novo.setprox(iterador.getprox()) 
        iterador.setprox(novo)
        self.__cont += 1

    #feito
    def InserirDepoisDe(self, el, ref):
        novo = objeto(el)
        iterador = self.__prim

        while iterador.getdado().getdado() != ref:
            iterador = iterador.getprox()

        novo.setprox(iterador.getprox()) 
        iterador.setprox(novo)
        self.__cont += 1

    #feito
    def RemoverPrimeiro(self):
        if self.__cont == 0:
            print("EXCEÇÃO")

        else:
            aux = self.__prim.getprox()
            self.__prim = aux
            self.__cont -= 1

    #feito
    def RemoverUltimo(self):
        iterador = self.__prim

        while iterador.getprox() != self.__ult:
            iterador = iterador.getprox()

        iterador = self.__ult
        self.__cont -= 1

    #feito
    def AcessaPrimeiro(self):
        return self.__prim.getdado().getdado()
    
    #feito
    def AcessaUltimo(self):
        return self.__ult.getdado().getdado()
    
    #feito
    def MostrarTudo(self):
        iterador = self.__prim

        while True:
            print(iterador.getdado().getdado())
            if iterador.getprox() == None: break
            iterador = iterador.getprox()

p1 = objeto(1)
p2 = objeto(2)
p3 = objeto(3)
p4 = objeto(4)
p5 = objeto(5)

lista = lista()

lista.InserirComoUltimo(p1)

lista.InserirComoUltimo(p2)

lista.InserirComoUltimo(p3)

lista.MostrarTudo()
