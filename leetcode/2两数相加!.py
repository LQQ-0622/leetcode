# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = l3 = ListNode(0)
        flag = 0
        while l1 or l2:
            # 判断l1,l2如果为空，则赋值0，防止错误
            l1 = l1 if l1 else ListNode(0)
            l2 = l2 if l2 else ListNode(0)
            sum = l1.val + l2.val + flag
            if sum >= 10:
                flag = 1
                value = sum - 10
                l3.val = value
                l3.next = ListNode(flag)
            else:
                flag = 0
                l3.val = sum
                l3.next = ListNode(flag)
            l1, l2 = l1.next, l2.next
            l3 = l3.next

        return result


input1 = ListNode(5, ListNode(3, ListNode(2)))
input2 = ListNode(6, ListNode(7, ListNode(8)))
result = Solution().addTwoNumbers(input1, input2)
print(result)
