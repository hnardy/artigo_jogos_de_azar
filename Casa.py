

class Casa:
    valorApostasRecebidas = []
    valorPremiosPagos = []
    historicoDeSaldos = []
    
    def __init__(self, saldoIncial = 0):
        self.saldo = saldoIncial
        self.historicoDeSaldos.append(saldoIncial)
        pass

    
    def receberApostas(self,apostas):
        self.saldo += apostas
        return
    
    def pagarPremio(self,premio):
        self.saldo -= premio
        self.valorPremiosPagos.append(premio)
        self.historicoDeSaldos.append(self.saldo)
        return
    
    def getSaldo(self):
        return self.saldo
    
    def getPremiosPagos(self):
        return self.valorPremiosPagos
