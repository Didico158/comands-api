from fastapi import APIRouter

router = APIRouter(prefix="/cliente", tags=["Cliente"])

@router.get("/", summary="Obter todos os clientes")
def get_clientes():
    return {"msg": "GET todos os clientes executado"}, 200

@router.get("/{id}", summary="Obter um cliente pelo ID")
def get_cliente_by_id(id: int):
    return {"msg": f"GET cliente com ID {id} executado"}, 200

@router.post("/", summary="Adicionar um novo cliente")
def adicionar_cliente():
    return {"msg": "POST cliente executado"}, 200

@router.put("/{id}", summary="Atualizar um cliente pelo ID")
def atualizar_cliente(id: int):
    return {"msg": f"PUT cliente com ID {id} executado"}, 201

@router.delete("/{id}", summary="Excluir um cliente pelo ID")
def excluir_cliente(id: int):
    return {"msg": f"DELETE cliente com ID {id} executado"}, 204
