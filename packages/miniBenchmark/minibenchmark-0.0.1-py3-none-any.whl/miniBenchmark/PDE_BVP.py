import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def solve_2d_wave(nx, ny, c, dx, dy, dt, time_steps, animate=False):
    """
    Solves the 2D wave equation over a specified number of time steps.
    
    Parameters:
        nx, ny: int
            The dimensions of the wave grid.
        c: float
            The wave speed.
        dx, dy: float
            The space step in the x and y directions.
        dt: float
            The time step.
        time_steps: int
            The number of time steps to evolve the system.
        animate: bool, optional
            If True, animates the wave propagation.

    Returns:
        u: ndarray
            The final state of the wave after the specified number of time steps.
    """
    # Stability criterion (CFL condition)
    assert (c * dt / dx)**2 < 1 / 2, "The CFL condition is not met!"

    # Initial conditions
    u = np.zeros((nx, ny))
    u[:int(nx / 8), :int(ny / 8)] = 1  # initial condition

    # Initialize past values (t-1) and future values (t+1) arrays
    u_past = np.copy(u)
    u_future = np.copy(u)

    # Simulation function
    def wave_equation_step(u, u_past):
        u_future = 2 * u - u_past
        u_future[1:-1, 1:-1] = (u_future[1:-1, 1:-1] +
                                 (c * dt / dx)**2 *
                                 (u[2:, 1:-1] - 2 * u[1:-1, 1:-1] + u[:-2, 1:-1]) +
                                 (c * dt / dy)**2 *
                                 (u[1:-1, 2:] - 2 * u[1:-1, 1:-1] + u[1:-1, :-2]))
        return u_future

    if animate:
        # Plot setup for animation
        fig = plt.figure(figsize=(5, 5))
        ax = fig.add_subplot(111)
        ax.set_xlim(0, nx)
        ax.set_ylim(0, ny)
        img = ax.imshow(u, cmap='viridis', vmin=-0.1, vmax=0.1, interpolation='nearest')

        # Animation function
        def animate_step(i):
            nonlocal u, u_past
            u_future = wave_equation_step(u, u_past)
            img.set_array(u_future)
            u_past = u
            u = u_future
            return img,

        # Run animation
        ani = FuncAnimation(fig, animate_step, frames=time_steps, interval=50, blit=True)
        plt.show()
    else:
        # Run simulation without animation
        for _ in range(time_steps):
            u_future = wave_equation_step(u, u_past)
            u_past = u
            u = u_future
    
    return u

# Example usage:



# Original parameters
#c = 1.0   # wave speed, constant
#Lx, Ly = 100.0, 100.0  # physical size of the domain
#nx, ny = 100, 100  # original number of grid points
#dx = Lx / nx  # original spatial resolution
#dy = Ly / ny
#dt = 0.1  # original time step

# New parameters for a finer grid
#factor = 4 # Factor by which to refine the grid
#nx_finer, ny_finer = factor * nx, factor * ny  # new number of grid points
#x_finer = Lx / nx_finer  # new spatial resolution
#dy_finer = Ly / ny_finer  #

# Adjust dt to satisfy the CFL condition for the new finer grid
# The CFL factor for stability must be the same or smaller to satisfy the condition
#cfl_factor = (c * dt / dx)**2
#dt_finer = dt / factor

#solve_2d_wave(nx=nx_finer, ny=ny_finer, c=1.0,
#              dx=dx_finer,dy=dy_finer, dt=dt_finer, time_steps=200, animate=True)

def task_wave_pde_2d(n=100):
    # Original parameters
    c = 1.0   # wave speed, constant
    Lx, Ly = 100.0, 100.0  # physical size of the domain
    nx, ny = 100, 100  # original number of grid points
    dx = Lx / nx  # original spatial resolution
    dy = Ly / ny
    dt = 0.1  # original time step

    # New parameters for a finer grid
    factor = 4 # Factor by which to refine the grid
    nx_finer, ny_finer = factor * nx, factor * ny  # new number of grid points
    dx_finer = Lx / nx_finer  # new spatial resolution
    dy_finer = Ly / ny_finer  

    # Adjust dt to satisfy the CFL condition for the new finer grid
    # The CFL factor for stability must be the same or smaller to satisfy the condition
    cfl_factor = (c * dt / dx)**2
    dt_finer = dt / factor

    solve_2d_wave(nx=nx_finer, ny=ny_finer, c=1.0,
                  dx=dx_finer,dy=dy_finer, dt=dt_finer, time_steps=200, animate=False)

