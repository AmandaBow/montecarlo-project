# Monte Carlo Method for Heat Diffusion
The purpose of this project is to explore how prediction methods such as random walks and Monte Carlo simulations are able to predict the flow of heat. Traditionally, heat diffusion is expressed as the heat equation, a partial differential equation that depicts how temperature evolves over time:

$$
\frac{\partial T}{\partial t} = \alpha \nabla^2 T
$$

Instead of solving for the equation direclty, this poject will simulate the stochastic motion of particles to approximate the physical behavior of heat diffusion. This project aims to demonstrate that a probabilistic model can accuratly replicate the behavior of heat diffusion.

Each particle represents a small packet of thermal energy, and its motion models the microscopic collisions responsible for heat flow. Over time, the collective motion of many particles produces a macroscopic heat distribution, which is compared to expected diffusion behavior.

## System Setup
- The system is a 2D square grid representing a uniform material.
- All particles start at the center of the grid, representing an initial localized heat source.
- The grid boundaries are treated as reflecting walls, meaning particles cannot leave the system of the grid.

### Monte Carlo / Random Walk Method
Each particle evolves according to a **random walk process**:

1. At each time step, a direction (up, down, right, left) is randomly chosen

2. The particle attempts to move one unit in that direction.

3. If the move stays within bounds, it is accepted; otherwise, it is rejected and another direction is chosen.

4. Each particle’s position contributes to a heat accumulation grid, where every visit increases the local temperature count.

Over many particles and time steps, this produces a statistical approximation of the heat equation solution.

## Organization
main.py - contains the random walk simulation

graphs.py - generates trajectory plots and heat maps

data - a folder that will store simutlation data (will be used for deeper analysis)

assets - a folder that will contain output images and vizualizations

(subject to change)

## Running the Code
The two main important files are **main.py** and **graphs.ipynb**. Inorder to execute this code on your engine you can either clone or fork the repository, which you can then access via Codespaces. 

Once you have done that, run this in terminal: 
python main.py

Then, go to the notebook **graphs.ipynb** and run all. This should produce a heatmap showing heat diffusion behavior and trajectory plot of a few particle paths. 

You can play around with the parameters inside of the random_walk() function (located in **main.py**) and produce differrent temperature maps. You will probably notice the increasing the number of particles improves the smoothness of the heatmap.

## Resources
_[How can a random walk solve a difficult mathematical problem?](https://medium.com/@snp.kriss/how-can-a-random-walk-solve-a-difficult-mathematical-problem-f738528d169a) by MCMC Addict_ -  example of how andom walk is used for heat diffusion

_Mathematical Methods in the Physical Sciences by Mary L. Boas_ - this textbook goes over PDEs and would be useful for refrencening the 2D heat diffusion equation

_Statistical and Thermal Physics: With Computer Applications by Harvey Gould and Jan Tobochnik_ - this textbook breifly goes over how a random walk can be simlated with Monte Carlo

(a few more need to be added)

## Project Timeline
Week 1 

+ Finalize Project idea
+ Set up Github directory
  
Week 2

+ Attempt random walk simulation for a single pariticle
+ Plot path of particle
  
Week 3 

+ Create a 2D grid that will contain multiple particles
+ Create simulation for multiple particles
  
Week 4 

+ Create heatmap and trajectory plots for multpiple particle walks

Week 5
+ Do PDE heat diffusion simulation
+ Do convergence graph

Week 6
+ Make plots comparing random walk monte carlo to heat diffusion equation
+ Create animations

Week 7

+ FInalize everything

(subject to change)

I am currently done with week 4. I have to now create a PDE solver and a convergence graph to compare the random walk simulation to and see under what conditions the simulation becomes accurate (if at all). 

## LLM Disclosure
The use of LLM such as ChatGPT and Claude.ai were used as s an assistant tools to improve the speed of simulation, debug code, and assisted the creation of heatmap vizulatizations and improvement of trajectory plots.
