"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

有效括号组合需满足：左括号必须以正确的顺序闭合。
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        a = ["()"]
        b = ["(())","()()"]
        c = ["((()))","(()())","(())()","()(())","()()()"]
        d = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
        """
        dp = [[""] for _ in range(n)]
        dp[0] = ["()"]
        for k in range(1, n):
            last = dp[k - 1]
            set1 = set()  # 集合存放不同的有效括号
            for i in range(len(last)):  # 遍历上一个dp的列表，获取每个括号组合
                item = last[i]
                for j in range(len(item)):  # 对于每个括号组合，尝试在每个位置插入一对括号()，把不同的组合添加到集合中
                    set1.add(item[:j] + "()" + item[j:])
            dp[k] = list(set1)
        # print("dp=", dp)
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(4))
