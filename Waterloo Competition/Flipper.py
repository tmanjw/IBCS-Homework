line=input()

grid=[[1,2],[3,4]]

for i in line:
    if i=="V":
        for i in range(2):
            grid[i] = [grid[i][1], grid[i][0]]
    else:
        grid = [grid[1], grid[0]]

for i in grid:
    print(i[0],i[1])