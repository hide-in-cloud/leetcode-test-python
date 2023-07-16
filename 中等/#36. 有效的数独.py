"""
请你判断一个 9x9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
数独部分空格内已填入了数字，空白格用 '.' 表示
"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    pos = (i // 3) * 3 + j // 3
                    if num not in rows[i] and num not in columns[j] and num not in squares[pos]:
                        rows[i].add(num)
                        columns[j].add(num)
                        squares[pos].add(num)
                    else:
                        return False
        return True


if __name__ == '__main__':
    board = [[".",".",".",".",".","3",".",".","."],
             ["8",".",".",".",".","5",".","1","."],
             [".",".",".",".","7",".",".",".","3"],
             [".",".",".",".",".",".",".",".","."],
             [".","5","9","7",".",".",".","9","."],
             ["7",".",".",".",".",".",".",".","."],
             [".","6",".",".",".",".","2",".","."],
             [".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".","7",".","."]]
    print(Solution().isValidSudoku(board))
