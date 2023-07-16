"""
在 MATLAB 中，有一个非常有用的函数 reshape ，它可以将一个 m x n 矩阵重塑为另一个大小不同（r x c）的新矩阵，但保留其原始数据。

给你一个由二维数组 mat 表示的 m x n 矩阵，以及两个正整数 r 和 c ，分别表示想要的重构的矩阵的行数和列数。

重构后的矩阵需要将原始矩阵的所有元素以相同的 行遍历顺序 填充。

如果具有给定参数的 reshape 操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵
"""
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        """先转为一维数组,再按照行列划分"""
        n = len(mat) * len(mat[0])
        if r * c != n:
            return mat
        ans = []
        nums = []
        for i in range(len(mat)):
            nums.extend(mat[i])
        for i in range(0, n, c):
            ans.append(nums[i:i+c])
        return ans

    def matrixReshape2(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        """逐个添加"""
        m, n = len(mat), len(mat[0])
        if r*c != m*n:
            return mat
        if c == n:
            return mat
        ans = []
        row = []
        count = 0
        for i in range(m):
            for j in range(n):
                row.append(mat[i][j])
                count += 1
                if count == c:
                    ans.append(row)
                    row = []
                    count = 0
        return ans

    def matrixReshape3(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        """ 二维数组的一维表示, (i,j) → i×n+j """
        m, n = len(mat), len(mat[0])
        if r * c != m * n:
            return mat
        ans = [[0] * c for _ in range(r)]
        for x in range(m*n):
            ans[x // c][x % c] = mat[x // n][x % n]
        return ans


if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    r = 2
    c = 6
    print(Solution().matrixReshape3(matrix, r, c))
