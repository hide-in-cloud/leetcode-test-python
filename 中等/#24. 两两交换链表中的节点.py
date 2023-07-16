"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换
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
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head

        p = dummy = ListNode(next=head)

        while p.next and p.next.next:
            node1 = p.next
            node2 = p.next.next
            node1.next = node2.next
            p.next = node2
            node2.next = node1
            p = node1

        return dummy.next


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    head = createList(nums)
    print(Solution().swapPairs(head))
