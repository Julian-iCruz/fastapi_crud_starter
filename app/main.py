from fastapi import FastAPI
from db.session import engine
from db.models import Base
from routers import items

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(items.router, prefix="/items", tags=["Items"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI CRUD Starter!"}
