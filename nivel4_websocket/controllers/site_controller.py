from bottle import template, static_file


class SiteController:
    """Página pública, painel restrito e arquivos estáticos."""

    def __init__(self, app, auth, hub, pasta_static):
        self.auth = auth
        self.hub = hub
        self.pasta_static = pasta_static
        app.route('/', method='GET', callback=self.index)
        app.route('/painel', method='GET', callback=auth.proteger(self.painel))
        app.route('/static/<caminho:path>', method='GET', callback=self.arquivos_estaticos)

    def index(self):
        return template('index')

    def painel(self):
        return template('painel', usuario=self.auth.usuario_logado(), estado=self.hub.estado())

    def arquivos_estaticos(self, caminho):
        return static_file(caminho, root=self.pasta_static)
