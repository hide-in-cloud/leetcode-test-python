"""
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。
"""
from typing import List


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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """优先队列"""
        def __lt__(self, other):
            return self.val < other.val
        ListNode.__lt__ = __lt__

        import heapq
        pre = dummy = ListNode()
        q = []
        for l in lists:
            if l:
                heapq.heappush(q, l)
        while q:
            node = heapq.heappop(q)
            pre.next = node
            pre = node
            if node.next:
                heapq.heappush(q, node.next)
        return dummy.next

        # import heapq
        # pre = dummy = ListNode()
        # q = []
        # for i in range(len(lists)):
        #     if lists[i]:
        #         heapq.heappush(q, (lists[i].val, i))
        #         lists[i] = lists[i].next
        # while q:
        #     val, idx = heapq.heappop(q)
        #     pre.next = ListNode(val)
        #     pre = pre.next
        #     if lists[idx]:
        #         heapq.heappush(q, (lists[idx].val, idx))
        #         lists[idx] = lists[idx].next
        # return dummy.next

    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        """分治合并"""
        def merge(l: int, r: int):
            if l == r:
                return lists[l]
            if l > r:
                return None
            mid = (l + r) >> 1
            return mergeTwoLists(merge(l, mid), merge(mid+1, r))

        def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
            """合并两个链表"""
            pre = dummy = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    pre.next = l1
                    l1 = l1.next
                else:
                    pre.next = l2
                    l2 = l2.next
                pre = pre.next
            pre.next = l1 if l1 else l2
            return dummy.next

        return merge(0, len(lists)-1)

    def mergeKLists3(self, lists: List[ListNode]) -> ListNode:
        """两两合并"""
        def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
            """合并排序"""
            pre = dummy = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    pre.next = l1
                    l1 = l1.next
                else:
                    pre.next = l2
                    l2 = l2.next
                pre = pre.next
            pre.next = l1 if l1 else l2
            return dummy.next

        ans = None
        for i in range(len(lists)):
            ans = mergeTwoLists(ans, lists[i])
        return ans

    def mergeKLists4(self, lists: List[ListNode]) -> ListNode:
        """先把每个值放进列表,然后排序,再构成链表"""
        lst = []
        for l in lists:
            while l:
                lst.append(l.val)
                l = l.next
        lst.sort()
        pre = dummy = ListNode()
        for num in lst:
            pre.next = ListNode(num)
            pre = pre.next
        return dummy.next


if __name__ == '__main__':
    nums = [[1,4,5],[1,3,4],[],[2,6]]
    lists = []
    for i in range(len(nums)):
        lists.append(createList(nums[i]))
    print(Solution().mergeKLists(lists))
