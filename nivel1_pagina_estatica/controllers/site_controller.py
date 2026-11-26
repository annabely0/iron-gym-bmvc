from bottle import template, static_file


class SiteController:
    """Controller da página estática do site."""

    HORARIOS = [
        ('Segunda a sexta', '05:30 - 23:00'),
        ('Sábado', '08:00 - 18:00'),
        ('Domingo e feriados', '09:00 - 13:00'),
    ]

    def __init__(self, app, catalogo, pasta_static):
        self.catalogo = catalogo
        self.pasta_static = pasta_static
        app.route('/', method='GET', callback=self.index)
        app.route('/static/<caminho:path>', method='GET', callback=self.arquivos_estaticos)

    def index(self):
        return template('index',
                        academia='Iron Gym',
                        planos=self.catalogo.listar(),
                        horarios=self.HORARIOS)

    def arquivos_estaticos(self, caminho):
        return static_file(caminho, root=self.pasta_static)
