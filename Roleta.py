from random import randint

# listas de prêmios e suas respectivas casas
x1 = (1, 4, 7, 9, 11, 13, 15, 19, 21, 23, 25, 29, 31, 34, 37, 39, 41, 43, 46, 50, 53)
x2 = (2, 5, 10, 14, 17, 20, 27, 32, 35, 44, 47, 49, 52)
x5 = (3, 8, 22, 26, 33, 40, 45)
x10 = (16, 28, 38, 51)
azul = (12, 24, 36, 48)
rosa = (6, 30)
verde = (18, 42)
vermelho = (54,)
historicoPremios = []

class Roleta:
    def __init__(self):  
        pass

    def girar(self):
        sorteado = randint(1, 54)
        premio = self.identificarCasa(sorteado)
        return premio,sorteado

    def premioAzul(self):
        return "prêmio azul"

    def premioRosa(self):
        return "prêmio rosa"

    def premioVerde(self):
        return "prêmio verde"

    def premioVermelho(self):
        return "prêmio vermelho"

    def premioMultiplicar(self, fator):
        return f"multiplicar por {fator}"


    def identificarCasa(self, num): 
        if num in x1:
            return self.premioMultiplicar(1)
        elif num in x2:
            return self.premioMultiplicar(2)
        elif num in x5:
            return self.premioMultiplicar(5)
        elif num in x10:
            return self.premioMultiplicar(10)
        elif num in azul:
            return self.premioAzul()
        elif num in rosa:
            return self.premioRosa()
        elif num in verde:
            return self.premioVerde()
        elif num in vermelho:
            return self.premioVermelho()
        else:
            return "erro"
