from abc import ABC, abstractmethod
from typing import Any

class BaseSolver(ABC):
    """
    Абстрактный базовый класс для всех математических решателей.
    Каждый уровень интеллекта (от арифметики до теорвера) будет наследовать этот класс.
    """
    
    @abstractmethod
    def solve(self, problem: str) -> Any:
        """
        Метод должен принимать задачу в виде строки и возвращать решение.
        """
        pass

    @abstractmethod
    def get_solver_type(self) -> str:
        """Возвращает тип решателя (например, 'Arithmetic', 'Neural', 'Quantum')"""
        pass