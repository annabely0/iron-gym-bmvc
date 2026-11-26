% rebase('base', title='Aluno')
<h1>{{'Editar aluno' if aluno.id else 'Novo aluno'}}</h1>

% for e in erros:
<div class="aviso erro">{{e}}</div>
% end

<form method="post" action="{{acao}}" class="formulario">
  <label>Nome
    <input type="text" name="nome" value="{{aluno.nome}}" required minlength="3">
  </label>
  <label>E-mail
    <input type="email" name="email" value="{{aluno.email}}" required>
  </label>
  <label>Plano
    <select name="plano">
      % for p in planos:
      <option value="{{p}}" {{'selected' if p == aluno.plano else ''}}>{{p}}</option>
      % end
    </select>
  </label>
  <label>Modalidade
    <select name="modalidade">
      % for m in modalidades:
      <option value="{{m}}" {{'selected' if m == aluno.modalidade else ''}}>{{m}}</option>
      % end
    </select>
  </label>
  <label>Data de início
    <input type="date" name="data_inicio" value="{{aluno.data_inicio}}">
  </label>
  <label>
    <input type="checkbox" name="ativo" {{'checked' if aluno.ativo else ''}} style="width:auto">
    Matrícula ativa
  </label>
  <button type="submit" class="btn">Salvar</button>
  <a class="btn btn-sec" href="/alunos">Cancelar</a>
</form>
