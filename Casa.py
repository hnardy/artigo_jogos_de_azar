# Classe que representa a "banca" ou "casa" do jogo, que recebe apostas e paga prêmios.
# Mantém históricos de saldo e pagamentos realizados.

class Casa:
    def __init__(self, saldoIncial=0):
        """
        Inicializa a casa com um saldo inicial.

        Args:
            saldoIncial (int): saldo inicial da casa (padrão 0)
        """
        self.saldo = saldoIncial
        self.valorApostasRecebidas = []         # Histórico de valores recebidos em apostas
        self.valorPremiosPagos = []             # Histórico de prêmios pagos por rodada
        self.historicoDeSaldos = [saldoIncial]  # Histórico do saldo da casa após cada pagamento

    def receberApostas(self, apostas):
        """
        Adiciona o valor das apostas recebidas ao saldo da casa.

        Args:
            apostas (int): valor total das apostas recebidas
        """
        self.saldo += apostas
        self.valorApostasRecebidas.append(apostas)
        # O saldo ainda não é registrado no histórico aqui, pois o pagamento ainda não ocorreu

    def pagarPremio(self, premio):
        """
        Subtrai o valor do prêmio pago do saldo da casa.

        Args:
            premio (int): valor do prêmio a ser pago
        """
        self.saldo -= premio
        # Esta função é chamada várias vezes por rodada, então não registra o saldo aqui
        # O registro de saldo total pago por rodada ocorrerá em deduzirPremio

    def deduzirPremio(self, pot):
        """
        Após pagar todos os jogadores da rodada, registra o valor total pago (pot)
        e atualiza o histórico de saldos da casa.

        Args:
            pot (int): valor total dos prêmios pagos na rodada
        """
        self.valorPremiosPagos.append(pot)
        self.historicoDeSaldos.append(self.saldo) 


    def saldoFinal(self):
        
        self.historicoDeSaldos.append(self.saldo)
