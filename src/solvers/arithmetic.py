from src.core.base_solver import BaseSolver

class ArithmeticSolver(BaseSolver):
    """
    Простейший решатель, использующий встроенные возможности Python.
    Решает задачи вида: '2 + 2', '10 * 5', '(3 + 5) / 2'
    """

    def get_solver_type(self) -> str:
        return "BasicArithmetic v1.0"

    def solve(self, problem: str) -> float:
        # Очистка строки от мусора (защита от инъекций кода в будущем)
        allowed_chars = set("0123456789+-*/(). ")
        if not set(problem).issubset(allowed_chars):
            raise ValueError("Обнаружены недопустимые символы. Этот модуль решает только базовую арифметику.")
        
        try:
            result = eval(problem) 
            return float(result)
        except Exception as e:
            raise ValueError(f"Не удалось решить задачу: {e}")