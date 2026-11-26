# Iron Gym | BMVC

Sistema de gestão para uma academia, a **Iron Gym**, desenvolvido em **Python** com o framework **Bottle**, no padrão de arquitetura **MVC** (Model, View, Controller). O projeto evolui em quatro níveis, cada um em sua própria pasta e com seu próprio vídeo de apresentação.

## Finalidade

Simular a rotina de uma academia: apresentar os planos, cadastrar e gerenciar alunos, controlar o acesso dos funcionários ao sistema e acompanhar a lotação em tempo real.

O projeto aplica o padrão MVC, persistência em arquivos JSON (DAO), autenticação com hash e salt, sessão em cookie assinado e comunicação em tempo real com WebSocket.

## Níveis do projeto

| Nível | Propósito | Pasta | Vídeo | Commit de entrega | Status |
|:-:|---|---|:-:|:-:|:-:|
| 1 | Página estática em template TPL, com CSS e JavaScript (planos e calculadora de IMC) | `nivel1_pagina_estatica` | Em breve | `A definir` | Pendente |
| 2 | CRUD completo do modelo Aluno, com persistência em JSON | `nivel2_crud` | Em breve | `A definir` | Pendente |
| 3 | CRUD com login, sessão em cookie assinado e páginas restritas | `nivel3_login` | Em breve | `A definir` | Pendente |
| 4 | Tudo do nível 3 mais WebSocket: check-in/out e lotação em tempo real | `nivel4_websocket` | Em breve | `A definir` | Pendente |

## Como rodar

Em cada pasta de nível:

```bash
cd nivelX_nome_da_pasta
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

O sistema abre em http://localhost:8080.

Nos níveis 3 e 4, o login inicial é `admin` / `admin123`, criado na primeira execução.

Para testar o tempo real no nível 4, abra `/ao-vivo` em duas janelas e faça check-in em uma delas.

## Estrutura de cada projeto

```
models/        # classes de domínio e DAO (JSON em data/)
views/         # templates .tpl
controllers/   # rotas (uma classe por assunto)
services/      # autenticação (nível 3) e hub WebSocket (nível 4)
static/        # css/ e js/
app.py         # monta tudo e sobe o servidor
```

## Autoria

Desenvolvido em dupla por [nome da Pessoa 1] e Annabely.
