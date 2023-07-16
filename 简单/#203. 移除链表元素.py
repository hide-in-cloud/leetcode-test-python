"""
给定一个单链表，你的任务是删除链表中等于所给值的元素。
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
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0, head)
        p = dummy
        while p.next is not None:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next

        return dummy.next


if __name__ == '__main__':
    nums = [1]
    val = 0
    head = createList(nums)
    print(Solution().removeElements(head, val))
