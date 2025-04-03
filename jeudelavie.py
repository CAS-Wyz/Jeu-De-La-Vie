import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Dimensions de la grille
N = 50

# Initialisation aléatoire de la grille
grid = np.random.choice([0, 1], N*N, p=[0.8, 0.2]).reshape(N, N)

def update(data):
    global grid
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # Calcul du nombre de voisins vivants
            total = (grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                     grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                     grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                     grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])
            # Règles du jeu de la vie
            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = 0
            else:
                if total == 3:
                    newGrid[i, j] = 1
    mat.set_data(newGrid)
    grid = newGrid
    return [mat]

# Configuration de l'affichage
fig, ax = plt.subplots()
mat = ax.matshow(grid, cmap='binary')

# Création de l'animation
ani = animation.FuncAnimation(fig, update, interval=200, save_count=50)

plt.show()
