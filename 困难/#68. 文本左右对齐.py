"""
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格' '填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格
"""
from typing import List

BLANK = " "


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        n = len(words)
        i = 0
        while i < n:
            line = [words[i]]
            width = len(words[i])
            i += 1
            while i < n and width + 1 + len(words[i]) <= maxWidth:
                line.append(words[i])
                width += 1 + len(words[i])
                i += 1
            num = len(line)  # 当前行的单词数
            if i != n and num >= 2:
                redundancy = (maxWidth - width) % (num - 1)  # 额外的空格
                spaces = (maxWidth - width) // (num - 1) + 1  # 平均分配的空格
                if redundancy == 0:
                    res.append((spaces * BLANK).join(line))
                else:
                    string = line[0]
                    for j in range(1, num):
                        string += spaces * BLANK
                        if j <= redundancy:
                            string += BLANK
                        string += line[j]
                    res.append(string)
            elif num == 1 or i == n:  # 当前行只有一个单词或者是最后一行时
                res.append(BLANK.join(line).ljust(maxWidth))  # 左对齐

        return res


if __name__ == '__main__':
    # words = ["This", "is", "an", "example", "of", "text", "justification."]
    # words = ["What","must","be","acknowledgment","shall","be"]
    # maxWidth = 16
    words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
             "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
    maxWidth = 20
    print(Solution().fullJustify(words, maxWidth))
