import sys
import re
from src.solvers.arithmetic import ArithmeticSolver
from src.solvers.symbolic import SymbolicSolver

def select_solver(problem: str):
    """
    Фабричный метод: выбирает решатель на основе сложности задачи.
    """
    # Если есть буквы (x, y, a...) или знак =, это Алгебра
    if re.search(r'[a-zA-Z=]', problem):
        return SymbolicSolver()
    else:
        # Иначе считаем это простой арифметикой
        return ArithmeticSolver()

def main():
    print("=== AxiomNova: Math Intelligence System ===")
    print("Поддерживается: Арифметика (+-*/) и Алгебра (x^2 + 5 = 10)")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("\nВведите задачу: ")
        
        if user_input.lower() in ['exit', 'quit']:
            print("Shutting down AxiomNova...")
            break
            
        try:
            # 1. Выбираем правильный "мозг"
            solver = select_solver(user_input)
            
            # 2. Решаем
            print(f"[DEBUG] Using: {solver.get_solver_type()}")
            result = solver.solve(user_input)
            
            print(f"✅ Решение: {result}")
            
        except Exception as e:
            print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    main()