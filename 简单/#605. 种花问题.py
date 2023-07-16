"""
假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给你一个整数数组  flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。
另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false。
"""
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """贪心"""
        count, m, prev = 0, len(flowerbed), -1
        for i in range(m):
            if flowerbed[i] == 1:
                if prev < 0:
                    count += i // 2
                else:
                    count += (i-prev-2) // 2
                if count >= n:
                    return True
                prev = i  # 上一个种花的位置

        if prev < 0:
            count += (m+1) // 2
        else:
            count += (m - prev - 1) // 2
        return count >= n

    def canPlaceFlowers2(self, flowerbed: List[int], n: int) -> bool:
        """防御式编程思想：在 flowerbed 数组两端各增加一个 0， 这样处理可以不用考虑边界条件"""
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0

    def canPlaceFlowers3(self, flowerbed: List[int], n: int) -> bool:
        """利用规则,每次跳两格"""
        m = len(flowerbed)
        i = 0
        while i < m:
            if flowerbed[i] == 0:
                if i == m-1 or flowerbed[i+1] == 0:
                    n -= 1
                    if n <= 0:
                        return True
                else:
                    i += 1
            i += 2
        return n <= 0


if __name__ == '__main__':
    flowerbed = [0,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0]
    n = 5
    print(Solution().canPlaceFlowers(flowerbed, n))
