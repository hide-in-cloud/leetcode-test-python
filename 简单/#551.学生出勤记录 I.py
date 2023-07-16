"""
给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：
'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。
你需要根据这个学生的出勤记录判断他是否会被奖赏。
"""

import collections


class Solution:
    def checkRecord(self, s: str) -> bool:
        # return s.count('A') <= 1 and 'LLL' not in s

        count = 0
        for i in range(len(s)):
            if s[i] == 'A':
                count += 1
            if count > 1:
                return False
            if s[i] == 'L':
                if i+3 <= len(s) and s[i+1] == 'L' and s[i+2] == 'L':
                    return False
        return True


if __name__ == '__main__':
    s = "PPALLPLL"
    # s = "LALL"
    print(Solution().checkRecord(s))
