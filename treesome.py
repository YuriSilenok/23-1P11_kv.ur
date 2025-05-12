"""Api для решения квадратного уравнения"""
from fastapi import FastAPI
from main import treesome

app = FastAPI()


@app.get("/treesome/")
async def treesome_result(a: float, b: float, c: float):
    """Возвращает решение квадратного уравнения"""
    return treesome(a, b, c)
