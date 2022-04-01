# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        list3 = ListNode()
        head = list3
        while list1 and list2:
            if list1.val <= list2.val:
                list3.next = ListNode(list1.val)
                list3 = list3.next
                list1 = list1.next
            else:
                list3.next = ListNode(list2.val)
                list3 = list3.next
                list2 = list2.next

        list3.next = list1 if list1 else list2

        return head.next


def printNode(head):
    while head:
        print(head.val)
        head = head.next
    print('======')


list1 = ListNode(1, ListNode(2))  # , ListNode(4)
list2 = ListNode(1, ListNode(3, ListNode(4)))


result = Solution().mergeTwoLists(list1, list2)


printNode(list1)
printNode(list2)
printNode(result)
