"""
给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数。计算并返回该研究者的 h 指数。

h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （n 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。且其余的 n - h 篇论文每篇被引用次数 不超过 h 次。

例如：某人的 h 指数是 20，这表示他已发表的论文中，每篇被引用了至少 20 次的论文总共有 20 篇。

提示：如果 h 有多种可能的值，h 指数 是其中最大的那个
"""
from typing import List
import collections


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """排序法"""
        n = len(citations)
        citations.sort()
        for i in range(n):
            h = n - i  # 被引用次数 >= citations[i] 的有 h 篇
            if citations[i] >= h:
                return h
        return 0

    def hIndex2(self, citations: List[int]) -> int:
        """计数法"""
        n = len(citations)
        counter = [0] * (n+1)
        for num in citations:
            if num >= n:
                counter[n] += 1
            else:
                counter[num] += 1
        # print(counter)
        total = 0
        for i in range(n,-1,-1):
            total += counter[i]
            if total >= i:
                return i
        return 0


if __name__ == '__main__':
    # citations = [3,0,6,1,5]
    citations = [1,3,5,7,8,9,10]
    # citations = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(Solution().hIndex2(citations))
