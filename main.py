from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
from typing import Union

app = FastAPI()

'''
@app.get("/")
async def root():
    return "Hello World"
'''

'''
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
'''

'''
@app.get("/{item_id}")
async def read_item(item_id):
    return "вы перешли по /" + item_id
'''

'''
@app.get("/{item}")
async def read_item(item: int):
    return item
'''

'''
@app.get("/{item}")
async def read_item(item: float):
    return item
'''

'''
@app.get("/users/me")
async def read_user_me():
    return {"id": "текущий пользователь"}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"id": user_id}
'''

'''
class Names(str, Enum):
    test1 = 'test'
    test2 = 'test2'
    
@app.get("/models/{model_name}")
async def get_model(model_name: Names):
    if model_name is Names.test1:
        return model_name +":",'сообщение 1'

    if model_name is Names.test2:
        return model_name +":",'сообщение 2'
'''

'''
class Names(str, Enum):
    test1 = 'test'
    test2 = 'test2'
    
@app.get("/models/{model_name}")
async def get_model(model_name: Names):
    if model_name is Names.test1:
        return model_name +":",'сообщение 1'

    if model_name  == 'test2':
        return model_name +":",'работает лол'
'''

'''
Names = {'test1':'сообщение1'}

    
@app.get("/models/{model_name}")
async def get_model(model_name):
    for i in Names:
        if model_name == i:
            return Names[i]
'''


'''
class ModelName(str, Enum):
    test1 = "test1"
    test2 = "test2"
    test3 = "test3"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.test1:
        return {"model_name": model_name, "message": "lol🤣"}

    if model_name.value == "test3":
        return {"model_name": model_name, "message": "lol1😊"}

    return {"model_name": model_name, "message": "lol2😂"}
'''


'''
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
'''

'''
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 1, limit: int = 10):
    return fake_items_db[skip : skip + limit]
'''

'''
@app.get("/items/{item_id}")
async def read_item(item_id: str, testik: str | None = None):
    if testik:
        return {'какой то параметр', item_id}
    return {'нет параметра'}
'''

'''
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
'''

'''
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
'''

'''
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item
'''


'''
@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item
'''

'''
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.post("/items/")
async def create_item(item: Item):
    return item
'''









