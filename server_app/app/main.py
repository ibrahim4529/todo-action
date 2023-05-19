from typing import List
from fastapi import FastAPI, Depends
from app.db import migrate_db, get_session, TodoCreate, TodoRead, TodoUpdate, Todo
from sqlmodel import Session


app = FastAPI()


@app.on_event("startup")
def on_startup():
    print("Starting up -> try migrating db")
    migrate_db()


@app.get("/")
def root():
    return {
        "name": "Todo Actions",
        "version": "0.1.0",
        "description": "A simple todo app",
    }


@app.post("/todos", response_model=TodoRead)
def create_todo(todo_data: TodoCreate, session: Session = Depends(get_session)):
    todo = Todo.from_orm(todo_data)
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo


@app.get("/todos", response_model=List[TodoRead])
def read_todos(session: Session = Depends(get_session)):
    todos = session.query(Todo).all()
    return todos


@app.get("/todos/{todo_id}", response_model=TodoRead)
def read_single_todo(todo_id: int, session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    return todo


@app.put("/todos/{todo_id}", response_model=TodoRead)
def update_single_todo(todo_id: int, todo: TodoUpdate , session: Session = Depends(get_session)):
    db_todo = session.get(Todo, todo_id)
    todo_data = todo.dict(exclude_unset=True)
    for key, value in todo_data.items():
        setattr(db_todo, key, value)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo
