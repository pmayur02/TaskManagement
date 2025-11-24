from backend.app.models.models import User
from backend.app.dbconnection.database import Base, engine


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)