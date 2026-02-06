import sympy
from src.core.base_solver import BaseSolver

class SymbolicSolver(BaseSolver):
    """
    Решатель для алгебры: уравнения, упрощение выражений.
    Использует библиотеку SymPy.
    """
    def get_solver_type(self) -> str:
        return "SymbolicAlgebra v1.0 (SymPy)"

    def solve(self, problem: str) -> str:
        # 1. Подготовка: заменяем ^ на ** (python стиль степени)
        problem = problem.replace("^", "**")
        
        try:
            # 2. Если есть знак "=", это уравнение
            if "=" in problem:
                left, right = problem.split("=")
                # Создаем уравнение: left = right
                # sympify превращает строку в математический объект
                eq = sympy.Eq(sympy.sympify(left), sympy.sympify(right))
                
                # Ищем переменную (обычно x, y, z...)
                # free_symbols находит все буквы в уравнении
                symbols = list(eq.free_symbols)
                
                if not symbols:
                    return str(sympy.sympify(left) == sympy.sympify(right))
                
                # Решаем уравнение
                solution = sympy.solve(eq, symbols[0])
                return f"{symbols[0]} = {solution}"
            
            else:
                # 3. Если нет "=", просто упрощаем выражение (например, "2x + 3x")
                expr = sympy.sympify(problem)
                result = sympy.simplify(expr)
                return str(result)

        except Exception as e:
            raise ValueError(f"Ошибка алгебры: {e}")