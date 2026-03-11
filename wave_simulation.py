import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

from clawpack import pyclaw # type: ignore
from clawpack import riemann # type: ignore


def initial_condition(state):
    x, y = state.grid.p_centers
    r2 = (x-0.5)**2 + (y-0.5)**2
    state.q[0,:,:] = 1 + 0.5*np.exp(-100*r2)   # water height bump
    state.q[1,:,:] = 0                         # x momentum
    state.q[2,:,:] = 0                         # y momentum


solver = pyclaw.ClawSolver2D(riemann.shallow_roe_with_efix_2D)

solver.limiters = pyclaw.limiters.tvd.MC
solver.bc_lower[0] = pyclaw.BC.extrap
solver.bc_upper[0] = pyclaw.BC.extrap
solver.bc_lower[1] = pyclaw.BC.extrap
solver.bc_upper[1] = pyclaw.BC.extrap


x = pyclaw.Dimension(0.0, 1.0, 100, name='x')
y = pyclaw.Dimension(0.0, 1.0, 100, name='y')
domain = pyclaw.Domain([x,y])


state = pyclaw.State(domain,3)
state.problem_data['grav'] = 1.0

initial_condition(state)


claw = pyclaw.Controller()
claw.solution = pyclaw.Solution(state,domain)
claw.solver = solver
claw.tfinal = 0.5
claw.num_output_times = 20
claw.keep_copy = True

claw.run()


for frame in claw.frames:
    plt.clf()
    h = frame.state.q[0]
    plt.imshow(h, origin='lower', cmap='viridis')
    plt.colorbar(label="Water Height")
    plt.title(f"Time = {frame.t:.3f}")
    plt.pause(0.1)

plt.show()