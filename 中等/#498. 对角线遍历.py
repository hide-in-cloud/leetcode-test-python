"""
给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。
"""
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(mat), len(mat[0])
        dirs = [(-1,1), (1,-1)]  # ↗和↙方向
        row = col = dirIdx = 0
        for i in range(m * n):
            ans.append(mat[row][col])
            dx, dy = dirs[dirIdx]
            r, c = row + dx, col + dy
            if dirIdx == 0:  # 右上↗
                if r < 0 or c >= n:  # 右上↗失败
                    if c < n:  # 右方有数
                        dx, dy = 0, 1
                    else:      # 下方有数
                        dx, dy = 1, 0
                    dirIdx = (dirIdx + 1) % 2
            else:            # 左下↙
                if c < 0 or r >= m:  # 左下↙失败
                    if r < m:
                        dx, dy = 1, 0
                    else:
                        dx, dy = 0, 1
                    dirIdx = (dirIdx + 1) % 2
            row, col = row + dx, col + dy
        return ans


if __name__ == '__main__':
    # matrix = [
    #     [1, 2, 3, 4],
    #     [12, 13, 14, 5],
    #     [11, 16, 15, 6],
    #     [10, 9, 8, 7],
    # ]
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(Solution().findDiagonalOrder(matrix))
