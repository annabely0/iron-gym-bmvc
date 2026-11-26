import json
import os
from datetime import datetime

from models.aluno import Aluno


class AlunoDAO:
    """Persistência dos alunos em um arquivo JSON."""

    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.alunos = []
        self._carregar()

    def _carregar(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, encoding='utf-8') as f:
                self.alunos = [Aluno.from_dict(d) for d in json.load(f)]

    def _salvar(self):
        os.makedirs(os.path.dirname(self.arquivo), exist_ok=True)
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            json.dump([a.to_dict() for a in self.alunos], f, ensure_ascii=False, indent=2)

    def _proximo_id(self):
        ids = [a.id for a in self.alunos]
        return max(ids) + 1 if ids else 1

    # CREATE
    def criar(self, aluno):
        aluno.id = self._proximo_id()
        self.alunos.append(aluno)
        self._salvar()
        return aluno

    # READ
    def listar(self):
        return list(self.alunos)

    def buscar(self, id):
        for aluno in self.alunos:
            if aluno.id == id:
                return aluno
        return None

    # UPDATE
    def atualizar(self, aluno):
        for posicao, existente in enumerate(self.alunos):
            if existente.id == aluno.id:
                self.alunos[posicao] = aluno
                self._salvar()
                return True
        return False

    # DELETE
    def remover(self, id):
        aluno = self.buscar(id)
        if aluno is None:
            return False
        self.alunos.remove(aluno)
        self._salvar()
        return True

    # Presença (check-in / check-out)
    def presentes(self):
        return [a for a in self.alunos if a.presente]

    def alternar_presenca(self, id):
        aluno = self.buscar(id)
        if aluno is None:
            return None
        aluno.presente = not aluno.presente
        aluno.hora_checkin = datetime.now().strftime('%H:%M') if aluno.presente else ''
        self._salvar()
        return aluno
