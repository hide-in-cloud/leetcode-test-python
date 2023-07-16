"""
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for i in range(1, n):
            res = self.describeNum(res)
        return res

    def describeNum(self, s: str):
        res = ""
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                res += str(count) + s[i-1]
                count = 1
        res += str(count) + s[-1]
        return res


if __name__ == '__main__':
    n = 3
    # print(Solution().describeNum("1211"))
    print(Solution().countAndSay(n))
