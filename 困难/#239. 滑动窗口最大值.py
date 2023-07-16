"""
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值
"""
from typing import List
import heapq
import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """双端单调队列"""
        if k == 1:
            return nums

        q = collections.deque()

        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        res = [nums[q[0]]]

        for i in range(k, len(nums)):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i-k:
                q.popleft()
            res.append(nums[q[0]])
        return res

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        """优先队列"""
        if k == 1:
            return nums

        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        res = [-q[0][0]]
        for i in range(k, len(nums)):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i-k:
                heapq.heappop(q)
            res.append(-q[0][0])
        return res

    def maxSlidingWindow4(self, nums: List[int], k: int) -> List[int]:
        """暴力, 超时"""
        res = []
        for i in range(len(nums)-k+1):
            res.append(max(nums[i:i+k]))
        return res


if __name__ == '__main__':
    nums = [9,10,9,-7,-4,-8,2,-6]
    k = 5
    print(Solution().maxSlidingWindow2(nums, k))
