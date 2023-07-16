"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """逐位相乘"""
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        ansArr = [0] * (n+m)
        for i in range(m-1,-1,-1):  # 逐位相乘
            x = int(num1[i])
            for j in range(n-1,-1,-1):
                ansArr[i+j+1] += int(num2[j]) * x

        for i in range(m+n-1,0,-1):  # 进位处理
            ansArr[i-1] += ansArr[i] // 10
            ansArr[i] = ansArr[i] % 10

        if ansArr[0] == 0:  # 舍弃高位的0
            ansArr.pop(0)
        return "".join(map(str, ansArr))

    def multiply2(self, num1: str, num2: str) -> str:
        """把乘数的每位乘积结果累加"""
        n, m = len(num1), len(num2)
        res = 0
        for i in range(m-1,-1,-1):
            num = "0" * (m-1-i)
            c = 0
            for j in range(n-1,-1,-1):
                c += int(num2[i]) * int(num1[j])
                num = str(c % 10) + num
                c = c // 10
            if c > 0:
                num = str(c) + num
            res += int(num)
        return str(res)


if __name__ == '__main__':
    num1 = "99"
    num2 = "9"
    print(Solution().multiply(num1, num2))
