from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix is None: return matrix
        if len(matrix) == 0: return matrix
        
        n = len(matrix)
        temp_matrix = [ [] for i in range(n)]

        for i in range(n):
            x = n - 1
            for j in range(n):
                temp_matrix[i].append(matrix[x][i])
                x -= 1
        
        for i in range(n):
            for j in range(n):
                matrix[i][j] = temp_matrix[i][j]

    