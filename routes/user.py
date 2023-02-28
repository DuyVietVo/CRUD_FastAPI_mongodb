from fastapi import APIRouter
from schemas.user import userEntity,usersEntity
from models.user import User
from config.db import conn
from bson import ObjectId

user = APIRouter()

@user.get('/user')
async def find_all():
    return usersEntity(conn.test.user.find())

@user.get('/user/{id}')
async def find_one_user(id:str):
    return userEntity(conn.test.user.find_one({"_id": ObjectId(id)}))

@user.post('/user')
async def create_user(user: User):
    conn.test.user.insert_one(dict(user))
    return usersEntity(conn.test.user.find())

@user.put('/user/{id}')
async def update_user(id: str, user: User):
    conn.test.user.find_one_and_update({'_id': ObjectId(id)}, {'$set': dict(user)})
    return userEntity(conn.test.user.find_one({"_id": ObjectId(id)}))

@user.delete('/user/{id}')
async def delete_user(id: str):
    return userEntity(conn.test.user.find_one_and_delete({'_id': ObjectId(id)}))