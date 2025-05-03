from random import randint



#saldo do jogador
#o jogador está ativo?
# esquema de aposta [x1 x2 x5 x10 azul rosa verde vermelho]



class ApostadorPadrao:
    
    historicoGanhos = []
    historicoApostas =[]
    historicoSaldos = []
    tipo = "padrão"


    def __init__(self, saldo = 100000):  
        self.saldoInicial =saldo
        self.saldo = saldo
        

    def estaAtivo(self):
        if self.saldo > 0:
            return True
        else:
            return False 



    def receberPremio(self,premio):
        self.saldo += premio
        self.historicoGanhos.append(premio)



    def apostar(self):

        self.historicoSaldos.append(self.saldo)
        
        montanteAposta = randint(1,int(self.saldo))


        # Se não houver saldo suficiente para dividir entre 8 categorias, aposta tudo em x1
        if montanteAposta < 8 and montanteAposta >= 1:
            x1 = montanteAposta
            x2 = x5 = x10 = azul = rosa = verde = vermelho = 0
            self.saldo -= montanteAposta

        elif montanteAposta >= 8:
            aposta_unitaria = montanteAposta // 8
            x1 = x2 = x5 = x10 = azul = rosa = verde = vermelho = aposta_unitaria
            total_apostado = aposta_unitaria * 8
            self.saldo -= total_apostado
        
        else:
            # Se nem 1 pode ser apostado, aposta tudo como 0
            x1 = x2 = x5 = x10 = azul = rosa = verde = vermelho = 0


        self.historicoApostas.append([x1, x2, x5, x10, azul, rosa, verde, vermelho])
        

        return x1, x2, x5, x10, azul, rosa, verde, vermelho


    def rodadasAteFalha(self):
        a = len(self.historicoApostas)
        return a
    

