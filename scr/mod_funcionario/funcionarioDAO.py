from fastapi import APIRouter

router = APIRouter(prefix="/funcionario", tags=["Funcionário"])

@router.get("/", summary="Obter todos os funcionários")
def get_funcionarios():
    return {"msg": "GET todos os funcionários executado"}, 200

@router.get("/{id}", summary="Obter um funcionário pelo ID")
def get_funcionario_by_id(id: int):
    return {"msg": f"GET funcionário com ID {id} executado"}, 200

@router.post("/", summary="Adicionar um novo funcionário")
def adicionar_funcionario():
    return {"msg": "POST funcionário executado"}, 200

@router.put("/{id}", summary="Atualizar um funcionário pelo ID")
def atualizar_funcionario(id: int):
    return {"msg": f"PUT funcionário com ID {id} executado"}, 201

@router.delete("/{id}", summary="Excluir um funcionário pelo ID")
def excluir_funcionario(id: int):
    return {"msg": f"DELETE funcionário com ID {id} executado"}, 204
