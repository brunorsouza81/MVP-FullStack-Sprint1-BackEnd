from pydantic import BaseModel
from typing import Optional, List
from model.terminal import Terminal


class TerminalSchema(BaseModel):
    """ Define como um novo terminal é representado para ser inserido
    """
    numero_de_serie: str = "PB123456789"
    modelo_terminal: str = "Smart POS - P2"
    status: str = "Em estoque"


class TerminalBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. 
        A busca será feita apenas com o número de série do terminal.
    """
    numero_de_serie: str = "PB123456789"


class ListagemTerminaisSchema(BaseModel):
    """ Define como uma listagem de terminais será retornada.
    """
    terminais:List[TerminalSchema]


def lista_terminais(terminais: List[Terminal]):
    """ Retorna uma representação do terminal seguindo o schema definido em
        TerminalViewSchema.
    """
    lista = []
    for terminal in terminais:
        lista.append({
            "numero_de_serie": terminal.numero_de_serie,
            "modelo_terminal": terminal.modelo_terminal,
            "status": terminal.status
        })

    return {"terminais": lista}


class TerminalViewSchema(BaseModel):
    """ Define como um terminal será visualizado.
    """
    id: int = 1
    numero_de_serie: str = "PB123456789"
    modelo_terminal: str = "Smart POS - P2"
    status: str = "Em estoque"


class TerminalDeleteSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição de exclusão.
    """
    mensagem: str
    numero_de_serie: str

def busca_terminal(terminal: Terminal):
    """ Retorna uma representação do terminal seguindo o schema definido em TerminalViewSchema.
    """
    return {
        "id": terminal.id,
        "numero_de_serie": terminal.numero_de_serie,
        "modelo_terminal": terminal.modelo_terminal,
        "status": terminal.status
    }
