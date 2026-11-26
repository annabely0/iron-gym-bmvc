import json
from urllib.parse import urlparse

from bottle import request, response, template, abort


class AoVivoController:
    """Página em tempo real, check-in/out e endpoint WebSocket."""

    def __init__(self, app, dao, auth, hub):
        self.dao = dao
        self.auth = auth
        self.hub = hub
        app.route('/ao-vivo', method='GET', callback=auth.proteger(self.pagina))
        app.route('/alunos/<id:int>/checkin', method='POST', callback=auth.proteger(self.checkin))
        app.route('/ws', method='GET', callback=self.websocket)

    def pagina(self):
        ativos = [a for a in self.dao.listar() if a.ativo]
        return template('ao_vivo', alunos=ativos, estado=self.hub.estado())

    def _json(self, dados, status=200):
        response.content_type = 'application/json'
        response.status = status
        return json.dumps(dados, ensure_ascii=False)

    def checkin(self, id):
        aluno = self.dao.buscar(id)
        if aluno is None:
            return self._json({'erro': 'Aluno não encontrado.'}, 404)
        if not aluno.presente:
            if not aluno.ativo:
                return self._json({'erro': 'Matrícula inativa.'}, 400)
            if len(self.dao.presentes()) >= self.hub.capacidade:
                return self._json({'erro': 'Academia lotada no momento.'}, 409)
        self.dao.alternar_presenca(id)
        self.hub.transmitir()
        return self._json({'ok': True, 'presente': aluno.presente})

    def websocket(self):
        if self.auth.usuario_logado() is None:
            abort(401, 'Faça login para acompanhar em tempo real.')
        origem = request.headers.get('Origin', '')
        if origem and urlparse(origem).netloc != request.headers.get('Host'):
            abort(403, 'Origem não permitida.')
        socket = request.environ.get('wsgi.websocket')
        if socket is None:
            abort(400, 'Esperava uma conexão WebSocket.')
        self.hub.conectar(socket)
        try:
            while True:
                mensagem = socket.receive()
                if mensagem is None:
                    break
        finally:
            self.hub.desconectar(socket)
        return ''
