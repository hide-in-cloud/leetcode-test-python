import collections


def canConstruct(ransomNote: str, magazine: str) -> bool:
    """使用Counter类，最快"""
    c1 = collections.Counter(ransomNote)
    c2 = collections.Counter(magazine)
    for k, val in c1.items():
        if c2[k] < val:
            return False
    return True


def canConstruct2(ransomNote: str, magazine: str) -> bool:
    """计数法"""
    cnt = [0] * 26
    for ch in magazine:
        cnt[ord(ch) - ord('a')] += 1
    for ch in ransomNote:
        cnt[ord(ch) - ord('a')] -= 1
        if cnt[ord(ch) - ord('a')] < 0:
            return False
    return True


if __name__ == '__main__':
    ransomNote = "aba"
    magazine = "aabcd"
    print(canConstruct(ransomNote, magazine))
