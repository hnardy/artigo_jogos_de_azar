# Classe que representa a "banca" ou "casa" do jogo, que recebe apostas e paga prêmios.
# Mantém históricos de saldo e pagamentos realizados.

class Casa:
    valorApostasRecebidas = []   # Histórico de valores recebidos em apostas (não está sendo usado)
    valorPremiosPagos = []       # Histórico de prêmios pagos
    historicoDeSaldos = []       # Histórico de saldos da casa após cada pagamento

    def __init__(self, saldoIncial=0):
        """
        Inicializa a casa com um saldo inicial.

        Args:
            saldoIncial (int): saldo inicial da casa (padrão 0)
        """
        self.saldo = saldoIncial
        self.historicoDeSaldos.append(saldoIncial)

    def receberApostas(self, apostas):
        """
        Adiciona o valor das apostas recebidas ao saldo da casa.

        Args:
            apostas (int): valor total das apostas recebidas
        """
        self.saldo += apostas
        # valorApostasRecebidas poderia ser atualizado aqui se desejado
        # self.valorApostasRecebidas.append(apostas)

    def pagarPremio(self, premio):
        """
        Subtrai o valor do prêmio pago do saldo da casa e registra nos históricos.

        Args:
            premio (int): valor do prêmio a ser pago
        """
        self.saldo -= premio
        self.valorPremiosPagos.append(premio)
        self.historicoDeSaldos.append(self.saldo)

    def getSaldo(self):
        """
        Retorna o saldo atual da casa.

        Returns:
            int: saldo atual
        """
        return self.saldo

    def getPremiosPagos(self):
        """
        Retorna a lista de prêmios pagos até o momento.

        Returns:
            list[int]: prêmios pagos
        """
        return self.valorPremiosPagos
