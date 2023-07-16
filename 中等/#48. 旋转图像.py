"""
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """每四个一次旋转"""
        n = len(matrix)
        for i in range(n // 2):
            end = n - 1 - i
            for j in range(i, end):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[end][n - 1 - j]
                matrix[end][n - 1 - j] = matrix[j][end]
                matrix[j][end] = temp

                # matrix[i][j], matrix[n - 1 - j][i], matrix[end][n - 1 - j], matrix[j][end] \
                #     = matrix[n - 1 - j][i], matrix[end][n - 1 - j], matrix[j][end], matrix[i][j]

        for r in range(n):
            print(matrix[r])

    def rotate2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """用翻转代替旋转"""
        n = len(matrix)
        # 水平翻转
        for i in range(n//2):
            for j in range(n):
                matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]
        # 主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # for r in range(n):
        #     print(matrix[r])


if __name__ == '__main__':
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print(Solution().rotate2(matrix))
