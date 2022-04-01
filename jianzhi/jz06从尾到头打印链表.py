# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> list[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]


node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(1)
head = node1
node1.next = node2
node2.next = node3
print1 = Solution().reversePrint(head)
print(print1)
