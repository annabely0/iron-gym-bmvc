import json


class PresencaHub:
    """Guarda as conexões WebSocket abertas e transmite o estado da academia."""

    def __init__(self, dao, capacidade=30):
        self.dao = dao
        self.capacidade = capacidade
        self.clientes = set()

    def estado(self):
        presentes = self.dao.presentes()
        return {
            'tipo': 'estado',
            'total_alunos': len(self.dao.listar()),
            'capacidade': self.capacidade,
            'presentes': [
                {'id': a.id, 'nome': a.nome, 'modalidade': a.modalidade, 'hora': a.hora_checkin}
                for a in presentes
            ],
        }

    def conectar(self, socket):
        self.clientes.add(socket)
        socket.send(json.dumps(self.estado()))

    def desconectar(self, socket):
        self.clientes.discard(socket)

    def transmitir(self):
        texto = json.dumps(self.estado())
        mortos = []
        for cliente in list(self.clientes):
            try:
                cliente.send(texto)
            except Exception:
                mortos.append(cliente)
        for cliente in mortos:
            self.clientes.discard(cliente)
