# Creatify.ai First round interview

# Spiral Matrix
from typing import List

class Solution:
    def sprialMatrixI(self, matrix: List[List[int]]) -> List[int]:
        """
        Given an m x n matrix, return all elements of ther matrix in sprial order.
        """
        if not matrix:
            return []
        
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        result = []

        while(1):
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1
            if top > bottom:
                break
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1
            if right < left:
                break
            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
            if bottom < top:
                break
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            left += 1
            if left > right:
                break
        
        return result


    def sprialMatrixII(self, n: int) -> List[List[int]]:
        """
        Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order.
        """
        matrix = [[0] * n for _ in range(n)]

        start_x, start_y = 0, 0
        loop, mid = n // 2, n // 2
        count = 1

        for offset in range(1, loop+1):
            for i in range(start_y, n - offset):
                matrix[start_x][i] = count
                count += 1
            for i in range(start_x, n - offset):
                matrix[i][n-offset] = count
                count += 1
            for i in range(n-offset, start_y, -1):
                matrix[n - offset][i] = count
                count += 1
            for i in range(n-offset, start_x, -1):
                matrix[i][start_y] = count
                count += 1
            start_x += 1
            start_y += 1
        
        if n % 2 != 0:
            matrix[mid][mid] = count
        
        return matrix
    
