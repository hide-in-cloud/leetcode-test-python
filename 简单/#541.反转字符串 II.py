"""
给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。
如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
"""


def reverseStr(s: str, k: int) -> str:
    s2 = list(s)
    length = len(s2)
    for i in range(0, length, k * 2):
        left, right = i, i+k
        s2[left:right] = reversed(s2[left:right])
    return "".join(s2)


def reverseStr2(s: str, k: int) -> str:
    length = len(s)
    s2 = ""
    left, mid, right = 0, k, 2*k
    while len(s2) < length:
        s2 += s[left:mid][::-1] + s[mid:right]
        left, mid, right = left+2*k, mid+2*k, right+2*k
    return s2


if __name__ == '__main__':
    s = "abcdefgh"
    k = 3
    print(reverseStr(s, k))
