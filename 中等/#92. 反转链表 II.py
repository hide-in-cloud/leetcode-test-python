"""
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。
请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表
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
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """头插法, 当前结点的下一个结点调整为前驱结点的下一个结点"""
        pre = dummy = ListNode(next=head)

        for i in range(left-1):  # 定位前驱结点pre
            pre = pre.next
        cur = pre.next

        for i in range(right-left):  # 把当前结点的下一个结点插入到pre的下一个结点
            p = cur.next  # 保存next指针
            cur.next = p.next
            p.next = pre.next
            pre.next = p

        return dummy.next


if __name__ == '__main__':
    nums = [1,2,3,4,5,6]  # 1,5,4,3,2,6
    left = 2
    right = 5
    head = createList(nums)
    print(Solution().reverseBetween(head, left, right))
