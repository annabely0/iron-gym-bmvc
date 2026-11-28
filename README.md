# Iron Gym | BMVC
Sistema de gerenciamento de academia, desenvolvido em **Python** com o framework **Bottle**, no padrão de arquitetura **MVC** (Model, View, Controller).
## Finalidade
Simular a rotina de uma academia: apresentar os planos e horários, cadastrar e gerenciar alunos, controlar o acesso dos funcionários ao sistema e acompanhar a lotação em tempo real.
O projeto evolui em quatro níveis, cada um em sua própria pasta e com seu próprio vídeo de apresentação. Neste momento, apenas o **nível 1** foi entregue.
## Níveis do projeto
| Nível | Propósito | Pasta | Vídeo | Commit de entrega | Status |
|:-----:|-----------|:-----:|:-----:|:-----------------:|:------:|
| 1 | Página estática em template TPL, com CSS e JavaScript ativos (planos e calculadora de IMC) | `nivel1_pagina_estatica` | [Link](https://youtu.be/eddZN9avpQQ) | `6e293b5` | Enviado |
| 2 | CRUD completo do modelo `Aluno`, com persistência em arquivo JSON | `nivel2_crud` | [Link](https://youtu.be/I9xHZZJS2Rs) | `A definir` | Pendente |
| 3 | CRUD com login, sessão em cookie assinado e páginas restritas | `nivel3_login` | Em breve | `A definir` | Pendente |
| 4 | Tudo do nível 3 mais WebSocket: check-in/out e lotação em tempo real | `nivel4_websocket` | Em breve | `A definir` | Pendente |
## Padrão MVC (nível 1)
| Camada | Onde está | O que faz |
|--------|-----------|-----------|
| Model | `models/plano.py` | A classe `Plano` guarda nome, preço e benefícios; o `CatalogoPlanos` entrega a lista de planos |
| View | `views/index.tpl` | Template TPL que percorre os planos com um laço `for` e monta a página |
| Controller | `controllers/site_controller.py` | O `SiteController` registra a rota `/` e a rota dos arquivos estáticos, e renderiza o template |
## Estrutura dos arquivos (nível 1)
| Arquivo | Função |
|---------|--------|
| `app.py` | Cria a aplicação Bottle, define a pasta de templates, instancia o controller e sobe o servidor |
| `models/plano.py` | Classes do domínio: `Plano` e `CatalogoPlanos` |
| `controllers/site_controller.py` | Rotas da página e dos arquivos estáticos |
| `views/index.tpl` | Página inicial: planos, calculadora de IMC e horários |
| `static/css/style.css` | Estilo da página, incluindo o menu responsivo |
| `static/js/app.js` | Menu para telas pequenas e cálculo do IMC sem recarregar a página |
| `requirements.txt` | Dependências do projeto |
## Como rodar
É necessário ter o Python 3 instalado. Abra um terminal na pasta do nível e use:

```bash
cd nivel1_pagina_estatica
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

O sistema abre em http://localhost:8080.

Se o seu sistema usa `python` em vez de `python3`, troque o comando.
## Autores

* Ana Clara Cheim de Matos
* Annabely Andrade Vieira
