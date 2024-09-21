# MVP Full Stack - Sprint 1 - Back-End (API Maquininha)
## 1. Introdução

Este projeto é parte do MVP - _Minimum Viable Product_ - da _Sprint 1_ do curso **Desenvolvimento _Full Stack_ Básico** da PUC-Rio. O MVP é composto de um Back-End, com banco de dados, e de um Front-End. Neste repositório encontra-se a parte do Back-end da aplicação. A parte do front-end pode ser acessada em [MVP-FullStack-Sprint1-FrontEnd](https://github.com/brunorsouza81/MVP-FullStack-Sprint1-FrontEnd.git).

>O objetivo do projeto é realizar o cadastro de maquininhas de adquirência para facilitar o controle de estoque dos terminais POS de uma *Cooperativa de Crédito*. As cooperativas de crédito oferecem serviços bancários com baixo custo para a população.

Uma das dores dessas cooperativas é o controle de estoque de terminais POS. É importante saber quantos terminais estão em estoque para realizar novos pedidos de terminais a tempo da entrega acontecer sem interromper as novas negociações em andamento.

  
## 2. Back-end
O back-end da aplicação é responsável pela criação e manutenção do banco de dados da aplicação, bem como pelas rotas de requisição ao servidor. As rotas implementadas foram do tipo GET, POST e DELETE, e sua documentação pode ser acessada em Swagger, conforme instruções do item 4 do presente documento.

O back-end está organizado da seguinte forma:

- app.py *(onde estão definidas as rotas de requisição)*
- model:
    - __ init __.py *(responsável pela criação do banco de dados)*
    - base.py *(responsável pela criação de uma super classe com modelo em SQLAlchemy)*
    - terminal.py *(responsável por criar a classe terminal)*
- schemas:
    - __ init __.py *(responsável por importar os schemas criados nos arquivos error.py e terminal.py)*
    - error.py *(define como uma mensagem de erro será representada)*
    - terminal.py *(define os schemas que serão utilizados nas rotas de requisição)*
- requirements.txt *(contém as bibliotecas a serem instaladas, conforme instruções do item 4 do presente documento)*


## 3. Pré-Requisitos
- Recomenda-se o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

- Faz-se necessária a instalação de todas as dependências/bibliotecas listadas no arquivo requirements.txt:
```
    (env)$ pip install -r requirements.txt
```


## 4. Como executar
- Para processar a API e consultar sua documentação em Swagger, executar:
```
(env)$ flask run --host 0.0.0.0 --port 5000
```
- Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.


## 5. Considerações
Por se tratar de um MVP, algumas funcionalidades da API não foram implementadas neste momento, ficando para versões futuras da aplicação. Dentre as já mapeadas, destacam-se as relacionadas abaixo:

- Rota GET de listagem de terminais com filtragem por modelo ou status;
- Rota PUT para atualização do status do terminal cadastrado no banco de dados.