import streamlit as st
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
from matplotlib import cm # type: ignore
from clawpack import pyclaw, riemann # type: ignore


st.title("Interactive Wave Simulation (Clawpack) 🌊")


# Sidebar controls
grid_size = st.sidebar.slider("Grid Resolution", 50, 200, 100)
disturbance_strength = st.sidebar.slider("Disturbance Strength", 0.1, 1.0, 0.5)
simulation_time = st.sidebar.slider("Simulation Time", 0.1, 1.0, 0.5)


def run_simulation(grid_size, disturbance_strength, simulation_time):

    solver = pyclaw.ClawSolver2D(riemann.shallow_roe_with_efix_2D)

    solver.bc_lower[0] = pyclaw.BC.extrap
    solver.bc_upper[0] = pyclaw.BC.extrap
    solver.bc_lower[1] = pyclaw.BC.extrap
    solver.bc_upper[1] = pyclaw.BC.extrap

    x = pyclaw.Dimension(0.0,1.0,grid_size,name='x')
    y = pyclaw.Dimension(0.0,1.0,grid_size,name='y')

    domain = pyclaw.Domain([x,y])
    state = pyclaw.State(domain,3)

    state.problem_data['grav'] = 1.0

    X,Y = state.grid.p_centers

    r2 = (X-0.5)**2 + (Y-0.5)**2
    state.q[0,:,:] = 1 + disturbance_strength*np.exp(-100*r2)
    state.q[1,:,:] = 0
    state.q[2,:,:] = 0

    claw = pyclaw.Controller()
    claw.solution = pyclaw.Solution(state,domain)
    claw.solver = solver
    claw.tfinal = simulation_time
    claw.num_output_times = 10
    claw.keep_copy = True

    claw.run()

    return claw.frames, X, Y


if st.button("Run Simulation"):

    with st.spinner("Running simulation..."):

        # ax.set_xlabel("X")
        # ax.set_ylabel("Y")
        # ax.set_zlabel("Water Height")

        frames, X, Y = run_simulation(grid_size, disturbance_strength, simulation_time)

        plot_area = st.empty()

        for frame in frames:

            h = frame.state.q[0]

            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            ax.plot_surface(X, Y, h, cmap=cm.viridis)

            ax.set_zlim(0.95,1.1)
            ax.set_title(f"Wave Simulation — Time {frame.t:.2f}")

            plot_area.pyplot(fig)