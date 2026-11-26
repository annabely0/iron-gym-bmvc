import os
from bottle import Bottle, run, TEMPLATE_PATH

from models.aluno_dao import AlunoDAO
from controllers.site_controller import SiteController
from controllers.aluno_controller import AlunoController

BASE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH.insert(0, os.path.join(BASE, 'views'))

app = Bottle()
dao = AlunoDAO(os.path.join(BASE, 'data', 'alunos.json'))

SiteController(app, dao, os.path.join(BASE, 'static'))
AlunoController(app, dao)

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)
