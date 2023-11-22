from grafite import Grafite


class Lapiseira:

    def __init__(self, calibre:float):
        self.calibre = calibre
        self.grafite_contador = 0
        self.grafite_escrever = None
        self.folhas_escritas = 0
        self.gasto_do_grafite = 0


    def inserir (self, grafite: Grafite):
        if grafite.calibre == self.calibre and self.grafite_contador == 0:
            self.grafite_contador += 1
            self.grafite_escrever = grafite
            return True
        else:
            return False


    def remover(self):
        if self.grafite_contador == 1:
            self.grafite_contador -= 1
            self.grafite_escrever = None
            self.folhas_escritas = 0
            return True
        else:
            return False


    def escrever(self, folhas: int):
        if self.grafite_contador == 1:
            self.paginas_por_grafite = self.grafite_escrever.tamanho / self.grafite_escrever.dureza.value
            if self.paginas_por_grafite > folhas:
                self.folhas_escritas += folhas
                self.gasto_do_grafite += folhas
                self.paginas_por_grafite -= folhas
                self.grafite_escrever.tamanho -= self.grafite_escrever.dureza.value * folhas
                return True
            elif self.paginas_por_grafite < folhas:
                diferenca = folhas - self.paginas_por_grafite
                self.folhas_escritas += folhas - diferenca
                self.grafite_contador = 0
                self.grafite_escrever = None
                self.paginas_por_grafite -= folhas
                return False
            else:
                self.grafite_contador = 0
                self.grafite_escrever = None
                self.folhas_escritas = folhas
                self.paginas_por_grafite -= folhas
                return True
        else:
            return False


    def getGrafite(self):
        if self.grafite_contador == 1:
            return self.grafite_escrever
        else:
            return None


    def getCalibre(self):
        return self.calibre


    def getFolhasEscritas(self):
        return self.folhas_escritas
