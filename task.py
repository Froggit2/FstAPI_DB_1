from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.backend.database import Base
from sqlalchemy.orm import relationship


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("tasks.id"), nullable=False, index=True)
    slug = Column(String, unique=True, index=True)

    user = relationship("Users", back_populates='tasks')


from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))