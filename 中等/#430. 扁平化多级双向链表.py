"""
多级双向链表中，除了指向下一个节点和前一个节点指针之外，它还有一个子链表指针，可能指向单独的双向链表。
这些子列表也可能会有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。

给你位于列表第一级的头节点，请你扁平化列表，使所有结点出现在单级双链表中。
"""


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def createList(nums):
    if nums is None:
        return None
    head = Node(nums[0], None, None, None)
    q = p = head
    i = 1
    while nums[i] is not None:
        p = Node(nums[i], prev=q, next=None, child=None)
        q.next = p
        q = p
        i += 1
    j = 0
    while nums[i+1] is None:
        j += 1
        i += 1
    return q


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        """栈"""
        if not head:
            return head
        p = head
        stack = list()
        while True:
            if p.child:
                if p.next is not None:
                    stack.append(p.next)
                p.next = p.child
                p.child.prev = p
                p.child = None
            elif p.next:
                p = p.next
            elif stack:
                q = stack.pop()
                p.next = q
                q.prev = p
                p = q
            else:
                return head

    def flatten2(self, head: 'Node') -> 'Node':
        """模拟二叉树的先序遍历"""
        if not head:
            return head
        prev = dummy = Node(0, None, None, None)
        stack = [head]
        while stack:
            cur = stack.pop()
            cur.prev = prev
            prev.next = cur

            if cur.next:  # 相当右子树
                stack.append(cur.next)
            if cur.child:  # 相当左子树
                stack.append(cur.child)
                cur.child = None

            prev = cur
        dummy.next.prev = None
        return dummy.next

    def flatten3(self, head: 'Node') -> 'Node':
        """利用递归"""
        if not head:
            return head
        dummy = Node(0, None, None, None)
        self.flatten_dfs(dummy, head)
        dummy.next.prev = None
        return dummy.next

    def flatten_dfs(self, prev, curr):
        """递归函数"""
        if not curr:
            return prev

        curr.prev = prev
        prev.next = curr

        tempNext = curr.next
        tail = self.flatten_dfs(curr, curr.child)
        curr.child = None
        return self.flatten_dfs(tail, tempNext)


if __name__ == '__main__':
    nums = [1,2,3,4,5,6,None,None,None,7,8,9,10,None,None,11,12]
    head = createList(nums)
    print(Solution().flatten(head))
