from fastapi import FastAPI
from backend.app.routes import users,todos
from backend.app.dbconnection.database import engine,Base 

app = FastAPI()




Base.metadata.create_all(bind=engine)
app.include_router(users.router)
app.include_router(todos.router)