from fastapi import FastAPI

app = FastAPI()

friends = [
    {"id": 1, "name": "Ravi"},
    {"id": 2, "name": "Suresh"},
    {"id": 3, "name": "Anil"}
]

@app.get("/")
def home():
    return {"message": "Welcome to my Friends API!"}

@app.get("/friends")
def get_friends():
    return friends