from bottle import request, redirect, template


class AuthController:
    """Login e logout."""

    def __init__(self, app, auth):
        self.auth = auth
        app.route('/login', method='GET', callback=self.formulario)
        app.route('/login', method='POST', callback=self.entrar)
        app.route('/logout', method='POST', callback=self.sair)

    @staticmethod
    def _destino_seguro(destino):
        # evita open redirect: só aceita caminhos internos
        if destino.startswith('/') and not destino.startswith('//'):
            return destino
        return '/painel'

    def formulario(self):
        if self.auth.usuario_logado() is not None:
            redirect('/painel')
        return template('login', erro='', proximo=request.query.get('proximo', ''))

    def entrar(self):
        login = request.forms.getunicode('login', '').strip()
        senha = request.forms.getunicode('senha', '')
        proximo = request.forms.getunicode('proximo', '')
        usuario = self.auth.autenticar(login, senha)
        if usuario is None:
            return template('login', erro='Login ou senha incorretos.', proximo=proximo)
        self.auth.iniciar_sessao(usuario)
        redirect(self._destino_seguro(proximo))

    def sair(self):
        self.auth.encerrar_sessao()
        redirect('/')
