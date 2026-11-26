import os
from bottle import Bottle, run, BaseTemplate, TEMPLATE_PATH

from models.aluno_dao import AlunoDAO
from models.usuario import Usuario
from models.usuario_dao import UsuarioDAO
from services.auth_service import AuthService
from controllers.site_controller import SiteController
from controllers.auth_controller import AuthController
from controllers.aluno_controller import AlunoController

BASE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH.insert(0, os.path.join(BASE, 'views'))

# Troque o segredo em produção: export IRONGYM_SEGREDO="uma-frase-longa-e-aleatoria"
SEGREDO = os.environ.get('IRONGYM_SEGREDO', 'troque-este-segredo-em-producao')

app = Bottle()
aluno_dao = AlunoDAO(os.path.join(BASE, 'data', 'alunos.json'))
usuario_dao = UsuarioDAO(os.path.join(BASE, 'data', 'usuarios.json'))

# Usuário inicial (apenas na primeira execução)
if usuario_dao.vazio():
    usuario_dao.criar(Usuario.novo('admin', 'Administrador', 'admin123'))

auth = AuthService(usuario_dao, SEGREDO)

# Disponível em todos os templates: usuario_logado()
BaseTemplate.defaults['usuario_logado'] = auth.usuario_logado

SiteController(app, aluno_dao, auth, os.path.join(BASE, 'static'))
AuthController(app, auth)
AlunoController(app, aluno_dao, auth)

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)
