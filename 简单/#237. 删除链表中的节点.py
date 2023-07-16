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
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    nums = [4,5,1,9]
    val = 5
    head = createList(nums)
    p = head
    while p:
        if p.val == val:
            break
        p = p.next
    print(Solution().deleteNode(p))
