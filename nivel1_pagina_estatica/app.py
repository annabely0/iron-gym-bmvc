import os
from bottle import Bottle, run, TEMPLATE_PATH

from models.plano import CatalogoPlanos
from controllers.site_controller import SiteController

BASE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH.insert(0, os.path.join(BASE, 'views'))

app = Bottle()
SiteController(app, CatalogoPlanos(), os.path.join(BASE, 'static'))

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)
