"""
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        right, bottom, left, top = n - 1, n - 1, 0, 0,
        k, total = 1, n*n
        while k <= total:
            for j in range(left, right + 1):
                matrix[top][j] = k
                k += 1
            top += 1
            for i in range(top, bottom + 1):
                matrix[i][right] = k
                k += 1
            right -= 1
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = k
                k += 1
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = k
                k += 1
            left += 1
        return matrix

    def generateMatrix2(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]  # 模拟四个方向
        row = col = dirIdx = 0
        for i in range(n*n):
            matrix[row][col] = i+1
            dx, dy = dirs[dirIdx]
            r, c = row + dx, col + dy
            if r < 0 or r >= n or c < 0 or c >= n or matrix[r][c] > 0:
                dirIdx = (dirIdx+1) % 4  # 顺时针旋转至下一个方向
                dx, dy = dirs[dirIdx]
            row, col = row + dx, col + dy
        return matrix


if __name__ == '__main__':
    n = 4
    """
    [
    [1, 2, 3, 4],
    [12,13,14,5],
    [11,16,15,6],
    [10,9, 8, 7],
    ]
    """
    print(Solution().generateMatrix2(n))
