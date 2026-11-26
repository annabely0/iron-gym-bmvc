% rebase('base', title='Início')
<section>
  <h1>Iron Gym · Sistema de gestão</h1>
  <p>Área pública do sistema. O cadastro de alunos e o painel são de <strong>acesso restrito</strong>
     aos funcionários.</p>
  % if usuario_logado():
  <a class="btn" href="/painel">Ir para o painel</a>
  % else:
  <a class="btn" href="/login">Entrar no sistema</a>
  % end
</section>
