(function () {
  var btnMenu = document.getElementById('btn-menu');
  var menu = document.getElementById('menu');
  if (btnMenu && menu) {
    btnMenu.addEventListener('click', function () {
      menu.classList.toggle('aberto');
    });
  }

  // Confirmação antes de excluir
  var formsExcluir = document.querySelectorAll('.form-excluir');
  formsExcluir.forEach(function (form) {
    form.addEventListener('submit', function (evento) {
      if (!window.confirm('Deseja realmente excluir este aluno?')) {
        evento.preventDefault();
      }
    });
  });

  // Filtro da tabela em tempo de digitação
  var busca = document.getElementById('busca');
  var linhas = document.querySelectorAll('#tabela-alunos tbody tr');
  if (busca) {
    busca.addEventListener('input', function () {
      var termo = busca.value.toLowerCase();
      linhas.forEach(function (linha) {
        var visivel = linha.textContent.toLowerCase().indexOf(termo) !== -1;
        linha.style.display = visivel ? '' : 'none';
      });
    });
  }
})();
