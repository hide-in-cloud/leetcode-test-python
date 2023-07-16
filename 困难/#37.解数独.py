"""
请你判断一个 9x9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
数独部分空格内已填入了数字，空白格用 '.' 表示
"""
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        symbols = set("123456789")
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        count = 0
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    pos = (i // 3) * 3 + j // 3
                    rows[i].add(num)
                    columns[j].add(num)
                    squares[pos].add(num)
                    count += 1
        while count < 81:
            for i in range(9):
                for j in range(9):
                    num = board[i][j]
                    if num == ".":
                        pos = (i // 3) * 3 + j // 3
                        container = rows[i] | columns[j] | squares[pos]
                        if len(container) == 8:
                            board[i][j] = (symbols - container).pop()
                            print((i,j), (symbols - container).pop())
                            count += 1


if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    print(Solution().solveSudoku(board))
