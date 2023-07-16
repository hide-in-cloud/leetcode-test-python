"""
给你一个字符串 s ，逐个翻转字符串中的所有 单词 。
单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
请你返回一个翻转 s 中单词顺序并用单个空格相连的字符串。

说明：
输入字符串 s 可以在前面、后面或者单词间包含多余的空格。
翻转后单词间应当仅用一个空格分隔。
翻转后的字符串中不应包含额外的空格。
"""
import collections


def reverseWords(s: str) -> str:
    """使用 split和reverse"""
    return " ".join(s.split()[::-1])


def reverseWords2(s: str) -> str:
    """使用双端队列"""
    left, right = 0, len(s)-1
    # 去掉字符串头部和尾部的空白字符
    while left <= right and s[left] == ' ':
        left += 1
    while left <= right and s[right] == ' ':
        right -= 1

    # 将单词push到队列头部
    d, word = collections.deque(), []
    while left <= right:
        if s[left] != ' ':
            word.append(s[left])
        elif s[left] == ' ' and word:
            d.appendleft(''.join(word))
            word = []
        left += 1
    d.appendleft(''.join(word))  # 插入最后一个单词
    return ' '.join(d)


if __name__ == '__main__':
    # s = "  hello world  "
    s = "  Bob    Loves  Alice   "
    print(reverseWords2(s))
