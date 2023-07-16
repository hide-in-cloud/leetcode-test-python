"""
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
"""


def reverseWords(s: str) -> str:
    return " ".join([word[::-1] for word in s.split()])

    # s2 = s.split()
    # words = []
    # for word in s2:
    #     words.append(word[::-1])
    # return " ".join(words)


def reverseWords2(s: str) -> str:
    """利用两次翻转"""
    return " ".join(s.split()[::-1])[::-1]


if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    print(reverseWords2(s))
