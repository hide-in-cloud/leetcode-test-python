"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
"""


def isPalindrome(s: str) -> bool:
    """双指针
    空间复杂度：O(|s|)"""
    string = ''
    for char in s.lower():
        if char.isalnum():
            string += char
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


def isPalindrome2(s: str) -> bool:
    """字符串翻转
    空间复杂度：O(|s|)"""
    s2 = ''.join(ch.lower() for ch in s if ch.isalnum())  # 筛选字符
    return s2 == s2[::-1]  # 逆序字符串


def isPalindrome3(s: str) -> bool:
    """在原字符串上直接判断
    空间复杂度：O(1)"""
    left, right = 0, len(s)-1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if left < right:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
    return True


print(isPalindrome('race car'))
print(isPalindrome2('race car'))
print(isPalindrome3('race car'))
