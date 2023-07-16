"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """模拟竖式加法"""
        cur = dummy = ListNode()
        _sum = 0  # 每一位的和
        carry = 0  # 进位
        while l1 or l2 or carry:
            _sum = carry
            if l1:
                l1, _sum = l1.next, _sum + l1.val
            if l2:
                l2, _sum = l2.next, _sum + l2.val
            carry, _sum = divmod(_sum, 10)
            cur.next = cur = ListNode(_sum)

        # p = dummy.next
        # while p:
        #     print(p.val)
        #     p = p.next

        return dummy.next


if __name__ == '__main__':
    num1 = [2,4,9]
    num2 = [5,6,4,9]
    l1 = createList(num1)
    l2 = createList(num2)
    print(Solution().addTwoNumbers(l1, l2))
