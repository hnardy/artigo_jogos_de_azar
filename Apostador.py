from random import randint

class apostadorPadrao:
    historicoGanhos = []
    historicoApostas =[]
    saldo = 0

    def __init__(self, saldo = 1000, percentualApostado = 20):  
        self.saldoInicial =saldo
        self.saldo = saldo
        self.percentualApostado = percentualApostado
  


    def receberPremio(self,premio):
        self.saldo += premio
        self.historicoGanhos.append(premio)

    def apostaCega(self):
        montanteAposta = int( self.saldo * self.percentualApostado/100)
        self.saldo -= montanteAposta

        x1 = montanteAposta/8
        x2 = montanteAposta/8
        x5 = montanteAposta/8
        x10 = montanteAposta/8
        azul = montanteAposta/8
        rosa = montanteAposta/8
        verde = montanteAposta/8
        vermelho = montanteAposta/8
        self.historicoApostas.append([x1,x2,x5,x10,azul,rosa,verde,vermelho])

        return x1,x2,x5,x10,azul,rosa,verde,vermelho
    
    def exbirHistorico(self):
        print(f"apostas: {self.historicoApostas}")            
        print(f"ganhos: {self.historicoGanhos}")
        print(f"saldo: {self.saldo}")