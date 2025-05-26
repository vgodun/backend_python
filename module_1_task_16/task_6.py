grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(grid)):
    for k in range(len(grid[i])):
        if grid[i][k] % 2 == 0:
            grid[i][k] *= 2
        else:
            grid[i][k] = 0


for row in grid:
    print(row)