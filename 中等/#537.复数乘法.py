"""
复数 可以用字符串表示，遵循 "实部+虚部i" 的形式，并满足下述条件：
    实部 是一个整数，取值范围是 [-100, 100]
    虚部 也是一个整数，取值范围是 [-100, 100]
    i2 == -1
给你两个字符串表示的复数 num1 和 num2 ，请你遵循复数表示形式，返回表示它们乘积的字符串
"""


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split('+')
        a1, a2 = int(num1[0]), int(num1[1][:-1])
        num2 = num2.split('+')
        b1, b2 = int(num2[0]), int(num2[1][:-1])
        a = a1*b1 - a2*b2  # 实部
        b = a1*b2 + b1*a2  # 虚部
        return f"{a}+{b}i"


if __name__ == '__main__':
    # num1 = "1+-2i"
    # num2 = "2+3i"
    num1 = "1+-1i"
    num2 = "1+-1i"
    print(Solution().complexNumberMultiply(num1, num2))
