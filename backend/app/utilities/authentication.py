from pwdlib import PasswordHash
from datetime import datetime,timedelta,timezone
from jose import jwt,JWTError
from backend.app.utilities.config import auth
from fastapi import HTTPException,status,Depends
from backend.app.schemas.schemas import TokenData 
from fastapi.security import OAuth2PasswordBearer


passHash = PasswordHash.recommended()

def hashPassword(orgPassword):
    return passHash.hash(orgPassword)

def verifyPassword(plainPass,hashPass):
    return passHash.verify(plainPass,hashPass)

def user_helper(user) -> dict:
    return {
        "name": user["name"] if isinstance(user, dict) else user.name,
        "email": user.get("email", "") if isinstance(user, dict) else getattr(user, "email", "")
    }

def createAccessToken(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=float(auth.tokenExpireDuration))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, auth.secretKey, algorithm=auth.algorithm)
    return encoded_jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

async def get_current_user(token: str=Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, auth.secretKey, algorithms=[auth.algorithm])
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception

    return token_data



