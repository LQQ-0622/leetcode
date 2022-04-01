# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next


    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        left, right = head, head
        distance = 0
        length = 1
        while (right.next):
            if distance < n:
                right = right.next
                distance += 1
                length += 1
            else:
                right = right.next
                left = left.next
                length += 1
        if distance == n:
            left.next = left.next.next
        elif length == n and distance == length - 1:
            head = left.next
        return head


head = [1, 2, 3, 4, 5]
n = 2
