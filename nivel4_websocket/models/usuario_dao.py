import json
import os

from models.usuario import Usuario


class UsuarioDAO:
    """Persistência dos usuários em JSON."""

    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.usuarios = []
        self._carregar()

    def _carregar(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, encoding='utf-8') as f:
                self.usuarios = [Usuario.from_dict(d) for d in json.load(f)]

    def _salvar(self):
        os.makedirs(os.path.dirname(self.arquivo), exist_ok=True)
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            json.dump([u.to_dict() for u in self.usuarios], f, ensure_ascii=False, indent=2)

    def criar(self, usuario):
        ids = [u.id for u in self.usuarios]
        usuario.id = max(ids) + 1 if ids else 1
        self.usuarios.append(usuario)
        self._salvar()
        return usuario

    def buscar_por_id(self, id):
        for usuario in self.usuarios:
            if usuario.id == id:
                return usuario
        return None

    def buscar_por_login(self, login):
        for usuario in self.usuarios:
            if usuario.login == login:
                return usuario
        return None

    def vazio(self):
        return len(self.usuarios) == 0
