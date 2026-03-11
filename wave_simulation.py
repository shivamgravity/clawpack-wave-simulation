import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
from matplotlib import cm # type: ignore
from mpl_toolkits.mplot3d import Axes3D # type: ignore

from clawpack import pyclaw # type: ignore
from clawpack import riemann # type: ignore


def initial_condition(state):
    x, y = state.grid.p_centers
    r2 = (x-0.5)**2 + (y-0.5)**2
    state.q[0,:,:] = 1 + 0.5*np.exp(-100*r2)
    state.q[1,:,:] = 0
    state.q[2,:,:] = 0


solver = pyclaw.ClawSolver2D(riemann.shallow_roe_with_efix_2D)
solver.limiters = pyclaw.limiters.tvd.MC

solver.bc_lower[0] = pyclaw.BC.extrap
solver.bc_upper[0] = pyclaw.BC.extrap
solver.bc_lower[1] = pyclaw.BC.extrap
solver.bc_upper[1] = pyclaw.BC.extrap


x = pyclaw.Dimension(0.0,1.0,100,name='x')
y = pyclaw.Dimension(0.0,1.0,100,name='y')

domain = pyclaw.Domain([x,y])

state = pyclaw.State(domain,3)
state.problem_data['grav'] = 1.0

initial_condition(state)


claw = pyclaw.Controller()
claw.solution = pyclaw.Solution(state,domain)
claw.solver = solver
claw.tfinal = 2.0
claw.num_output_times = 200
claw.keep_copy = True

claw.run()


# Prepare grid for 3D plotting
X, Y = state.grid.p_centers


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


for frame in claw.frames:

    ax.clear()

    h = frame.state.q[0]

    surf = ax.plot_surface(
        X, Y, h,
        cmap=cm.viridis,
        linewidth=0,
        antialiased=True
    )
    ax.view_init(elev=35, azim=frame.t*50) # Rotate the view over time
    ax.set_zlim(0.95,1.1) # Set consistent z-axis limits for better visualization
    ax.set_title(f"Wave Simulation — Time {frame.t:.2f}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Water Height")

    plt.pause(0.1)

plt.show()