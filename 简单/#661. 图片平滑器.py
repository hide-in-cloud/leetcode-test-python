"""
包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入)，
平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们
"""
from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        """遍历每个格周围的9个点"""
        numRows, numColumns = len(img), len(img[0])
        grayscale = [[0 for _ in range(numColumns)] for _ in range(numRows)]
        for r in range(numRows):
            for c in range(numColumns):
                count = 0
                for i in (r-1,r,r+1):
                    for j in (c-1,c,c+1):
                        if 0 <= i < numRows and 0 <= j < numColumns:
                            grayscale[r][c] += img[i][j]
                            count += 1
                grayscale[r][c] //= count
        return grayscale


if __name__ == '__main__':
    img = [[1,1,1],[1,0,1],[1,1,1]]
    print(Solution().imageSmoother(img))
