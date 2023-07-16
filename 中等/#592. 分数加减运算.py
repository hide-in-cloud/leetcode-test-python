"""
给定一个表示分数加减运算表达式的字符串，你需要返回一个字符串形式的计算结果。
这个结果应该是不可约分的分数，即最简分数。
如果最终结果是一个整数，例如 2，你需要将它转换成分数形式，其分母为 1。所以在上述例子中, 2 应该被转换为 2/1
"""
import math


class Solution:
    def fractionAddition(self, expression: str) -> str:
        nums = expression.replace('+', ' +').replace('-', ' -').split(' ')
        print(nums)
        nums.remove('')
        print(nums)
        a1 = int(nums[0].split('/')[0])
        a2 = int(nums[0].split('/')[1])
        b1 = int(nums[1].split('/')[0])
        b2 = int(nums[1].split('/')[1])
        gcd = math.gcd(a2, b2)
        a = a1*b2//gcd+b1*a2//gcd  # 分子
        b = a2*b2//gcd  # 分母
        gcd = math.gcd(a, b)
        a = a//gcd
        b = b//gcd
        return f"{a}/{b}"

    def fractionAddition2(self, expression: str) -> str:
        """调用api"""
        from re import findall
        from functools import reduce
        from fractions import Fraction
        res = str(reduce(Fraction.__add__,
                         map(Fraction, findall('[+-]?\d+/\d+', expression))))
        return f'{res}/1' if len(res) <= 2 else res  # "-4/1"


if __name__ == '__main__':
    expression = "-1/4+1/2"
    print(Solution().fractionAddition2(expression))
