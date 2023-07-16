from typing import List


def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """

    """
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    """

    '''
    l = len(s) // 2
    for i in range(l):
        s[i], s[~i] = s[~i], s[i]
    '''

    # s.reverse()

    s[::] = s[::-1]


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    reverseString(s)
    print(s)
