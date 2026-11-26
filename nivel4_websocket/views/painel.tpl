% rebase('base', title='Painel')
<h1>Painel restrito</h1>
<p>Bem-vindo(a), <strong>{{usuario.nome}}</strong>. Os números abaixo atualizam sozinhos, em tempo real.
   <span id="status-ws" class="status-ws">conectando...</span></p>
<div class="metricas">
  <div class="cartao metrica"><strong id="total-alunos">{{estado['total_alunos']}}</strong>Alunos cadastrados</div>
  <div class="cartao metrica"><strong id="contador-presentes">{{len(estado['presentes'])}}</strong>Treinando agora</div>
  <div class="cartao metrica"><strong id="capacidade">{{estado['capacidade']}}</strong>Capacidade</div>
</div>
<div class="barra"><div id="barra-lotacao" style="width: {{min(100, round(len(estado['presentes']) * 100 / estado['capacidade']))}}%"></div></div>
<p>
  <a class="btn" href="/ao-vivo">Controle de acesso ao vivo</a>
  <a class="btn btn-sec" href="/alunos">Gerenciar alunos</a>
</p>
