"""
给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：
'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。
你需要根据这个学生的出勤记录判断他是否会被奖赏。
"""

import re


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """正则查找连续的0和连续的1"""
        binary_regex = re.compile(r'0+|1+')
        lst = binary_regex.findall(s)
        nums = []
        for str in lst:
            nums.append(len(str))
        # print(nums)
        ans = 0
        for i in range(1,len(nums)):
            ans += min(nums[i-1], nums[i])
        return ans

    def countBinarySubstrings2(self, s: str) -> int:
        """将字符串 s 按照 0 和 1 的连续段分组，存在counts 数组中，例如 s = 00111011，
        可以得到这样的counts数组：counts={2,3,1,2}，
        再取任意两个相邻数字的最小值，计算它们的和"""
        pre = 0
        n = len(s)
        last = 0
        ans = 0
        while pre < n:
            c = s[pre]
            count = 0
            while pre < n and s[pre] == c:
                pre += 1
                count += 1
            ans += min(last, count)
            last = count

        return ans

    def countBinarySubstrings3(self, s: str) -> int:
        """将连续的0和连续的1分段"""
        l = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split()))
        return sum(min(a, b) for a, b in zip(l, l[1:]))


if __name__ == '__main__':
    # s = "00110011"
    s = "000111010101"
    print(Solution().countBinarySubstrings(s))
