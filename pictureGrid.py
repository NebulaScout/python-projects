# This program creates a character picture grid using 'O' and '.'


# define size of the picture
WIDTH = 9
HEIGHT = 6

# Initialize the grid with empty spaces
grid = [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]

# draw the picture
for i in [2,3,5,6]:
    grid[0][i] = 'O'
for i in range(1, 8):
    grid[1][i] = grid[2][i] = 'O'
for i in range(2, 7):
    grid[3][i] = 'O'
for i in range(3, 6):
    grid[4][i] = 'O'

grid[5][4] = 'O'

# output the picture
for row in grid:
    print(''.join(row))


        