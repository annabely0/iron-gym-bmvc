class Aluno:
    """Modelo de aluno da academia."""

    PLANOS = ['Mensal', 'Trimestral', 'Anual']
    MODALIDADES = ['Musculação', 'Funcional', 'Spinning', 'Yoga', 'Crossfit']

    def __init__(self, id=None, nome='', email='', plano='Mensal',
                 modalidade='Musculação', data_inicio='', ativo=True,
                 presente=False, hora_checkin=''):
        self.id = id
        self.nome = nome
        self.email = email
        self.plano = plano
        self.modalidade = modalidade
        self.data_inicio = data_inicio
        self.ativo = ativo
        self.presente = presente
        self.hora_checkin = hora_checkin

    def validar(self):
        """Devolve uma lista de mensagens de erro (vazia se estiver tudo certo)."""
        erros = []
        if len(self.nome.strip()) < 3:
            erros.append('O nome deve ter ao menos 3 caracteres.')
        if '@' not in self.email:
            erros.append('Informe um e-mail válido.')
        if self.plano not in self.PLANOS:
            erros.append('Plano inválido.')
        if self.modalidade not in self.MODALIDADES:
            erros.append('Modalidade inválida.')
        return erros

    def to_dict(self):
        return dict(vars(self))

    @classmethod
    def from_dict(cls, dados):
        return cls(**dados)
