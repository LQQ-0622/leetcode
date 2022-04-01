# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        import heapq
        next_add_heap = []  # 每个链表中未被合并的最小结点
        finall_list = ListNode()
        head = finall_list
        for list_index in range(len(lists)):
            if lists[list_index]:
                heapq.heappush(next_add_heap, (lists[list_index].val, list_index))
                lists[list_index] = lists[list_index].next
        while next_add_heap:
            val, list_index = heapq.heappop(next_add_heap)
            finall_list.next = ListNode(val)
            finall_list = finall_list.next
            if lists[list_index]:
                heapq.heappush(next_add_heap, (lists[list_index].val, list_index))
                lists[list_index] = lists[list_index].next
        return head.next


input = [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]
result = Solution().mergeKLists(input)


def printNode(head):
    while head:
        print(head.val)
        head = head.next
    print('======')


printNode(result)
