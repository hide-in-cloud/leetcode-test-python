"""
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """调用内置函数,字符串先转为十进制再转为二进制"""
        # return bin(int(a, 2) + int(b, 2))[2:]
        return "{:b}".format(int(a, 2) + int(b, 2))

    def addBinary2(self, a: str, b: str) -> str:
        """模拟,先转为整型数组,逐位相加"""
        a, b = list(map(int, a)), list(map(int, b))
        n, m = len(a), len(b)
        res = [0] * max(n, m)
        i = -1
        c = 0  # 进位标志
        while i > -n-1 or i > -m-1:
            # print(a[i], b[i])
            c += a[i] if i > -n-1 else 0
            c += b[i] if i > -m-1 else 0
            res[i] = c % 2
            c = c // 2
            i -= 1
        if c == 1:
            res.insert(0, 1)
        return "".join(map(str, res))

    def addBinary3(self, a: str, b: str) -> str:
        """模拟,字符串上逐位相加"""
        n, m = len(a), len(b)
        res = ""
        i = 0
        c = 0  # 进位标志
        while i < n or i < m:
            # print(a[i], b[i])
            c += ord(a[n-1-i]) - ord('0') if i < n else 0
            c += ord(b[m-1-i]) - ord('0') if i < m else 0
            res = str(c % 2) + res
            c = c // 2
            i += 1
        if c > 0:
            res = '1' + res
        return res

    def addBinary4(self, a: str, b: str) -> str:
        """位运算"""
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y  # 异或
            carry = (x & y) << 1  # x与y,再右移1位
            x, y = answer, carry
        return bin(x)[2:]


if __name__ == '__main__':
    a = "1110"
    b = "101"
    print(Solution().addBinary4(a, b))
