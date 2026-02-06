from src.solvers.symbolic import SymbolicSolver

def test_linear_equation():
    solver = SymbolicSolver()
    # 2x = 10 -> x = 5
    result = solver.solve("2*x = 10")
    assert "5" in result

def test_simplification():
    solver = SymbolicSolver()
    # x + x = 2x
    assert str(solver.solve("x + x")) == "2*x"

def test_quadratic():
    solver = SymbolicSolver()
    # x^2 - 4 = 0 -> x = -2, 2
    result = solver.solve("x^2 - 4 = 0")
    assert "-2" in result and "2" in result