import pytest
from src.solvers.arithmetic import ArithmeticSolver

def test_simple_addition():
    solver = ArithmeticSolver()
    assert solver.solve("2 + 2") == 4.0

def test_complex_expression():
    solver = ArithmeticSolver()
    assert solver.solve("(10 * 2) + 5") == 25.0

def test_division():
    solver = ArithmeticSolver()
    assert solver.solve("10 / 2") == 5.0

def test_invalid_input():
    solver = ArithmeticSolver()
    with pytest.raises(ValueError):
        solver.solve("2 + x") # x не разрешен в арифметике пока что