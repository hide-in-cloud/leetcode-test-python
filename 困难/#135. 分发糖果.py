"""
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

你需要按照以下要求，帮助老师给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
评分更高的孩子必须比他两侧的邻位孩子获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？
"""
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        """O(1)空间"""
        n = len(ratings)
        ret = 1
        inc, dec, pre = 1, 0, 1
        for i in range(1, n):
            if ratings[i] >= ratings[i-1]:
                dec = 0
                pre = 1 if ratings[i] == ratings[i-1] else pre + 1
                ret += pre
                inc = pre  # 递增序列长度
            else:
                dec += 1
                if dec == inc:  # 递减长度等于递增长度时，把递增最后一个数加入到递减序列中
                    dec += 1
                ret += dec
                pre = 1
        return ret

    def candy2(self, ratings: List[int]) -> int:
        """贪心, 从左到右,再从右到左"""
        n = len(ratings)
        candis = [1] * n

        for i in range(n-1):
            if ratings[i] < ratings[i + 1]:
                candis[i + 1] = candis[i] + 1

        for i in range(n-1,0,-1):
            if ratings[i-1] > ratings[i] and candis[i] + 1 > candis[i-1]:
                candis[i-1] = candis[i] + 1  # 第二次更新的值需要大于第一次更新的值

        print(candis)
        return sum(candis)


if __name__ == '__main__':
    candyType = [1,6,10,8,7,3,2]  # 1+2+5+4+3+2+1 = 18
    # candyType = [1,0,2,3,3,3,0,2,1]  # 2+1+2+3+1+2+1+2+1=15
    # candyType = [1,3,4,5,2]  # 1+2+3+4+1=11
    print(Solution().candy(candyType))
