"""
请实现 copyRandomList 函数，复制一个复杂链表。
在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null
"""
from typing import List


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def createList(nums):
    n = len(nums)
    lst = []
    for i in range(n):
        lst.append(Node(nums[i][0]))
    lst.append(None)
    for i in range(n):
        lst[i].next = lst[i+1]
        if lst[i][1] is None:
            lst[i].random = None
        else:
            lst[i].random = lst[lst[i][1]]
    return lst[0]


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """哈希表"""
        if not head:
            return head
        dic = {}
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        return dic[head]

    def copyRandomList2(self, head: 'Node') -> 'Node':
        """拼接 + 拆分"""
        if not head:
            return head
        cur = head
        # 1. 复制各节点，并构建拼接链表
        while cur:
            temp = Node(cur.val)
            temp.next = cur.next
            cur.next = temp
            cur = temp.next
        # 2. 构建各新节点的 random 指向
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 3. 拆分两链表
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None
        return res


if __name__ == '__main__':
    nums = [[7,None],[13,0],[11,4],[10,2],[1,0]]
    head = createList(nums)
    print(Solution().copyRandomList(head))
