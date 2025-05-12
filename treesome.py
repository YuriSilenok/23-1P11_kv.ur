"""Api для решения квадратного уравнения"""
from fastapi import FastAPI
from main import treesome

app = FastAPI()


@app.get("/treesome/")
async def treesome_result(a: int, b: int, c: int):
    """Возвращает решение квадратного уравнения"""
    return treesome(a, b, c)
