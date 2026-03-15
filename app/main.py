from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.db.database import TORTOISE_CONFIG
from app.core.config import settings

app = FastAPI()

register_tortoise(
    app,
    config=TORTOISE_CONFIG,
    generate_schemas=True,
    add_exception_handlers=True
)

@app.get('/')
async def root():
    return {"msg":f"wellcome {settings.PROJECT_NAME}"}

if __name__=="__main__":
    import uvicorn
    uvicorn.run("app.main:app",host="127.0.0.1",port=8000,reload=True)