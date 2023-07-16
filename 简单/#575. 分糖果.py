"""
给定一个偶数长度的数组，其中不同的数字代表着不同种类的糖果，每一个不同的数字代表一种糖果。
你需要把这些糖果平均分给一个弟弟和一个妹妹。返回妹妹可以获得的最大糖果的种类数
"""
from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType)//2)


if __name__ == '__main__':
    candyType = [1,1,2,3]
    print(Solution().distributeCandies(candyType))
