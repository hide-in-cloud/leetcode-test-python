"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
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
    def reverseList(self, head: ListNode) -> ListNode:
        """迭代"""
        pre, cur = None, head
        while cur:
            p = cur.next  # 保存next指针
            cur.next = pre
            pre = cur
            cur = p
        return pre

    def reverseList2(self, head: ListNode) -> ListNode:
        """递归"""
        if not head or not head.next:
            return head
        p = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return p


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    head = createList(nums)
    print(Solution().reverseList2(head))
