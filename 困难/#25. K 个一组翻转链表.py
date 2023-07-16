"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序

进阶：
你可以设计一个只使用常数额外空间的算法来解决此问题吗？
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """头插法, 当前结点的下一个结点调整为前驱结点的下一个结点"""
        dummy = ListNode(next=head)
        p = dummy
        length = 0
        while p.next:
            length += 1
            p = p.next

        pre = dummy
        cur = pre.next
        for _ in range(length//k):
            for _ in range(k-1):  # 把当前结点的下一个结点插入到pre的下一个结点
                p = cur.next  # 保存next指针
                cur.next = p.next
                p.next = pre.next
                pre.next = p
            pre = cur
            cur = pre.next

        return dummy.next


if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7,8]  # 1,5,4,3,2,6
    k = 3
    head = createList(nums)
    print(Solution().reverseKGroup(head, k))
