"""
你在和朋友一起玩 猜数字（Bulls and Cows）游戏，该游戏规则如下：
你写出一个秘密数字，并请朋友猜这个数字是多少。
朋友每猜测一次，你就会给他一个提示，告诉他的猜测数字中有多少位属于数字和确切位置都猜对了（称为“Bulls”, 公牛），
有多少位属于数字猜对了但是位置不对（称为“Cows”, 奶牛）。朋友根据提示继续猜，直到猜出秘密数字。
请写出一个根据秘密数字和朋友的猜测数返回提示的函数，返回字符串的格式为 xAyB ，x 和 y 都是数字，A 表示公牛，用 B 表示奶牛。
xA 表示有 x 位数字出现在秘密数字中，且位置都与秘密数字一致。
yB 表示有 y 位数字出现在秘密数字中，但位置与秘密数字不一致。
请注意秘密数字和朋友的猜测数都可能含有重复数字，每位数字只能统计一次。
"""
import collections


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a, b = 0, 0
        secret = list(secret)
        guess = list(guess)
        i = 0
        while i < len(secret):
            print(secret)
            if guess[i] == secret[i]:
                a += 1
                secret.pop(i)
                guess.pop(i)
            else:
                i += 1
        i = 0
        while i < len(guess):
            if guess[i] in secret:
                b += 1
                secret.remove(guess[i])
            i += 1
        return f'{a}A{b}B'

    def getHint2(self, secret: str, guess: str) -> str:
        mp_secret = collections.defaultdict(int)
        mp_guess = collections.defaultdict(int)
        a, b = 0, 0

        for i, j in zip(secret, guess):
            if i == j:
                a += 1
            else:
                mp_secret[i] += 1
                mp_guess[j] += 1
        for key in mp_secret:
            if key in mp_guess:
                b += min(mp_secret[key], mp_guess[key])

        return f'{a}A{b}B'


if __name__ == '__main__':
    secret = "011"
    guess = "110"
    print(Solution().getHint2(secret, guess))
