from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class RecentlyUsedProject(Base):
    __tablename__ = "recent_used_projects"
    id = Column(Integer, primary_key=True)
    path = Column(String())

    def __repr__(self):
        return f"RecentlyUsedProject(id={self.id!r}, name={self.path!r})"
