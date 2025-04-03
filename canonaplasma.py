import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def initialize_grid(grid_size):
    grid = np.zeros(grid_size, dtype=int)
    
    # Position de départ du canon à planeur (Gosper Glider Gun)
    gun = [
        (5, 1), (5, 2), (6, 1), (6, 2),
        (5, 11), (6, 11), (7, 11), (4, 12), (8, 12), (3, 13), (9, 13),
        (3, 14), (9, 14), (6, 15), (4, 16), (8, 16), (5, 17), (6, 17), (7, 17), (6, 18),
        (3, 21), (4, 21), (5, 21), (3, 22), (4, 22), (5, 22), (2, 23), (6, 23),
        (1, 25), (2, 25), (6, 25), (7, 25),
        (3, 35), (4, 35), (3, 36), (4, 36)
    ]
    
    for cell in gun:
        grid[cell] = 1
    
    return grid

def update(grid):
    neighbors = sum(np.roll(np.roll(grid, i, 0), j, 1)
                    for i in (-1, 0, 1) for j in (-1, 0, 1) if (i, j) != (0, 0))
    return (neighbors == 3) | (grid & (neighbors == 2))

def animate(frame, img, grid):
    grid[:] = update(grid)
    img.set_array(grid)
    return img,

def main():
    grid_size = (40, 50)  # Taille de la grille
    grid = initialize_grid(grid_size)
    
    fig, ax = plt.subplots()
    img = ax.imshow(grid, cmap='gray_r')
    ax.set_xticks([])
    ax.set_yticks([])
    
    ani = animation.FuncAnimation(fig, animate, fargs=(img, grid), interval=100, blit=True)
    plt.show()

if __name__ == "__main__":
    main()