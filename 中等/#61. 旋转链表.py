"""
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createList(nums):
    q = None
    for i in range(len(nums) - 1, -1, -1):
        p = ListNode(nums[i], next=q)
        q = p
    return q


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        p = dummy = ListNode(next=head)
        length = 0
        while p.next:  # 计算长度
            length += 1
            p = p.next
        p.next = dummy.next  # 头尾相接

        k = k % length
        for _ in range(length - k):
            p = p.next  # 倒数第k个的前结点
        ans = p.next  # 把倒数第k个结点做为头
        p.next = None
        return ans


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    k = 2
    head = createList(nums)
    print(Solution().rotateRight(head, k))
