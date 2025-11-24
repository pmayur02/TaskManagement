from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
from backend.app.dbconnection.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(50),unique=True ,index=True)
    password = Column(String(50))
    role = Column(Enum("User", "Admin"))
    isActive = Column(Boolean,default=True)
    todos = relationship("Task",back_populates="task")



class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String(255),index=True)
    taskDetail = Column(String(255))
    userId = Column(Integer,ForeignKey("users.id"))
    task = relationship("User",back_populates="todos")
