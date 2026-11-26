from bottle import request, redirect, template, abort

from models.aluno import Aluno


class AlunoController:
    """CRUD completo de alunos."""

    MENSAGENS = {
        'criado': 'Aluno cadastrado com sucesso.',
        'atualizado': 'Aluno atualizado com sucesso.',
        'excluido': 'Aluno excluído com sucesso.',
    }

    def __init__(self, app, dao):
        self.dao = dao
        app.route('/alunos', method='GET', callback=self.listar)
        app.route('/alunos/novo', method='GET', callback=self.novo)
        app.route('/alunos', method='POST', callback=self.criar)
        app.route('/alunos/<id:int>/editar', method='GET', callback=self.editar)
        app.route('/alunos/<id:int>/editar', method='POST', callback=self.atualizar)
        app.route('/alunos/<id:int>/excluir', method='POST', callback=self.excluir)

    def _ler_formulario(self, aluno):
        forms = request.forms
        aluno.nome = forms.getunicode('nome', '').strip()
        aluno.email = forms.getunicode('email', '').strip()
        aluno.plano = forms.getunicode('plano', '')
        aluno.modalidade = forms.getunicode('modalidade', '')
        aluno.data_inicio = forms.getunicode('data_inicio', '')
        aluno.ativo = forms.getunicode('ativo') == 'on'
        return aluno

    def _form(self, aluno, acao, erros=None):
        return template('aluno_form', aluno=aluno, acao=acao, erros=erros or [],
                        planos=Aluno.PLANOS, modalidades=Aluno.MODALIDADES)

    # READ (lista)
    def listar(self):
        mensagem = self.MENSAGENS.get(request.query.get('msg', ''), '')
        return template('alunos_lista', alunos=self.dao.listar(), mensagem=mensagem)

    # CREATE
    def novo(self):
        return self._form(Aluno(), '/alunos')

    def criar(self):
        aluno = self._ler_formulario(Aluno())
        erros = aluno.validar()
        if erros:
            return self._form(aluno, '/alunos', erros)
        self.dao.criar(aluno)
        redirect('/alunos?msg=criado')

    # UPDATE
    def editar(self, id):
        aluno = self.dao.buscar(id)
        if aluno is None:
            abort(404, 'Aluno não encontrado.')
        return self._form(aluno, '/alunos/{}/editar'.format(id))

    def atualizar(self, id):
        aluno = self.dao.buscar(id)
        if aluno is None:
            abort(404, 'Aluno não encontrado.')
        self._ler_formulario(aluno)
        erros = aluno.validar()
        if erros:
            return self._form(aluno, '/alunos/{}/editar'.format(id), erros)
        self.dao.atualizar(aluno)
        redirect('/alunos?msg=atualizado')

    # DELETE
    def excluir(self, id):
        if not self.dao.remover(id):
            abort(404, 'Aluno não encontrado.')
        redirect('/alunos?msg=excluido')
