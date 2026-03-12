import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import imageio
import os

from clawpack import pyclaw, riemann


def initial_condition(state):
    x, y = state.grid.p_centers
    r2 = (x-0.5)**2 + (y-0.5)**2
    state.q[0,:,:] = 1 + 0.5*np.exp(-100*r2)
    state.q[1,:,:] = 0
    state.q[2,:,:] = 0


solver = pyclaw.ClawSolver2D(riemann.shallow_roe_with_efix_2D)

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
claw.tfinal = 0.5
claw.num_output_times = 20
claw.keep_copy = True

claw.run()


X, Y = state.grid.p_centers

images = []
frame_files = []

os.makedirs("frames", exist_ok=True)


for i, frame in enumerate(claw.frames):

    h = frame.state.q[0]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(X, Y, h, cmap=cm.viridis)

    ax.set_zlim(0.95,1.1)
    ax.set_title(f"Wave Simulation — Time {frame.t:.2f}")

    filename = f"frames/frame_{i}.png"
    plt.savefig(filename)

    frame_files.append(filename)

    plt.close()


for file in frame_files:
    images.append(imageio.imread(file))


imageio.mimsave("simulation_images/demo.gif", images, fps=10)

print("GIF saved as demo.gif")