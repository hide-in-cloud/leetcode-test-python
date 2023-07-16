"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        rows, columns = len(matrix), len(matrix[0])
        right, bottom, left, top = columns-1, rows-1, 0, 0,
        while left <= right and top <= bottom:
            for j in range(left, right+1):
                ans.append(matrix[top][j])
            top += 1
            for i in range(top, bottom+1):
                ans.append(matrix[i][right])
            right -= 1
            if left <= right and top <= bottom:
                for j in range(right,left-1,-1):
                    ans.append(matrix[bottom][j])
                bottom -= 1
                for i in range(bottom, top-1, -1):
                    ans.append(matrix[i][left])
                left += 1
        return ans

    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res


if __name__ == '__main__':
    # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    matrix = [[2,5],[8,4],[0,-1]]
    print(Solution().spiralOrder(matrix))
