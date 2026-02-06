from src.solvers.calculus import CalculusSolver
from src.solvers.symbolic import SymbolicSolver

def test_implicit_multiplication():
    # Проверяем, что 2x работает
    solver = SymbolicSolver()
    result = solver.solve("2x = 10")
    assert "5" in result

def test_derivative():
    solver = CalculusSolver()
    # d/dx (x^2) = 2x
    assert str(solver.solve("diff(x**2, x)")) == "2*x"

def test_integral():
    solver = CalculusSolver()
    # int(2x) dx = x^2
    assert str(solver.solve("integrate(2*x, x)")) == "x**2"