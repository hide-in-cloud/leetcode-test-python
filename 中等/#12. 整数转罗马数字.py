"""
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        romans = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        ans = ""
        for i in range(len(romans) - 1, -1, -1):
            while num >= values[i]:
                num -= values[i]
                ans += romans[i]
        return ans

    def intToRoman2(self, num: int) -> str:
        """硬编码数字"""
        THOUSANDS = ["", "M", "MM", "MMM"]  # 千位
        HUNDREDS = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]  # 百位
        TENS = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]  # 十位
        ONES = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]  # 个位

        return THOUSANDS[num // 1000] + \
               HUNDREDS[num % 1000 // 100] + \
               TENS[num % 100 // 10] + \
               ONES[num % 10]


if __name__ == '__main__':
    num = 58
    # num = 1994
    print(Solution().intToRoman(num))
