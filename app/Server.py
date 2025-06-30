from typing import Union

from fastapi import FastAPI
from config.Config import getSettings
from config.db.db import init_db

from models.user.UserModel import User
app = FastAPI()

settings = getSettings()
init_db(app)

@app.get("/")
async def get_user():
    user = await User.all()
    print(user)
    return user


@app.post("/")
async def create_user():
    print("a")
    user = await User.create(name="a")
    return user


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}