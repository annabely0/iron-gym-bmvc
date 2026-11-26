import os
from bottle import Bottle, BaseTemplate, TEMPLATE_PATH

from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

from models.aluno_dao import AlunoDAO
from models.usuario import Usuario
from models.usuario_dao import UsuarioDAO
from services.auth_service import AuthService
from services.ws_hub import PresencaHub
from controllers.site_controller import SiteController
from controllers.auth_controller import AuthController
from controllers.aluno_controller import AlunoController
from controllers.aovivo_controller import AoVivoController

BASE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH.insert(0, os.path.join(BASE, 'views'))

# Troque o segredo em produção: export IRONGYM_SEGREDO="uma-frase-longa-e-aleatoria"
SEGREDO = os.environ.get('IRONGYM_SEGREDO', 'troque-este-segredo-em-producao')
CAPACIDADE = 30

app = Bottle()
aluno_dao = AlunoDAO(os.path.join(BASE, 'data', 'alunos.json'))
usuario_dao = UsuarioDAO(os.path.join(BASE, 'data', 'usuarios.json'))

if usuario_dao.vazio():
    usuario_dao.criar(Usuario.novo('admin', 'Administrador', 'admin123'))

auth = AuthService(usuario_dao, SEGREDO)
hub = PresencaHub(aluno_dao, CAPACIDADE)
BaseTemplate.defaults['usuario_logado'] = auth.usuario_logado

SiteController(app, auth, hub, os.path.join(BASE, 'static'))
AuthController(app, auth)
AlunoController(app, aluno_dao, auth, hub)
AoVivoController(app, aluno_dao, auth, hub)

if __name__ == '__main__':
    print('Iron Gym em http://localhost:8080')
    servidor = WSGIServer(('localhost', 8080), app, handler_class=WebSocketHandler)
    servidor.serve_forever()
