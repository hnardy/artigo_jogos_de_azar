from random import randint

# Classe que representa um apostador com uma estratégia padrão.
# Aposta em todas as categorias igualmente, se possível.
# Mantém históricos de saldo, apostas e ganhos.

class ApostadorPadrao:
  

    def __init__(self, saldo=100):
        """
        Inicializa o jogador com um saldo definido.

        Args:
            saldo (int): saldo inicial do jogador (padrão 1000)
        """

        self.historicoGanhos =[]    # Guarda todos os prêmios recebidos
        self.historicoApostas=[]    # Guarda todas as apostas realizadas
        self.historicoSaldos =[]    # Guarda o saldo antes de cada aposta                                   
        self.saldo = saldo          #saldo variavel
        self.tipo = "padrao"

    def estaAtivo(self):
        """
        Verifica se o jogador ainda possui saldo.

        Returns:
            bool: True se o saldo for maior que 0, False caso contrário
        """
        return self.saldo > 0

    def receberPremio(self, premio):
        """
        Atualiza o saldo do jogador com o valor do prêmio recebido e registra no histórico.

        Args:
            premio (int): valor a ser adicionado ao saldo
        """
        self.saldo += premio
        self.historicoGanhos.append(premio)

    def apostar(self):
        """
        Realiza uma aposta com parte do saldo disponível, dividindo igualmente entre as categorias,
        se possível. Se o saldo for menor que 8, aposta tudo em x1.

        Returns:
            tuple: valores apostados em cada categoria
        """
        self.historicoSaldos.append(self.saldo)
        montanteAposta = randint(1, int(self.saldo))

        if 1 <= montanteAposta < 8:
            x1 = montanteAposta
            x2 = x5 = x10 = azul = rosa = verde = vermelho = 0
            self.saldo -= montanteAposta

        elif montanteAposta >= 8:
            aposta_unitaria = montanteAposta // 8
            x1 = x2 = x5 = x10 = azul = rosa = verde = vermelho = aposta_unitaria
            total_apostado = aposta_unitaria * 8
            self.saldo -= total_apostado

        else:
            # Aposta nula se o saldo não permite nem 1 de aposta
            x1 = x2 = x5 = x10 = azul = rosa = verde = vermelho = 0

        self.historicoApostas.append([x1, x2, x5, x10, azul, rosa, verde, vermelho])
        return x1, x2, x5, x10, azul, rosa, verde, vermelho

    
    def rodadasAteFalha(self):
        """
        Retorna o número de apostas realizadas, que corresponde ao número de rodadas jogadas
        até o jogador falhar (quebrar).

        Returns:
            int: número de rodadas até o jogador ficar sem saldo
        """
        return len(self.historicoApostas)

