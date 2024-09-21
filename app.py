from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Terminal
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="API Maquininha", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
terminal_tag = Tag(name="Terminal", description="Inclusão, visualização e exclusão de terminais à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/terminal', tags=[terminal_tag],
          responses={"200": TerminalViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_terminal(form: TerminalSchema):
    """Inclui um novo Terminal no banco de dados

    Retorna uma representação dos terminais.
    """
    terminal = Terminal(
        numero_de_serie=form.numero_de_serie,
        modelo_terminal=form.modelo_terminal,
        status=form.status)
    logger.debug(f"Incluindo terminal número de série: '{terminal.numero_de_serie}'")
    try:
        # criando conexão com a base
        session = Session()
        # incluindo terminal
        session.add(terminal)
        # salvando a inclusão do novo terminal na tabela
        session.commit()
        logger.debug(f"Incluindo terminal número de série: '{terminal.numero_de_serie}'")
        return busca_terminal(terminal), 200

    except IntegrityError as e:
        # caso ocorra a inclusão de terminal com o mesmo número de série recupera o erro
        error_msg = "Terminal com o mesmo número de série já existe no banco de dados :/"
        logger.warning(f"Erro ao incluir o terminal número de série '{terminal.numero_de_serie}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso ocorra um erro imprevisto
        error_msg = "Não foi possível incluir o novo terminal:/"
        logger.warning(f"Erro ao incluir o terminal número de série '{terminal.numero_de_serie}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/terminais', tags=[terminal_tag],
         responses={"200": ListagemTerminaisSchema, "404": ErrorSchema})
def get_terminais():
    """Busca a lista de todos os terminais cadastrados

    Retorna uma representação da listagem de terminais.
    """
    logger.debug(f"Buscando terminais ")
    # criando conexão com a base
    session = Session()
    # buscando lista
    terminais = session.query(Terminal).all()

    if not terminais:
        # se não há produtos cadastrados
        return {"terminais": []}, 200
    else:
        logger.debug(f"%d terminais econtrados" % len(terminais))
        # retorna a representação de produto
        print(terminais)
        return lista_terminais(terminais), 200


@app.get('/terminal', tags=[terminal_tag],
         responses={"200": TerminalViewSchema, "404": ErrorSchema})
def get_terminal(query: TerminalBuscaSchema):
    """Faz a busca por um Terminal a partir do número de série do terminal

    Retorna uma representação dos terminais.
    """
    numero_de_serie = query.numero_de_serie
    logger.debug(f"Buscando dados do terminal #{numero_de_serie}")
    # criando conexão com a base
    session = Session()
    # buscando os dados
    terminal = session.query(Terminal).filter(Terminal.numero_de_serie == numero_de_serie).first()

    if not terminal:
        # se o terminal não foi encontrado
        error_msg = "Terminal não encontrado no banco de dados :/"
        logger.warning(f"Erro ao buscar o terminal número de série: '{numero_de_serie}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Terminal econtrado: '{numero_de_serie}'")
        # retorna a representação de terminal
        return busca_terminal(terminal), 200


@app.delete('/terminal', tags=[terminal_tag],
            responses={"200": TerminalDeleteSchema, "404": ErrorSchema})
def del_terminal(query: TerminalBuscaSchema):
    """Exclui um Terminal a partir do número de série

    Retorna uma mensagem confirmando a exclusão.
    """
    numero_de_serie = unquote(unquote(query.numero_de_serie))
    print(numero_de_serie)
    logger.debug(f"Excluindo o terminal número de série: {numero_de_serie}")
    # criando conexão com a base
    session = Session()
    # excluindo terminal
    session_retorno = session.query(Terminal).filter(Terminal.numero_de_serie == numero_de_serie).delete()
    # salvando a exclusão do terminal no banco de dados
    session.commit()

    if session_retorno:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Excluindo o terminal número de série: {numero_de_serie}")
        return {"mensagem": "Terminal excluído", "numero_de_serie": numero_de_serie}
    else:
        # se o terminal não foi encontrado
        error_msg = "Terminal não encontrado no banco de dados :/"
        logger.warning(f"Erro ao excluir o terminal número de série: '{numero_de_serie}', {error_msg}")
        return {"mensagem": error_msg}, 404
