from pydantic import BaseModel
from typing import Optional

class Funcionario(BaseModel):
    id_funcionario: Optional[int]
    nome: str
    matricula: str
    cpf: str
    telefone: Optional[str]
    grupo: int
    senha: Optional[str]