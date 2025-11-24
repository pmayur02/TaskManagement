from fastapi import APIRouter,Depends
from backend.app.models.models import User
from backend.app.schemas.schemas import UserModel, UserResponseModel,UpdateUser
from backend.app.services.users import getUsers,registerUsers, getUser, updateUser,deleteUser,login,isAdmin
from backend.app.dbconnection.database import get_db
from sqlalchemy.orm import Session
from backend.app.utilities.authentication import get_current_user
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    tags=["Users"],
    prefix="/users"
)


@router.post("/registeruser")
def registerUser(user:UserModel,db:Session= Depends(get_db)):
    response = registerUsers(user,db)
    return response

@router.get("/getusers",response_model=UserResponseModel)
def getAllUsers(db:Session = Depends(get_db), currentUser:User = Depends(get_current_user)):
    isAdmin(currentUser.email,db)
    response = getUsers(db)
    return response;

@router.get("/getuser/{id}")
def getAUser(id:int,db:Session = Depends(get_db), currentUser:User = Depends(get_current_user)):
    isAdmin(currentUser.email,db)
    response = getUser(id,db)
    return response

@router.post("/updateuser/{id}")
def updateAUser(id:int,updateData:UpdateUser ,db:Session = Depends(get_db), currentUser:User = Depends(get_current_user)):
    isAdmin(currentUser.email,db)
    response = updateUser(id,updateData,db)
    return response


@router.post("/deleteuser/{id}")
def deleteAUser(id:int,db:Session = Depends(get_db), currentUser:User = Depends(get_current_user)):
    isAdmin(currentUser.email,db)
    response = deleteUser(id,db)
    return response

@router.post("/login")
def loginUser(loginRequest:OAuth2PasswordRequestForm=Depends(), db:Session = Depends(get_db)):
    response = login(loginRequest, db)
    return response
