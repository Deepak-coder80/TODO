
from fastapi import FastAPI
import models
from database import engine
app = FastAPI()

models.Base.metadata.create_all(bind=engine)
@app.get('/')
async def create_db():
    return  {'Connection':'Established'}