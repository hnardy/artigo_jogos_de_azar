from random import randint

class apostadorPadrao:
    
    historicoGanhos = []
    historicoApostas =[]
    historicoSaldos = []

    saldo = 0

    def __init__(self, saldo = 10):  
        self.saldoInicial =saldo
        self.saldo = saldo
        
  


    def receberPremio(self,premio):
        self.saldo += premio
        self.historicoGanhos.append(premio)



    def apostaCega(self):

        self.historicoSaldos.append(self.saldo)
        montanteAposta = randint(0,int(self.saldo))

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




    
    def exbirHistorico(self):
        print(f"apostas: {self.historicoApostas}")            
        print(f"ganhos: {self.historicoGanhos}")
        print(f"saldos:{self.historicoSaldos}")
        print(f"saldo Atual: {self.saldo}")
