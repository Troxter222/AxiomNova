import sympy
from src.core.base_solver import BaseSolver

class CalculusSolver(BaseSolver):
    """
    Решает задачи матана: производные и интегралы.
    Примеры: "diff(x^2)", "integrate(2*x)"
    """
    def get_solver_type(self) -> str:
        return "CalculusEngine v1.0"

    def solve(self, problem: str) -> str:
        # SymPy отлично понимает строки вида "diff(sin(x), x)"
        # Мы просто передаем строку в sympify, он сам распознает функции
        try:
            expr = sympy.sympify(problem)
            result = expr.doit() # doit() заставляет SymPy вычислить интеграл/производную
            return str(result)
        except Exception as e:
            raise ValueError(f"Calculus Error: {e}")