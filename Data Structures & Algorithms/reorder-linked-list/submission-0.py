# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle point
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # seperate two listNode
        second = slow.next
        slow.next = None
        # reverse second listNode
        pre = None
        while second:
            temp = second.next
            second.next = pre
            pre = second
            second = temp
        # second listNode start pointer is pre.
        first, second = head, pre
        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
