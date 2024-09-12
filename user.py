from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.backend.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    task = relationship("Task", back_populates='user')


from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))