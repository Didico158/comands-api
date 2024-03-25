from fastapi import FastAPI
from settings import HOST, PORT, RELOAD
from mod_funcionario import FuncionarioDAO
from mod_cliente import ClienteDAO

app = FastAPI()

# Mapeamento das rotas/endpoints
app.include_router(FuncionarioDAO.router)
app.include_router(ClienteDAO.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=HOST, port=int(PORT), reload=RELOAD)
