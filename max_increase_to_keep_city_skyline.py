class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        row_length = len(grid[0])
        col_length = len(grid)
        # store rows along the length of row_length and store columns along everything after row_length
        max_heights = [0]*(row_length + col_length)

        for row_index in range(row_length):
            for col_index in range(col_length):
                if grid[row_index][col_index] > max_heights[row_index]:
                    max_heights[row_index] = grid[row_index][col_index]
                if grid[row_index][col_index] > max_heights[row_length + col_index]:
                    max_heights[row_length + col_index] = grid[row_index][col_index]
        
        total_sum_increased = 0

        for row_index in range(row_length):
            for col_index in range(col_length):
                total_sum_increased += (min(max_heights[row_index], max_heights[row_length + col_index]) - grid[row_index][col_index])
        
        return total_sum_increased