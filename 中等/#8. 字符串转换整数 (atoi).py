"""
请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。
函数 myAtoi(string s) 的算法如下：
    读入字符串并丢弃无用的前导空格
    检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
    读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
    将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
    如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被固定为 −231 ，大于 231 − 1 的整数应该被固定为 231 − 1 。
    返回整数作为最终结果。
注意：
    本题中的空白字符只包括空格字符 ' ' 。
    除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符
"""
INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Automaton:
    """自动机类"""
    def __init__(self):
        self.ans = 0  # 无符号数
        self.sign = 1  # 符号
        self.state = "start"
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c: str):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == "in_number":
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == "signed":
            self.sign = 1 if c == '+' else -1


class Solution:
    def myAtoi(self, s: str) -> int:
        """利用自动机"""
        automaton = Automaton()
        for c in s:
            automaton.get(c)
            if automaton.state == 'end':
                break
        return automaton.sign * automaton.ans

    def myAtoi2(self, s: str) -> int:
        """法二"""
        s = s.lstrip()  # 去除空格

        if len(s) == 0:
            return 0

        num = ""
        sign = 1

        # 判断符号
        i = 0
        if s[i] == '+' or s[i] == '-':
            if s[i] == '-':
                sign = -1
            i = 1

        # 截取连续的数字
        while i < len(s):
            if s[i].isdigit():
                num += s[i]
                i += 1
            else:
                break
        num = sign*int(num) if num != "" else 0

        # 判断溢出
        if num < -2 ** 31:
            num = -2 ** 31
        elif num > 2 ** 31 - 1:
            num = 2 ** 31 - 1

        return num


if __name__ == '__main__':
    s = "-91283472332"
    # print(-2 ** 31)
    print(Solution().myAtoi2(s))
