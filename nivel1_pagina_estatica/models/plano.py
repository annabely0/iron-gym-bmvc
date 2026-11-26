class Plano:
    """Plano de assinatura da academia."""

    def __init__(self, nome, preco, beneficios, destaque=False):
        self.nome = nome
        self.preco = preco
        self.beneficios = beneficios
        self.destaque = destaque

    def preco_formatado(self):
        return 'R$ {:.2f}'.format(self.preco).replace('.', ',')


class CatalogoPlanos:
    """Fonte de dados (em memória) dos planos exibidos na página."""

    def listar(self):
        return [
            Plano('Mensal', 129.90, ['Musculação livre', 'Vestiário com armários']),
            Plano('Trimestral', 109.90,
                  ['Musculação livre', 'Aulas coletivas', 'Avaliação física'], True),
            Plano('Anual', 89.90,
                  ['Tudo do trimestral', 'Treino personalizado', '2 convidados/mês']),
        ]
