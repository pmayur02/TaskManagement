from backend.app.models.models import User
from fastapi import HTTPException, status
from backend.app.utilities.authentication import hashPassword, verifyPassword, user_helper, createAccessToken


def getUsers(db):
    try:
        data = db.query(User).filter(User.isActive ==True)
        users = [user_helper(u) for u in data]
        if not users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Records Found!")
        return {
            "data":users,
            "message": "Data Found successfully",
            "status": status.HTTP_200_OK
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))
    
def registerUsers(payload, db):
    try:
            body = payload.model_dump()
            userExist = db.query(User).filter(User.email == body["email"]).first()

            if userExist:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User Already Exists!")
    
            body["password"] = hashPassword(body["password"])
            new_user = User(**body)
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            return {
                "message" :"User Registered Successfully!",
                "status" : status.HTTP_200_OK 
            }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))
    
def getUser(userId,db):
    try:
        user = db.query(User).filter(User.isActive == True, User.id == userId).first() 
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No User Found!")
        return {
                "data":user_helper(user),
                "message": "Data Found successfully",
                "status": status.HTTP_200_OK
        }
    
    except HTTPException:
        raise
    except Exception as e:
         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))
    

def updateUser(userId, updatePayload, db):
    try:
        userExist = db.query(User).get(userId) 
        if not userExist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No User Found!");
        
        for key, value in updatePayload.dict(exclude_unset=True).items():
            setattr(userExist, key, value)

        db.commit()
        db.refresh(userExist)

        return {
            "status": 200,
            "message": "User updated successfully",
            "data": userExist.id
        }
   
    except HTTPException:
          raise
    except Exception as e:
          raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))


def deleteUser(userId,db):
    try:
        isUserExist = db.query(User).get(userId)
        if not isUserExist:
              raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No User Found!");

        isUserExist.isActive = False
        db.commit()
        db.refresh(isUserExist)
        return {
            "status": 200,
            "message": "User updated successfully",
            "data":[]
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))
          

def login(payload, db):
    try:
        isUserExist = db.query(User).filter(User.email == payload.username and User.isActive == True).first()
        if not isUserExist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No User Found!")
        
        
        validPassword = verifyPassword(payload.password,isUserExist.password)
        
        if not validPassword:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Credentials")
        
        token = createAccessToken(data={"sub": isUserExist.email})
        return {"access_token":token, "token_type":"bearer"}
        

        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))
    

def isAdmin(adminEmail,db):
    isAdmin = db.query(User).filter(User.role == "Admin",User.email == adminEmail).first()

    if not isAdmin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Access Denied")
    
    return isAdmin