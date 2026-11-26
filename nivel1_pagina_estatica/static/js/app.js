(function () {
  var btnMenu = document.getElementById('btn-menu');
  var menu = document.getElementById('menu');
  if (btnMenu && menu) {
    btnMenu.addEventListener('click', function () {
      menu.classList.toggle('aberto');
    });
  }

  var btnImc = document.getElementById('btn-imc');
  if (btnImc) {
    btnImc.addEventListener('click', function () {
      var peso = parseFloat(document.getElementById('peso').value);
      var altura = parseFloat(document.getElementById('altura').value);
      var saida = document.getElementById('resultado-imc');
      if (!peso || !altura) {
        saida.textContent = 'Informe peso e altura válidos.';
        return;
      }
      var imc = peso / (altura * altura);
      var faixa = 'obesidade';
      if (imc < 18.5) { faixa = 'abaixo do peso'; }
      else if (imc < 25) { faixa = 'peso normal'; }
      else if (imc < 30) { faixa = 'sobrepeso'; }
      saida.textContent = 'Seu IMC é ' + imc.toFixed(1) + ' (' + faixa + ').';
    });
  }
})();
