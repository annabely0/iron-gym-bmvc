(function () {
  var protocolo = window.location.protocol === 'https:' ? 'wss' : 'ws';
  var socket = null;

  function definirTexto(id, valor) {
    var elemento = document.getElementById(id);
    if (elemento) { elemento.textContent = valor; }
  }

  function status(texto, conectado) {
    var el = document.getElementById('status-ws');
    if (!el) { return; }
    el.textContent = texto;
    el.classList.toggle('on', conectado);
  }

  function aplicarEstado(estado) {
    var ids = {};
    estado.presentes.forEach(function (p) { ids[p.id] = true; });

    definirTexto('contador-presentes', estado.presentes.length);
    definirTexto('capacidade', estado.capacidade);
    definirTexto('total-alunos', estado.total_alunos);

    var barra = document.getElementById('barra-lotacao');
    if (barra) {
      var pct = Math.min(100, Math.round(estado.presentes.length * 100 / estado.capacidade));
      barra.style.width = pct + '%';
    }

    var lista = document.getElementById('lista-presentes');
    if (lista) {
      lista.textContent = '';
      estado.presentes.forEach(function (p) {
        var li = document.createElement('li');
        li.textContent = p.nome + ' · ' + p.modalidade + ' · desde ' + p.hora;
        lista.appendChild(li);
      });
      if (estado.presentes.length === 0) {
        var vazio = document.createElement('li');
        vazio.textContent = 'Ninguém treinando agora.';
        lista.appendChild(vazio);
      }
    }

    document.querySelectorAll('.btn-checkin').forEach(function (botao) {
      var dentro = ids[botao.getAttribute('data-id')] === true;
      botao.textContent = dentro ? 'Check-out' : 'Check-in';
      botao.classList.toggle('btn-sec', dentro);
    });
  }

  function conectar() {
    socket = new WebSocket(protocolo + '://' + window.location.host + '/ws');
    socket.onopen = function () { status('● ao vivo', true); };
    socket.onmessage = function (evento) {
      var dados = JSON.parse(evento.data);
      if (dados.tipo === 'estado') { aplicarEstado(dados); }
    };
    socket.onclose = function () {
      status('○ reconectando...', false);
      window.setTimeout(conectar, 2000);
    };
  }

  document.querySelectorAll('.btn-checkin').forEach(function (botao) {
    botao.addEventListener('click', function () {
      var id = botao.getAttribute('data-id');
      fetch('/alunos/' + id + '/checkin', { method: 'POST' })
        .then(function (resposta) { return resposta.json(); })
        .then(function (dados) {
          if (dados.erro) { window.alert(dados.erro); }
        });
    });
  });

  conectar();
})();
