# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # l1 = [2,4,3]  代表 342
        # l2 = [5,6,4]  代表 465
        res = newhead = ListNode(0)
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            cur = int(v1) + int(v2) + newhead.val
            newhead.val = cur % 10
            if (l1 and l1.next) or (l2 and l2.next) or ((cur // 10) > 0):
                newhead.next = ListNode((cur // 10) % 10)
            newhead = newhead.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res
