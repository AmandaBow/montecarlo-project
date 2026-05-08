
# import libraries
import numpy as np
import random 
from graphs import plot_results

# set seed to make code reproducable
random.seed(42)

def random_walk(grid_size_x = 101, grid_size_y = 101, N = 200, steps = 1000, n_trails = 5):
    # center
    center_x = grid_size_x // 2
    center_y = grid_size_y // 2
    # all particles start center
    x = [center_x] * N
    y = [center_y] * N

    # heat accumulation grid
    heat = np.zeros((grid_size_y, grid_size_x))

    # store trajectories for a few particles
    traj_x = [[center_x] for _ in range(n_trails)]
    traj_y = [[center_y] for _ in range(n_trails)]

    # particle movement
    for step in range(steps):

        # move every particle
        for i in range(N):

            move_accepted = False

            # rejects invalid moves
            while not move_accepted:

                direction = random.choice(["up", "down", "right", "left"])

                # positions after choice
                dx, dy = x[i], y[i]

                if direction == "up":
                    dy += 1
                elif direction == "down":
                    dy -= 1
                elif direction == "right":
                    dx += 1
                elif direction == "left":
                    dx -= 1

                # check bounds
                if 0 <= dx < grid_size_x and 0 <= dy < grid_size_y:

                    # accept move
                    x[i] = dx
                    y[i] = dy

                    move_accepted = True

            heat[y[i], x[i]] += 1


        # store trajectories for selected particles
        for j in range(n_trails):

            traj_x[j].append(x[j])
            traj_y[j].append(y[j])

    return heat, traj_x, traj_y, grid_size_x, grid_size_y


if __name__ == "__main__":

    heat, traj_x, traj_y, grid_size_x, grid_size_y = random_walk()

    plot_results(heat, traj_x, traj_y, grid_size_x, grid_size_y)


