

# padrão de aposta 
# x1, x2, x5, x10, azul, rosa, verde, vermelho

class Apostas:
    def __init__(self):  
        pass


    def aposta(self, x1, x2, x5, x10, azul, rosa, verde, vermelho,sorteado):
    
        if sorteado == ("multiplicar por 1"):
            premio = x1 + x1*1
            return premio
    
        elif sorteado == ("multiplicar por 2"):
            premio = x2 + x2*2
            return premio
        
        elif sorteado == ("multiplicar por 5"):
            premio = x5 + x5*5
            return premio

        elif sorteado == ("multiplicar por 10"):
            premio = x10 + x10*10
            return premio
        
        elif sorteado == ("prêmio azul"):
            premio = azul + azul*9
            return premio
        
        elif sorteado == ("prêmio rosa"):
            premio = rosa + rosa*20
            return premio
        
        elif sorteado == ("prêmio verde"):
            premio = verde + verde*20
            return premio
        
        elif sorteado == ("prêmio vermelho"):
            premio = vermelho + vermelho*100
            return premio