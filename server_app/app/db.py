from typing import Optional
from sqlmodel import Field, SQLModel, Session, create_engine


class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    completed: bool = False


# This is not best practice, but it's a good way to get started just place this code in db.py:
class TodoCreate(SQLModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TodoRead(SQLModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

engine = create_engine("sqlite:///./database.db", echo=True)

def get_session():
    with Session(engine) as session:
        yield session


def migrate_db():
    SQLModel.metadata.create_all(engine)
