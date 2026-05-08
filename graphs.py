
import numpy as np
import matplotlib.pyplot as plt


def plot_results(heat, traj_x, traj_y, grid_size):

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    center = grid_size // 2


    # -------------------------------
    # TRAJECTORY PLOT
    # -------------------------------

    for i in range(len(traj_x)):

        ax1.plot(
            traj_x[i],
            traj_y[i],
            lw=0.5,
            alpha=0.6
        )

        ax1.scatter(
            traj_x[i][-1],
            traj_y[i][-1],
            s=15
        )

    ax1.scatter(
        center,
        center,
        color="black",
        marker="*",
        s=100,
        label="Start"
    )

    ax1.set_title("Random Walk Trajectories")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")

    ax1.set_xlim(0, grid_size - 1)
    ax1.set_ylim(0, grid_size - 1)

    ax1.grid(alpha=0.3)
    ax1.legend()


    # -------------------------------
    # HEAT MAP
    # -------------------------------

    log_heat = np.log1p(heat)

    im = ax2.imshow(
        log_heat,
        origin="lower",
        cmap="inferno"
    )

    ax2.set_title("Monte Carlo Heat Diffusion")
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")

    ax2.scatter(
        center,
        center,
        color="white",
        marker="*",
        s=100
    )

    cbar = plt.colorbar(im, ax=ax2)
    cbar.set_label("log(1 + visits)")

    plt.tight_layout()
    plt.show()