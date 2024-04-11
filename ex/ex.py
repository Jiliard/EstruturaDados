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
    
    def InserirComoPrimeiro(self, el):
        novo = objeto(el)

        if self.__cont == 0:
            self.__ult = novo

        else:
            novo.setprox(self.__prim)

        self.__prim = novo
        self.__cont += 1

    def InserirComoUltimo(self, el):
        novo = objeto(el)

        if self.__cont == 0:
            self.__prim = novo

        else:
            self.__ult.setprox(novo)

        self.__ult = novo
        self.__cont += 1
    
    def InserirNaPosicao(self, el, pos):
        novo = objeto(el)

        iterador = self.__prim
        atual = 2

        while atual < pos:
            iterador = iterador.getprox
            atual +=1

        novo.setprox(iterador.getprox()) 
        iterador.setprox(novo)

    def InserirAntesDe(self, el, ref):
        novo = objeto(el)

    def InserirDepoisDe(self, el, ref):
        novo = objeto(el)

    def RemoverPrimeiro(self):
        if self.__cont == 0:
            print("EXCEÇÃO")

        else:
            aux = self.__prim.getprox()
            self.__prim = aux
            self.__cont -= 1
    
    def RemoverUltimo(self):
        if self.__cont == 0:
            print("EXCEÇÃO")

        else:
            aux = self.__prim.getprox()
            self.__prim = aux
            self.__cont -= 1


    def AcessaPrimeiro(self):
        return self.__prim

    def AcessaUltimo(self):
        return self.__ult

    def MostrarTudo(self):
        iterador = self.__prim
        atual = 1

        while atual <= self.__ult.getdado().getdado() :
            print(iterador.getdado().getdado())
            iterador = iterador.getprox
            atual +=1

p1 = objeto(1)
p2 = objeto(2)
p3 = objeto(3)
p4 = objeto(4)

lista = lista()

lista.InserirComoPrimeiro(p1)

lista.InserirComoPrimeiro(p2)

lista.InserirComoPrimeiro(p3)

lista.RemoverPrimeiro()

lista.MostrarTudo()
