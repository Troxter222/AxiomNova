import time
from src.utils.generator import MathGenerator
from main import select_solver

def run_training_session(iterations=20):
    print("=== AxiomNova: TRAINING MODE STARTED ===")
    print(f"Generating {iterations} unique problems...\n")
    
    generator = MathGenerator()
    score = 0
    errors = []

    for i in range(1, iterations + 1):
        # 1. Генерируем уникальную задачу
        problem = generator.get_random_problem()
        
        print(f"Task #{i}: {problem}", end=" ... ")
        
        try:
            # 2. Выбираем решатель
            solver = select_solver(problem)
            
            # 3. Решаем
            # Замеряем время "размышления"
            start_time = time.time()
            result = solver.solve(problem)
            end_time = time.time()
            
            print(f"✅ OK ({end_time - start_time:.4f}s) -> Result: {result}")
            score += 1
            
        except Exception as e:
            print("❌ FAIL")
            errors.append((problem, str(e)))

    # Итоги сессии
    print("\n" + "="*40)
    print("Training Complete.")
    print(f"Accuracy: {score}/{iterations} ({(score/iterations)*100}%)")
    
    if errors:
        print("\nFailed Cases (Needs fixing):")
        for p, err in errors:
            print(f"- Task: {p} | Error: {err}")
    else:
        print("\n🚀 PERFECT RUN! System is stable.")
    print("="*40)

if __name__ == "__main__":
    # Запускаем 20 случайных тестов
    run_training_session(20)