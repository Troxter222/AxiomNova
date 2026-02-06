import random

class MathGenerator:
    """
    Генератор процедурных задач для тренировки ИИ.
    Создает задачи, которые система еще никогда не видела.
    """
    
    def generate_arithmetic(self, difficulty=1) -> str:
        ops = ['+', '-', '*', '/']
        if difficulty == 1:
            # Простые: 5 + 3
            return f"{random.randint(1, 100)} {random.choice(ops)} {random.randint(1, 100)}"
        else:
            # Сложные: (5 + 3) * 12
            a, b, c = random.randint(1, 50), random.randint(1, 50), random.randint(1, 10)
            return f"({a} {random.choice(ops)} {b}) * {c}"

    def generate_algebra(self) -> str:
        # Генерирует уравнения вида ax + b = c
        a = random.randint(2, 10)
        b = random.randint(1, 50)
        c = random.randint(50, 200)
        # Иногда делаем 2x, иногда 2*x (проверяем парсер)
        var_part = f"{a}x" if random.random() > 0.5 else f"{a}*x"
        return f"{var_part} + {b} = {c}"

    def generate_calculus(self) -> str:
        # Генерирует diff(x^n) или integrate(x^n)
        power = random.randint(2, 9)
        func = f"x^{power}"
        cmd = random.choice(['diff', 'integrate'])
        return f"{cmd}({func})"

    def get_random_problem(self) -> str:
        """Возвращает случайную задачу любого типа"""
        category = random.choice(['arithmetic', 'algebra', 'calculus'])
        
        if category == 'arithmetic':
            return self.generate_arithmetic(difficulty=random.randint(1, 2))
        elif category == 'algebra':
            return self.generate_algebra()
        else:
            return self.generate_calculus()