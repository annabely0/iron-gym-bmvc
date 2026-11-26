<!doctype html>
<html lang="pt-br">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{academia}} · Treine sem desculpas</title>
  <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
  <header class="topo">
    <a class="logo" href="/">IRON<span>GYM</span></a>
    <button id="btn-menu" class="btn-menu" aria-label="Abrir menu">☰</button>
    <nav id="menu">
      <a href="#planos">Planos</a>
      <a href="#imc">Calculadora de IMC</a>
      <a href="#horarios">Horários</a>
    </nav>
  </header>

  <section class="hero">
    <h1>Treine sem desculpas.</h1>
    <p>Equipamentos novos, professores presentes e um ambiente feito para você evoluir.</p>
    <a class="btn" href="#planos">Conheça os planos</a>
  </section>

  <main class="conteudo">
    <section id="planos">
      <h2>Planos</h2>
      <div class="grade">
        % for p in planos:
        <article class="cartao {{'destaque' if p.destaque else ''}}">
          <h3>{{p.nome}}</h3>
          <p class="preco">{{p.preco_formatado()}}<small>/mês</small></p>
          <ul>
            % for b in p.beneficios:
            <li>{{b}}</li>
            % end
          </ul>
        </article>
        % end
      </div>
    </section>

    <section id="imc">
      <h2>Calculadora de IMC</h2>
      <div class="cartao">
        <label>Peso (kg)<input type="number" id="peso" step="0.1" min="1"></label>
        <label>Altura (m)<input type="number" id="altura" step="0.01" min="0.5"></label>
        <button class="btn" id="btn-imc">Calcular</button>
        <p id="resultado-imc" class="resultado" aria-live="polite"></p>
      </div>
    </section>

    <section id="horarios">
      <h2>Horários de funcionamento</h2>
      <table class="tabela">
        <tbody>
          % for dia, hora in horarios:
          <tr><td>{{dia}}</td><td>{{hora}}</td></tr>
          % end
        </tbody>
      </table>
    </section>
  </main>

  <footer>© {{academia}} · Projeto acadêmico de Orientação a Objetos</footer>
  <script src="/static/js/app.js"></script>
</body>
</html>
