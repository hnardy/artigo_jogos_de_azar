from random import randint

# a classe roleta escolhe um número e dita seu premio, apenas 


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


    def identificarCasa(self, num): 
        if num in x1:
            historicoPremios.append("1")
            return "multiplicar por 1"
        
        elif num in x2:
            historicoPremios.append("2")
            return "multiplicar por 2"
        
        elif num in x5:
            historicoPremios.append("5")
            return"multiplicar por 5"
        
        elif num in x10:
            historicoPremios.append("10")
            return "multiplicar por 10"
        
        elif num in azul:
            historicoPremios.append(f"azul")
            return "prêmio azul"
        
        elif num in rosa:
            historicoPremios.append(f"rosa")
            return "prêmio rosa"
        
        elif num in verde:
            historicoPremios.append(f"verde")
            return "prêmio verde"
        
        elif num in vermelho:
            historicoPremios.append(f"vermelho")
            return "prêmio vermelho"
        
        else:
            return "erro"
        





    def getHistorico(self):
        return historicoPremios