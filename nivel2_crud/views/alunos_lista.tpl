% rebase('base', title='Alunos')
<div class="cabecalho-pagina">
  <h1>Alunos</h1>
  <a class="btn" href="/alunos/novo">+ Novo aluno</a>
</div>

% if mensagem:
<div class="aviso ok">{{mensagem}}</div>
% end

<label>Buscar aluno
  <input type="search" id="busca" placeholder="Digite um nome ou modalidade...">
</label>

<table class="tabela" id="tabela-alunos">
  <thead>
    <tr><th>#</th><th>Nome</th><th>Plano</th><th>Modalidade</th><th>Situação</th><th>Ações</th></tr>
  </thead>
  <tbody>
    % for a in alunos:
    <tr>
      <td>{{a.id}}</td>
      <td>{{a.nome}}<br><small>{{a.email}}</small></td>
      <td>{{a.plano}}</td>
      <td>{{a.modalidade}}</td>
      <td><span class="etiqueta {{'ativo' if a.ativo else ''}}">{{'Ativo' if a.ativo else 'Inativo'}}</span></td>
      <td class="acoes">
        <a href="/alunos/{{a.id}}/editar">Editar</a>
        <form method="post" action="/alunos/{{a.id}}/excluir" class="form-excluir">
          <button type="submit" class="btn-perigo">Excluir</button>
        </form>
      </td>
    </tr>
    % end
    % if not alunos:
    <tr><td colspan="6">Nenhum aluno cadastrado ainda.</td></tr>
    % end
  </tbody>
</table>
