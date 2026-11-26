from bottle import template, static_file


class SiteController:
    """Página pública, painel restrito e arquivos estáticos."""

    def __init__(self, app, dao, auth, pasta_static):
        self.dao = dao
        self.auth = auth
        self.pasta_static = pasta_static
        app.route('/', method='GET', callback=self.index)
        app.route('/painel', method='GET', callback=auth.proteger(self.painel))
        app.route('/static/<caminho:path>', method='GET', callback=self.arquivos_estaticos)

    def index(self):
        return template('index')

    def painel(self):
        alunos = self.dao.listar()
        ativos = [a for a in alunos if a.ativo]
        usuario = self.auth.usuario_logado()
        return template('painel', usuario=usuario, total=len(alunos), ativos=len(ativos))

    def arquivos_estaticos(self, caminho):
        return static_file(caminho, root=self.pasta_static)
