"""
将非负整数 num 转换为其对应的英文表示
"""


class Solution:
    ONES = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    two_less_20 = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
                   16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
    Tens = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
    Levels = ["", "Thousand", 'Million', 'Billion']

    def numberToWords(self, num: int) -> str:
        """按照西方数字每三位分割开，每次处理三位"""

        def helper(num: int):
            """处理个十百位的数字"""
            hundred = num // 100
            ten = num % 100 // 10
            one = num % 10

            res = ""
            if hundred != 0:
                res += self.ONES[hundred] + " Hundred "
            if ten != 0:
                if ten >= 2:
                    res += self.Tens[ten] + " "
                else:
                    tens = ten * 10 + one
                    res += self.two_less_20[tens] + " "
                    return res
            if one != 0:
                res += self.ONES[one] + " "
            return res

        if num == 0:
            return "Zero"

        res = ""
        i = 0
        while num > 0:
            three = num % 1000
            if three:
                res = helper(three) + self.Levels[i] + ' ' + res
            num = num // 1000
            i += 1

        return res.strip()


if __name__ == '__main__':
    num = 20
    # num = 120
    # num = 1000010
    # num = 1000
    # num = 12994
    # num = 1234567
    # num = 1034067801
    print(Solution().numberToWords(num))
