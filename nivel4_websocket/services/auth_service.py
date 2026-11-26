from functools import wraps

from bottle import request, response, redirect


class AuthService:
    """Controle de sessão (cookie assinado) e proteção de rotas."""

    COOKIE = 'sessao_iron_gym'

    def __init__(self, usuario_dao, segredo):
        self.usuario_dao = usuario_dao
        self.segredo = segredo

    def autenticar(self, login, senha):
        usuario = self.usuario_dao.buscar_por_login(login)
        if usuario is not None and usuario.conferir_senha(senha):
            return usuario
        return None

    def iniciar_sessao(self, usuario):
        response.set_cookie(self.COOKIE, str(usuario.id), secret=self.segredo,
                            path='/', httponly=True, samesite='Lax')

    def encerrar_sessao(self):
        response.delete_cookie(self.COOKIE, path='/')

    def usuario_logado(self):
        valor = request.get_cookie(self.COOKIE, secret=self.segredo)
        if not valor:
            return None
        try:
            return self.usuario_dao.buscar_por_id(int(valor))
        except (TypeError, ValueError):
            return None

    def proteger(self, funcao):
        """Envolve um callback: só executa se houver usuário logado."""
        @wraps(funcao)
        def interno(*args, **kwargs):
            if self.usuario_logado() is None:
                redirect('/login?proximo=' + request.path)
            return funcao(*args, **kwargs)
        return interno
