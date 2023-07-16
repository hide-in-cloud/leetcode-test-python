"""
给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示
"""
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440:
            return 0

        timePoints.sort()

        # 第一个时间点
        pre = timePoints[0]
        pre_min = int(pre[:2]) * 60 + int(pre[3:])
        # 最后一个时间点
        last = timePoints[-1]
        last_min = int(last[:2]) * 60 + int(last[3:])

        min_period = 24*60 - (last_min - pre_min)  # 记录最小时间差
        for i in range(1, len(timePoints)):
            cur = timePoints[i]
            cur_min = int(cur[:2]) * 60 + int(cur[3:])
            min_period = min(min_period, cur_min-pre_min)
            if min_period == 0:
                return min_period
            pre_min = cur_min

        return min_period


if __name__ == '__main__':
    timePoints = ["22:00","23:00","23:59","21:50","00:01","23:40",]
    print(Solution().findMinDifference(timePoints))
