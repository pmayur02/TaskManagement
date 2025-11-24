from fastapi import APIRouter,Depends
from backend.app.schemas.schemas import TaskModel,UpdateTaskModel
from backend.app.dbconnection.database import get_db
from backend.app.services.todos import getTasks,createTasks,getTask,updateTask,deleteTask
from backend.app.utilities.authentication import get_current_user
from backend.app.models.models import User
from sqlalchemy.orm import Session


router = APIRouter()

@router.get("/gettasks")
def  getAllTasks(db:Session = Depends(get_db), currentUser:User = Depends(get_current_user)):
    response = getTasks(db,currentUser.email)
    return response

@router.get("/gettask/{id}")
def getATask(id:int, db:Session = Depends(get_db), currentUser:User = Depends(get_current_user)):
    response = getTask(id,db,currentUser.email)
    return response

@router.post("/createtask")
def  createTask(tasks:TaskModel, db:Session = Depends(get_db), currentUser:User = Depends(get_current_user)):
    response = createTasks(tasks,db,currentUser.email)
    return response

@router.post("/updateTask/{id}")
def updateATask(id:int,task:UpdateTaskModel, db:Session = Depends(get_db), currentUser:User = Depends(get_current_user)):
    response = updateTask(id,task,db,currentUser.email)
    return response

@router.post("/deleteTask/{id}")
def deleteATask(id:int, db:Session = Depends(get_db), currentUser:User = Depends(get_current_user)):
    response = deleteTask(id,db,currentUser.email)
    return response