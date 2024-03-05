from fastapi import FastAPI
import model
from config import engine
import router

model.Base.metadata.create_all(bind=engine)


app=FastAPI()

@app.get('/')
async def Home():
    return "Welcome Home | أهلاً بك في بيتك | 欢迎回家 | Добро пожаловать домой"


app.include_router(router.router,prefix="/book",tags=["book"])