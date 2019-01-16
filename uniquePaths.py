def uniquePaths(m, n):
    dp_grid = [[1 for _ in range(m)] for _ in range(n)]
    for row in range(n):
        for col in range(m):
            if col > 0 and row > 0:
                dp_grid[row][col] = dp_grid[row][col-1] + dp_grid[row-1][col]
            if col > 0  and row == 0:
                dp_grid[row][col] = dp_grid[row][col-1]
            if col == 0 and row > 0:
                dp_grid[row][col] = dp_grid[row-1][col]

    return dp_grid[n-1][m-1]
            
print(uniquePaths(3, 2))
print(uniquePaths(7,3))
