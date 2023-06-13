
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# MAIN
# set ON to equal to 255 and OFF to 0
ON = 255
OFF = 0

N = 101

def init_grid():
    grid = np.random.choice([0,255], N*N).reshape(N,N)
    return grid

# define Conway's rules
def conway(current, total):    # current is the value of the current cell being evaluated and total is the number of neighbours that are on around the current cell
    if current == ON: 
        if total < 2 or total > 3:
            current = OFF
    else:
        if total == 3:
            current = ON
    return current

# define update function which returns the new grid after Conway's rules have been implemented
def update(frame, img, grid, N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = int((grid[(i-1)%N, j] + grid[(i+1)%N, j]
                         + grid[i, (j-1)%N] + grid[i, (j+1)%N]
                         + grid[(i-1)%N, (j-1)%N] + grid[(i+1)%N, (j-1)%N]
                         + grid[(i-1)%N, (j+1)%N] + grid[(i+1)%N, (j+1)%N])/255)   # total counts the number of the eight neighbours that are ON
            newGrid[i][j] = conway(grid[i][j], total)
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return newGrid

def main():
    grid = init_grid()
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N))
    plt.show()
    

if __name__ == '__main__':
    main()

