import sys
from src.solvers.arithmetic import ArithmeticSolver

def main():
    print("=== AxiomNova: Math Intelligence System ===")
    print("Type 'exit' to quit.")

    # Инициализация решателя (позже здесь будет логика выбора решателя)
    solver = ArithmeticSolver()
    print(f"Loaded Module: {solver.get_solver_type()}")

    while True:
        user_input = input("\nВведите задачу (например, 2 + 2 * 3): ")
        
        if user_input.lower() in ['exit', 'quit']:
            print("Shutting down AxiomNova...")
            break
            
        try:
            result = solver.solve(user_input)
            print(f"✅ Решение: {result}")
        except ValueError as e:
            print(f"❌ Ошибка: {e}")
            print("💡 AxiomNova пока не умеет это решать. Нужно обучение (следующий этап).")

if __name__ == "__main__":
    main()