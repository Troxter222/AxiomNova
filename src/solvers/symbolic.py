import sympy
import re
from src.core.base_solver import BaseSolver

class SymbolicSolver(BaseSolver):
    def get_solver_type(self) -> str:
        return "SymbolicAlgebra v1.1 (Smart Input)"

    def _preprocess(self, problem: str) -> str:
        """
        Превращает человеческий ввод ('2x', '(x+1)(x-2)') в понятный Python ('2*x', ...).
        """
        # 1. Заменяем ^ на **
        problem = problem.replace("^", "**")
        
        # 2. Вставляем * между числом и буквой (2x -> 2*x)
        # Ищет цифру, за которой сразу идет буква
        problem = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', problem)
        
        # 3. Вставляем * между числом и скобкой (2(x+1) -> 2*(x+1))
        problem = re.sub(r'(\d)(\()', r'\1*\2', problem)
        
        # 4. Вставляем * между скобкой и буквой ((x+1)x -> (x+1)*x)
        problem = re.sub(r'(\))([a-zA-Z])', r'\1*\2', problem)
        
        # 5. Вставляем * между скобками ((a)(b) -> (a)*(b))
        problem = re.sub(r'(\))(\()', r'\1*\2', problem)
        
        return problem

    def solve(self, problem: str) -> str:
        clean_problem = self._preprocess(problem)
        
        try:
            if "=" in clean_problem:
                left, right = clean_problem.split("=")
                eq = sympy.Eq(sympy.sympify(left), sympy.sympify(right))
                symbols = list(eq.free_symbols)
                
                if not symbols:
                    return "Верно" if sympy.sympify(left) == sympy.sympify(right) else "Неверно"
                
                solution = sympy.solve(eq, symbols[0])
                
                # Красивый вывод
                if not solution:
                    return "∅ (Нет решений)"
                return f"{symbols[0]} = {solution}"
            
            else:
                expr = sympy.sympify(clean_problem)
                result = sympy.simplify(expr)
                return str(result)

        except Exception as e:
            # Если SymPy упал, возвращаем оригинальную ошибку для отладки
            raise ValueError(f"Не удалось разобрать: {clean_problem}. Ошибка: {e}")