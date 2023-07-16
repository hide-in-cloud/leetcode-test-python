"""
给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。
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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        q = dummy
        p = head
        for i in range(n):
            p = p.next
        while p:
            p = p.next
            q = q.next
        q.next = q.next.next
        # while head:
        #     print(head.val)
        #     head = head.next
        return dummy.next


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    head = createList(nums)
    n = 1
    print(Solution().removeNthFromEnd(head, n))
