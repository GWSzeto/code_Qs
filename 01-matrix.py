# 542. 01 Matrix

class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        dist_matrix = [[10000 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        # from top-bottom/left-right
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    dist_matrix[row][col] = 0
                if row > 0:
                    dist_matrix[row][col] = min(dist_matrix[row][col], dist_matrix[row - 1][col] + 1)
                if col > 0:
                    dist_matrix[row][col] = min(dist_matrix[row][col], dist_matrix[row][col - 1] + 1)
        
        # from bottom-top/right-left
        for row in range(len(matrix) - 1, -1, -1):
            for col in range(len(matrix[row]) - 1, -1, -1):
                if row < len(matrix) - 1:
                    dist_matrix[row][col] = min(dist_matrix[row][col], dist_matrix[row + 1][col] + 1)
                if col < len(matrix[row]) - 1:
                    dist_matrix[row][col] = min(dist_matrix[row][col], dist_matrix[row][col + 1] + 1)
        
        return dist_matrix
                    