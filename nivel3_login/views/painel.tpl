% rebase('base', title='Painel')
<h1>Painel restrito</h1>
<p>Bem-vindo(a), <strong>{{usuario.nome}}</strong>. Esta página só aparece para usuários autenticados.</p>
<div class="metricas">
  <div class="cartao metrica"><strong>{{total}}</strong>Alunos cadastrados</div>
  <div class="cartao metrica"><strong>{{ativos}}</strong>Matrículas ativas</div>
</div>
<a class="btn" href="/alunos">Gerenciar alunos</a>
<a class="btn btn-sec" href="/alunos/novo">+ Novo aluno</a>
