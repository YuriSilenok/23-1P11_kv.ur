"""D=0"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class QuadraticEquation(BaseModel):
    """иухэ"""
    a: float
    b: float
    c: float


@app.post("/solve/")
def solve_quadratic(eq: QuadraticEquation):
    """иухэ"""
    a, b, c = eq.a, eq.b, eq.c
    d = b**2 - 4*a*c

    if d == 0:
        root = -b / (2*a)
        explanation = (
            "Дискриминант равен нулю.",
            "Уравнение имеет один двойной корень.")
        root = [root]

        return {
            "a": a,
            "b": b,
            "c": c,
            "discriminant": d,
            "explanation": explanation,
            "roots": root}
    return "null"
