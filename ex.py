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


class ListaDuplamenteEncadeada():

    def __init__(self, tamanho = 30):
        self.__prim = None
        self.__ult = None
        self.__cursor = None
        self.__tamanho = tamanho
        self.__quantidade = 0
      
    #feito
    def __avancarKPosicoes(self, k):
        for i in range(k):
            if self.__cursor == self.__ult:
                break

            self.__cursor = self.__cursor.getProx()

    #feito
    def __retrocederKPosicoes(self, k):
        for i in range(k):
            if self.__cursor == self.__prim:
                break

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
        novo = objeto(el)
        self.__irParaOPrimeiro()
        self.__ult.setProx(novo)

        contador = 1

        while True:
            if self.__cursor.getDado() == novo.getDado():
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
        self.__cursor = novo

    #feito
    def InserirComoUltimo(self, el):
        novo = objeto(el)

        if self.__ult == None:
            self.__prim = novo
            self.__cursor = novo

        else:
            self.__ult.setProx(novo)
            novo.setAnter(self.__ult)

        self.__ult = novo

        self.__quantidade += 1
        self.__cursor = novo

    #feito    
    def InserirNaPosicao(self, el, pos):
        self.__irParaOPrimeiro()
        self.__avancarKPosicoes(pos - 1)
        self.InserirAntesDoAtual(el)

        self.__quantidade += 1

    #feito
    def InserirAntesDoAtual(self, el):
        novo = objeto(el)

        if self.__cursor.getAnter() != None:
            self.__cursor.getAnter().setProx(novo)
            novo.setAnter(self.__cursor.getAnter())
        
        else:
            self.__prim = novo

        novo.setProx(self.__cursor)
        self.__cursor.setAnter(novo)

        self.__quantidade += 1
        self.__cursor = novo

    #feito
    def InserirDepoisDoAtual(self, el):
        novo = objeto(el)

        if self.__cursor.getProx() != None:
            self.__cursor.getProx().setAnter(novo)
            novo.setProx(self.__cursor.getProx())

        else:
            self.__ult = novo

        novo.setAnter(self.__cursor)
        self.__cursor.setProx(novo)

        self.__quantidade += 1
        self.__cursor = novo

    #feito
    def ExcluirAtual(self):
        if self.__cursor == self.__prim:
            self.ExcluirPrim()
        
        elif self.__cursor == self.__ult:
            self.ExcluirUlt()
        
        else:
            self.__cursor.getProx().setAnter(self.__cursor.getAnter())
            self.__cursor.getAnter().setProx(self.__cursor.getProx())      
            self.__avancarKPosicoes(1)

        self.__quantidade -= 1
        
    #feito
    def ExcluirPrim(self):
        if self.__Vazio():
            print("EXCEÇÃO")

        else:
            self.__prim = self.__prim.getProx()
            self.__prim.setAnter(None)

        self.__quantidade -= 1
        self.__cursor = self.__prim

    #feito
    def ExcluirUlt(self):
        if self.__Vazio():
            print("Exceção")

        else:
            self.__ult = self.__ult.getAnter()
            self.__ult.setProx(None)

        self.__quantidade -= 1
        self.__cursor = self.__ult

    #feito
    def ExcluirElemento(self, el):
        novo = objeto(el)
        self.__irParaOPrimeiro

        self.__ult.setProx(novo)

        while True:
            if self.__cursor.getDado() == novo.getDado():
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
        novo = objeto(el)

        self.__ult.setProx(novo)

        while True:
            if self.__cursor.getDado() == novo.getDado():
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

lista = ListaDuplamenteEncadeada()

lista.InserirComoPrimeiro(1)
lista.InserirComoUltimo(2)
lista.InserirAntesDoAtual(3)
lista.MostrarTudo()
#esperado = 1 3 2
print('------')

lista.InserirDepoisDoAtual(4)
lista.InserirComoPrimeiro(0)
lista.ExcluirUlt()
lista.MostrarTudo()
#esperado = 0 1 3 4 
print('------')

lista.ExcluirDaPos(2)
lista.ExcluirElemento(4)
lista.MostrarTudo()
#esperado = 0 3 
print('------')

#esperado = True 
print(lista.Buscar(0))
