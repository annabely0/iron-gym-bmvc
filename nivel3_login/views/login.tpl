% rebase('base', title='Entrar')
<div class="cartao cartao-login">
  <h1>Entrar</h1>
  % if erro:
  <div class="aviso erro">{{erro}}</div>
  % end
  <form method="post" action="/login">
    <input type="hidden" name="proximo" value="{{proximo}}">
    <label>Login
      <input type="text" name="login" autocomplete="username" required autofocus>
    </label>
    <label>Senha
      <input type="password" name="senha" id="senha" autocomplete="current-password" required>
    </label>
    <label>
      <input type="checkbox" id="mostrar-senha" style="width:auto"> Mostrar senha
    </label>
    <button type="submit" class="btn">Entrar</button>
  </form>
</div>
