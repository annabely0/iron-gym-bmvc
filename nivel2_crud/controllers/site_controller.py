from bottle import template, static_file


class SiteController:
    """Página inicial e arquivos estáticos."""

    def __init__(self, app, dao, pasta_static):
        self.dao = dao
        self.pasta_static = pasta_static
        app.route('/', method='GET', callback=self.index)
        app.route('/static/<caminho:path>', method='GET', callback=self.arquivos_estaticos)

    def index(self):
        alunos = self.dao.listar()
        ativos = [a for a in alunos if a.ativo]
        return template('index', total=len(alunos), ativos=len(ativos))

    def arquivos_estaticos(self, caminho):
        return static_file(caminho, root=self.pasta_static)
