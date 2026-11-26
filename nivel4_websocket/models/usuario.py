import hashlib
import hmac
import os


class Usuario:
    """Usuário do sistema (funcionário da academia)."""

    ITERACOES = 100000

    def __init__(self, id=None, login='', nome='', senha_hash='', salt=''):
        self.id = id
        self.login = login
        self.nome = nome
        self.senha_hash = senha_hash
        self.salt = salt

    @classmethod
    def novo(cls, login, nome, senha):
        usuario = cls(login=login, nome=nome)
        usuario.definir_senha(senha)
        return usuario

    @classmethod
    def _calcular_hash(cls, senha, salt_hex):
        resultado = hashlib.pbkdf2_hmac('sha256', senha.encode('utf-8'),
                                        bytes.fromhex(salt_hex), cls.ITERACOES)
        return resultado.hex()

    def definir_senha(self, senha):
        self.salt = os.urandom(16).hex()
        self.senha_hash = self._calcular_hash(senha, self.salt)

    def conferir_senha(self, senha):
        tentativa = self._calcular_hash(senha, self.salt)
        return hmac.compare_digest(tentativa, self.senha_hash)

    def to_dict(self):
        return dict(vars(self))

    @classmethod
    def from_dict(cls, dados):
        return cls(**dados)
