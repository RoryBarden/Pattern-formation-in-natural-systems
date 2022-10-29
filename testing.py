import numpy as np
import pde

grid = pde.UnitGrid([256, 256])
state = pde.ScalarField.random_uniform(grid, rng=np.random.default_rng(12345))  # Seedable random state generator


def reaction_kinetics(u_value: pde.fields.scalar.ScalarField):
    return u_value  # Testing with kinetics that do nothing


eq = pde.PDE({"u": "diffusivity * laplace(u) + reaction_kinetics(u)"},
             user_funcs={"reaction_kinetics": reaction_kinetics}, consts={"diffusivity": 0.5})
result = eq.solve(state, t_range=5).plot()
