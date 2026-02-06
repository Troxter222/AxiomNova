import sympy
from src.core.base_solver import BaseSolver

class SymbolicSolver(BaseSolver):
    def get_solver_type(self) -> str:
        return "SymbolicAlgebra v1.2 (Inherited Smart Input)"

    def solve(self, problem: str) -> str:
        # Используем метод родителя!
        clean_problem = self._preprocess(problem)
        
        try:
            if "=" in clean_problem:
                left, right = clean_problem.split("=")
                eq = sympy.Eq(sympy.sympify(left), sympy.sympify(right))
                symbols = list(eq.free_symbols)
                
                if not symbols:
                    return "Верно" if sympy.sympify(left) == sympy.sympify(right) else "Неверно"
                
                solution = sympy.solve(eq, symbols[0])
                if not solution:
                    return "∅ (Нет решений)"
                return f"{symbols[0]} = {solution}"
            
            else:
                expr = sympy.sympify(clean_problem)
                result = sympy.simplify(expr)
                return str(result)

        except Exception as e:
            raise ValueError(f"Алгебра: {e}")