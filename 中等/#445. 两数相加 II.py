"""
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。
它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头

进阶：如果输入链表不能修改该如何处理？换句话说，不能对列表中的节点进行翻转。
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
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """模拟竖式加法"""

        def reverseList(head: ListNode) -> ListNode:
            """迭代翻转链表"""
            pre, cur = None, head
            while cur:
                p = cur.next  # 保存next指针
                cur.next = pre
                pre = cur
                cur = p
            return pre

        l1 = reverseList(l1)
        l2 = reverseList(l2)

        cur = None
        _sum = 0  # 每一位的和
        carry = 0  # 进位
        while l1 or l2 or carry:
            _sum = carry
            if l1:
                l1, _sum = l1.next, _sum + l1.val
            if l2:
                l2, _sum = l2.next, _sum + l2.val
            carry, _sum = divmod(_sum, 10)
            cur = ListNode(_sum, next=cur)

        # p = cur
        # while p:
        #     print(p.val)
        #     p = p.next

        return cur

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """栈"""
        num1, num2 = [], []
        while l1:
            num1.append(l1.val)
            l1 = l1.next
        while l2:
            num2.append(l2.val)
            l2 = l2.next

        cur = None
        _sum = 0  # 每一位的和
        carry = 0  # 进位
        while num1 or num2 or carry:
            _sum = carry
            if num1:
                _sum = _sum + num1.pop()
            if num2:
                _sum = _sum + num2.pop()
            carry, _sum = divmod(_sum, 10)
            cur = ListNode(_sum, next=cur)

        p = cur
        while p:
            print(p.val)
            p = p.next

        return cur


if __name__ == '__main__':
    num1 = [7,2,4,3]
    num2 = [5,6,4]
    l1 = createList(num1)
    l2 = createList(num2)
    print(Solution().addTwoNumbers(l1, l2))
