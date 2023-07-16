"""
给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """滚动数组"""
        row = [0] * (rowIndex+1)
        row[0] = 1
        for i in range(1, rowIndex+1):
            for j in range(i,0,-1):
                row[j] += row[j-1]
        return row

    def getRow2(self, rowIndex: int) -> List[int]:
        """滚动数组"""
        pre = []
        for i in range(rowIndex + 1):
            cur = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    cur.append(1)
                else:
                    cur.append(pre[j - 1] + pre[j])
            pre = cur
        return pre


if __name__ == '__main__':
    rowIndex = 4
    print(Solution().getRow(rowIndex))
