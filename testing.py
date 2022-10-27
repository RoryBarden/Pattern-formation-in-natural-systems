import pde

grid = pde.UnitGrid([256, 256])
state = pde.ScalarField.random_uniform(grid)

eq = pde.DiffusionPDE(diffusivity=0.5)
result = eq.solve(state, t_range=10).plot()
