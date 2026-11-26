% rebase('base', title='Ao vivo')
<div class="cabecalho-pagina">
  <h1>Controle de acesso ao vivo</h1>
  <span id="status-ws" class="status-ws">conectando...</span>
</div>

<div class="cartao">
  <p><strong id="contador-presentes">{{len(estado['presentes'])}}</strong> /
     <span id="capacidade">{{estado['capacidade']}}</span> pessoas treinando agora</p>
  <div class="barra"><div id="barra-lotacao" style="width: {{min(100, round(len(estado['presentes']) * 100 / estado['capacidade']))}}%"></div></div>
</div>

<div class="grade" style="margin-top:20px">
  <section>
    <h2>Quem está na academia</h2>
    <ul id="lista-presentes" class="lista-presentes">
      % for p in estado['presentes']:
      <li>{{p['nome']}} <small>· {{p['modalidade']}} · desde {{p['hora']}}</small></li>
      % end
      % if not estado['presentes']:
      <li>Ninguém treinando agora.</li>
      % end
    </ul>
  </section>

  <section>
    <h2>Registrar entrada/saída</h2>
    <table class="tabela">
      <tbody>
        % for a in alunos:
        <tr>
          <td>{{a.nome}}</td>
          <td><button class="btn btn-checkin {{'btn-sec' if a.presente else ''}}" data-id="{{a.id}}">{{'Check-out' if a.presente else 'Check-in'}}</button></td>
        </tr>
        % end
        % if not alunos:
        <tr><td>Cadastre alunos ativos primeiro.</td></tr>
        % end
      </tbody>
    </table>
  </section>
</div>
