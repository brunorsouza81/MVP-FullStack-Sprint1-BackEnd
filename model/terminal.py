from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class Terminal(Base):
    __tablename__ = 'terminal'

    id = Column("pk_terminal", Integer, primary_key=True)
    numero_de_serie = Column(String(11), unique=True)
    modelo_terminal = Column(String(20))
    status = Column(String(20))

    def __init__(self, numero_de_serie:str, modelo_terminal:str , status:str):
        """
        Cria um Terminal

        Arguments:
            numero_de_serie: número de série do terminal.
            modelo_terminal: modelo do terminal [Smart POS - P2, Smart POS - X990, POS - S920]
            status: status do terminal [Em estoque, Instalado, Reversado].
        """
        self.numero_de_serie = numero_de_serie
        self.modelo_terminal = modelo_terminal
        self.status = status