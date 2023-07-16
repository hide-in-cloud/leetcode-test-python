"""
给定一个初始元素全部为 0，大小为 m*n 的矩阵 M 以及在 M 上的一系列更新操作。

操作用二维数组表示，其中的每个操作用一个含有两个正整数 a 和 b 的数组表示，含义是将所有符合 0 <= i < a 以及 0 <= j < b 的元素 M[i][j] 的值都增加 1。

在执行给定的一系列操作后，你需要返回矩阵中含有最大整数的元素个数。
"""
from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        """巧妙解法,最小ops矩阵"""
        if not ops:
            return m * n
        ziped = list(zip(*ops))
        return min(ziped[0]) * min(ziped[1])

    def maxCount1(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        min_a, min_b = ops[0]
        for a, b in ops:
            min_a = min(min_a, a)
            min_b = min(min_b, b)
        return min_a * min_b

    def maxCount2(self, m: int, n: int, ops: List[List[int]]) -> int:
        """暴力算法"""
        nums = [[0]*n for _ in range(m)]
        for rows, columns in ops:
            for r in range(rows):
                for c in range(columns):
                    nums[r][c] += 1
        # for r in range(m):
        #     print(nums[r])
        maxNum = nums[0][0]
        count = 0
        for r in range(m):
            count += nums[r].count(maxNum)
        return count


if __name__ == '__main__':
    m = 5
    n = 5
    operations = [[5, 4], [4, 2], [4, 3], [3, 4], [2, 4]]
    # operations = []
    print(Solution().maxCount2(m, n, operations))
