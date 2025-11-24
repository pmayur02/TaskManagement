import os
from dotenv import load_dotenv

load_dotenv()

class dbSettings:
    host= os.getenv("DB_HOST")
    user= os.getenv("DB_USER")
    password= os.getenv("DB_PASSWORD")
    port= os.getenv("DB_PORT")
    name= os.getenv("DB_NAME")


dbConfig = dbSettings()





class Authentication:
    secretKey = os.getenv("SECRETKEY")
    algorithm = os.getenv("ALGORITHM")
    tokenExpireDuration = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

auth = Authentication()

    


