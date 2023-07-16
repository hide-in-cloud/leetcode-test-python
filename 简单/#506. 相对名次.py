"""
给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”
（"Gold Medal", "Silver Medal", "Bronze Medal"）。(注：分数越高的选手，排名越靠前。)
"""
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """排序 + 散列表"""
        ans = []
        dic = {}  # (key, value)=(分数, 名次)
        sorted_score = sorted(score, reverse=True)  # 降序排列
        n = len(score)

        for i in range(n):
            if i == 0:
                dic[sorted_score[i]] = 'Gold Medal'
            elif i == 1:
                dic[sorted_score[i]] = 'Silver Medal'
            elif i == 2:
                dic[sorted_score[i]] = 'Bronze Medal'
            else:
                dic[sorted_score[i]] = str(i+1)

        for i in range(n):
            ans.append(dic[score[i]])

        return ans

    def findRelativeRanks2(self, score: List[int]) -> List[str]:
        """计数排序"""
        length = len(score)  # 原得分数组长度
        ans = [''] * length
        max_num = max(score)  # 最高得分
        # 下标为成绩，值为成绩在原score数组的下标
        nums_index = [-1] * (max_num+1)
        for i in range(length):
            nums_index[score[i]] = i
        # 记录成绩对应的排名
        rank = 1
        for i in range(len(nums_index)-1, -1, -1):
            if nums_index[i] >= 0:
                if rank == 1:
                    ans[nums_index[i]] = 'Gold Medal'
                elif rank == 2:
                    ans[nums_index[i]] = 'Silver Medal'
                elif rank == 3:
                    ans[nums_index[i]] = 'Bronze Medal'
                else:
                    ans[nums_index[i]] = str(rank)
                rank += 1
        return ans

    def findRelativeRanks3(self, score: List[int]) -> List[str]:
        """最大堆"""
        pass


if __name__ == '__main__':
    s = [123123,11921,1,0,123]
    print(Solution().findRelativeRanks2(s))
