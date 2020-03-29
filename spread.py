import numpy as np
import math
import random
from matplotlib import pyplot as plt
from IPython.display import clear_output

def viral_spread(population,time,initial,movement):
  

  grid_space=int(math.sqrt(population))

  grid=np.zeros((grid_space,grid_space))

  for i in range(0,initial):

    x0=np.random.randint(0,grid_space-1) 

    y0=np.random.randint(0,grid_space-1)

    grid[x0,y0]=1



  plt.imshow(grid, interpolation='none', vmin=0, vmax=1, aspect='equal')



  ax = plt.gca();

  ax.set_xticks(np.arange(0, grid_space, 1));

  ax.set_yticks(np.arange(0, grid_space, 1));

  ax.set_xticklabels(np.arange(1, grid_space+1, 1));

  ax.set_yticklabels(np.arange(1, grid_space+1, 1));

  spread_chance=[0]*76+[1]*24

  plot_list=[]

  infectioncount=[]

  for a in range(0,time): 

    for i in range(0,grid_space-1):

      for j in range(0,grid_space-1):

        if grid[i,j]==1:

          for a in range(-1,2):
            for b in range (-1,2):
              grid[a+i,b+j] = random.choice(spread_chance)

        
          x_switch=0
          y_switch=0
          x_switch=i+np.random.randint(-movement,movement+1)
          y_switch=j+np.random.randint(-movement,movement+1)
          if x_switch < grid_space-1:
            if x_switch>0:
              if y_switch<grid_space-1:
                if y_switch> 0:
                  grid[x_switch,y_switch]=1
                  grid[i,j]=0



    infectioncount.append(np.count_nonzero(grid))

    plt.figure()

    return plt.imshow(grid, interpolation='none', vmin=0, vmax=1, aspect='equal')

    plot_list.append(plt)

  

#example 10000 population in 3 hours, 2 initial population with the virus, and 20 movements per hour.
viral_spread(10000,3,2,20)



  
