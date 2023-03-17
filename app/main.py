from fastapi import FastAPI
from .database import engine
from .router import books_data
from .models import models


models.Base.metadata.create_all(bind=engine)



app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Wellcome to Baccvs api please write end of code /docs"}


app.include_router(books_data.router)
