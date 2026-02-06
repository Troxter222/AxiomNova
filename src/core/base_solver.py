from abc import ABC, abstractmethod
import re
from typing import Any

class BaseSolver(ABC):
    """
    Абстрактный базовый класс.
    Теперь содержит общую логику обработки текста для всех модулей.
    """
    
    @abstractmethod
    def solve(self, problem: str) -> Any:
        pass

    @abstractmethod
    def get_solver_type(self) -> str:
        pass

    def _preprocess(self, problem: str) -> str:
        """
        Общий метод очистки ввода для всех наследников.
        Превращает '2x^2' -> '2*x**2'.
        """
        # 1. Заменяем ^ на **
        problem = problem.replace("^", "**")
        
        # 2. Вставляем * между цифрой и буквой (2x -> 2*x)
        problem = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', problem)
        
        # 3. Вставляем * между цифрой и скобкой (2( -> 2*()
        problem = re.sub(r'(\d)(\()', r'\1*\2', problem)
        
        # 4. Вставляем * между скобкой и буквой ()x -> ()*x)
        problem = re.sub(r'(\))([a-zA-Z])', r'\1*\2', problem)
        
        # 5. Вставляем * между скобками )( -> )*(
        problem = re.sub(r'(\))(\()', r'\1*\2', problem)
        
        return problem