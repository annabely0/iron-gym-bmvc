% u = usuario_logado()
<!doctype html>
<html lang="pt-br">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{title}} · Iron Gym</title>
  <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
  <header class="topo">
    <a class="logo" href="/">IRON<span>GYM</span></a>
    <button id="btn-menu" class="btn-menu" aria-label="Abrir menu">☰</button>
    <nav id="menu">
      <a href="/">Início</a>
      % if u:
      <a href="/painel">Painel</a>
      <a href="/alunos">Alunos</a>
      <a href="/ao-vivo">Ao vivo</a>
      <span class="status-ws">Olá, {{u.nome}}</span>
      <form method="post" action="/logout" style="margin:0">
        <button type="submit">Sair</button>
      </form>
      % else:
      <a href="/login">Entrar</a>
      % end
    </nav>
  </header>
  <main class="conteudo">
    {{!base}}
  </main>
  <footer>© Iron Gym · Projeto acadêmico de Orientação a Objetos</footer>
  <script src="/static/js/app.js"></script>
  % if u:
  <script src="/static/js/ws.js"></script>
  % end
</body>
</html>
