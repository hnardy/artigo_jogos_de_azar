from random import randint

# A classe Roleta escolhe aleatoriamente um número e retorna seu prêmio correspondente.

# Listas de prêmios e suas respectivas casas
x1 = (1, 4, 7, 9, 11, 13, 15, 19, 21, 23, 25, 29, 31, 34, 37, 39, 41, 43, 46, 50, 53)
x2 = (2, 5, 10, 14, 17, 20, 27, 32, 35, 44, 47, 49, 52)
x5 = (3, 8, 22, 26, 33, 40, 45)
x10 = (16, 28, 38, 51)
azul = (12, 24, 36, 48)
rosa = (6, 30)
verde = (18, 42)
vermelho = (54,)




class Roleta:
    def __init__(self):
        """Inicializa a roleta."""
        self.historicoPremios = []  # Histórico de todos os prêmios sorteados
        

    def girar(self):
        """
        Sorteia um número aleatório de 1 a 54 e identifica seu prêmio.
        
        Returns:
            tuple: (nome do prêmio, número sorteado)
        """
        sorteado = randint(1, 54)
        premio = self.identificarCasa(sorteado)
        return premio, sorteado

    def identificarCasa(self, num):
        """
        Identifica qual é o prêmio correspondente ao número sorteado.
        Também atualiza o histórico de prêmios.

        Args:
            num (int): número sorteado pela roleta

        Returns:
            str: nome do prêmio correspondente
        """
        if num in x1:
            self.historicoPremios.append("1")
            return "multiplicar por 1"
        
        elif num in x2:
            self.historicoPremios.append("2")
            return "multiplicar por 2"
        
        elif num in x5:
            self.historicoPremios.append("5")
            return "multiplicar por 5"
        
        elif num in x10:
            self.historicoPremios.append("10")
            return "multiplicar por 10"
        
        elif num in azul:
            self.historicoPremios.append("azul")
            return "prêmio azul"
        
        elif num in rosa:
            self.historicoPremios.append("rosa")
            return "prêmio rosa"
        
        elif num in verde:
            self.historicoPremios.append("verde")
            return "prêmio verde"
        
        elif num in vermelho:
            self.historicoPremios.append("vermelho")
            return "prêmio vermelho"
        
        else:
            return "erro"

    
