"""
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

进阶：
一个直观的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个仅使用常量空间的解决方案吗？
"""
from typing import List


class Solution:
    def setZeroes2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows_zero = set()
        columns_zero = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows_zero.add(i)
                    columns_zero.add(j)
        for r in range(m):
            for c in range(n):
                if r in rows_zero or c in columns_zero:
                    matrix[r][c] = 0

        for r in range(m):
            print(matrix[r])

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """标记法"""
        m, n = len(matrix), len(matrix[0])
        rows = set()
        columns = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)
        for r in rows:
            for c in range(n):
                matrix[r][c] = 0
        for r in range(m):
            for c in columns:
                matrix[r][c] = 0

        for r in range(m):
            print(matrix[r])

    def setZeroes3(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """标记每一行每一列的第一个元素"""
        row = len(matrix)
        col = len(matrix[0])
        row0_flag = False
        col0_flag = False
        # 预处理
        # 找第一行是否有0
        for j in range(col):
            if matrix[0][j] == 0:
                row0_flag = True
                break
        # 第一列是否有0
        for i in range(row):
            if matrix[i][0] == 0:
                col0_flag = True
                break

        # 把第一行或者第一列作为 标志位
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        # print(matrix)
        # 置0
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 复原
        if row0_flag:
            for j in range(col):
                matrix[0][j] = 0
        if col0_flag:
            for i in range(row):
                matrix[i][0] = 0


if __name__ == '__main__':
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print(Solution().setZeroes(matrix))
