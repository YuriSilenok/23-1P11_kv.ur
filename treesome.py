"""Api для решения квадратного уравнения"""
from fastapi import FastAPI, Depends
from main import treesome

app = FastAPI()


@app.get("/treesome/")
async def treesome_result(result: dict = Depends(treesome)):
    """Возвращает решение квадратного уравнения"""
    return result
