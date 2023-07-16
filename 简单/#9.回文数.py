"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
"""


def isPalindrome(x: int) -> bool:
    """利用字符串翻转"""
    if x < 0:
        return False
    else:
        return str(x)[::-1] == str(x)


def isPalindrome2(x: int) -> bool:
    """在原整数上反转后半段数字"""
    # 利用0的特性排除一部分
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    reversedNumber = 0
    while x > reversedNumber:  # 反转后半段
        reversedNumber = reversedNumber * 10 + x % 10
        x = x // 10
    # print(reversedNumber)
    return x == reversedNumber or reversedNumber//10 == x  # 考虑奇数和偶数的情况


if __name__ == '__main__':
    print(isPalindrome2(12321))
