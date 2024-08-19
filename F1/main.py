from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()

# Create a Model

class User(BaseModel):
	id: str
	user_name: str
	password: str

users = []

@app.get('/users')
def get_users():
	return users

@app.post('/user')
def save_user(user: User):
	users.append(user)
	return users

@app.put('/user/{id}')
def update_user(id: str, update_user: User):
	for idx, user in enumerate(users):
		if user.id == id:
			users[idx] = update_user
			return users
	return f'user id ${id} not found !'

@app.delete('/users/{id}')
def delete_user(id: str):
	users_temp = [user for user in users if user.id != id]
	return users_temp
