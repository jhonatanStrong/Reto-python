from fastapi import FastAPI , Form
from typing import Annotated
from Config_datos import Config_datos as cof
from models import Gender, Role, User , Valors
from typing import List
from uuid import uuid4

os = cof()
a = os.funion_datos()



lists = []
for x in a['fecha']:
    lists.append(
       Valors(
    #id=uuid4(),
    fecha=a['fecha'][x],
    valor=a['valor'][x],
            )

    )

db: List[Valors] = [

lists

]


datos = a
app = FastAPI()
fo = Form()

@app.get("/api/v1/valores")
async def get_users():
 return db


"""



@app.get("/")
def index():
    #da = {}
    #da = datos
    return {"02/12/193":100 ,"03/12/193":200 , "04/12/193":300}


@app.get("/libros/{id}")
def mostrar_libros(id: int):



    return {"data":id}

@app.post("/login/")
async def login(username: Annotated[str, fo], password: Annotated[str, fo]):



    return {"username": username}"""