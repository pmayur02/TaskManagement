from fastapi import HTTPException,status
from backend.app.schemas.schemas import TaskModel,UserModel
from backend.app.models.models import Task,User



def getTasks(db,currentUser):
    try:
        userDetail = db.query(User).filter(User.email == currentUser).first()
        allTasks = db.query(Task).filter(userDetail.id == Task.userId, User.isActive==True).all()
        if not allTasks:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Records Found!")
    
        return {
                "data": allTasks,
                "status":status.HTTP_200_OK,
                "message":"Data found successfully!"
            }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))
    
def getTask(id,db,currentUser):
    try:
        userDetail = db.query(User).filter(User.email == currentUser).first()
        task = db.query(Task).filter(Task.id == id,userDetail.id == Task.userId, User.isActive==True).first()
        if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Records Found!")
    
        return {
                "data": task,
                "status":status.HTTP_200_OK,
                "message":"Data found successfully!"
            }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))    

    
def createTasks(payload,db,currentUser):
    try:
        userDetail = db.query(User).filter(User.email == currentUser).first()

        body = payload.model_dump()
        body["userId"]= userDetail.id
        
        newTask = Task(**body)
        db.add(newTask)
        db.commit()
        db.refresh(newTask)
    
        return {
                "data": newTask,
                "status":status.HTTP_200_OK,
                "message":"Data found successfully!"
            }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))
    
def updateTask(id, updatePayload, db,currentUser):
    try:
        userDetail = db.query(User).filter(User.email == currentUser).first()
        task = db.query(Task).filter(Task.id == id,userDetail.id == Task.userId, User.isActive==True).first()
        if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Task Found!");
        
        for key, value in updatePayload.dict(exclude_unset=True).items():
            setattr(task, key, value)

        db.commit()
        db.refresh(task)

        return {
            "status": 200,
            "message": "task updated successfully",
            "data": task.id
        }
   
    except HTTPException:
          raise
    except Exception as e:
          raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))
    
def deleteTask(id,db,currentUser):
    try:
        userDetail = db.query(User).filter(User.email == currentUser).first()
        task = db.query(Task).filter(Task.id == id,userDetail.id == Task.userId, User.isActive==True).first()
        if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Records Found!")
        db.delete(task)
        db.commit()

        return {
            "status": 200,
            "message": "task deleted successfully",
            "data": task.id
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))
    

