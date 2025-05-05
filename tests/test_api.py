"""D=0"""
from fastapi import FastAPI
from pydantic import BaseModel
import unittest
import sys

app = FastAPI()

class QuadraticEquation(BaseModel):
    a: float  # Коэффициент при x²
    b: float  # Коэффициент при x
    c: float  # Свободный член


def solve_quadratic_equation(a: float, b: float, c: float):
    """ иухэ """
    if a == 0:
        return {
            "error": "Коэффициент a не может быть равен нулю,"
            " это не квадратное уравнение."
        }
    
    D = b**2 - 4*a*c  # Вычисляем дискриминант

    if D != 0:
        return {
            "error": "Обрабатывается только случай"
            " с дискриминантом равным нулю."
        }
    
    root = -b / (2*a)
    explanation = "Дискриминант равен нулю. Уравнение имеет один двойной корень."
    roots = [root]

    return {
        "a": a,
        "b": b,
        "c": c,
        "discriminant": D,
        "explanation": explanation,
        "roots": roots
    }

@app.post("/solve/")
def solve_quadratic(eq: QuadraticEquation):
    return solve_quadratic_equation(eq.a, eq.b, eq.c)


# unittest интегрирован в этот же файл

class TestQuadraticSolver(unittest.TestCase):

    def test_double_root(self):
        result = solve_quadratic_equation(1, 2, 1)  # D=0, корень -1
        self.assertEqual(result["discriminant"], 0)
        self.assertEqual(len(result["roots"]), 1)
        self.assertAlmostEqual(result["roots"][0], -1.0)
        self.assertIn("один двойной корень", result["explanation"])

    def test_not_quadratic(self):
        result = solve_quadratic_equation(0, 2, 1)
        self.assertIn("error", result)
        self.assertEqual(result["error"], "Коэффициент a не может быть равен нулю, это не квадратное уравнение.")

    def test_discriminant_not_zero(self):
        result = solve_quadratic_equation(1, 3, 1)  # D != 0
        self.assertIn("error", result)
        self.assertEqual(result["error"], "Обрабатывается только случай с дискриминантом равным нулю.")

if name == "main":
    unittest.main()