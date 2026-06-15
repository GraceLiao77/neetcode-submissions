# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow and fast pointer
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

        # HashSet
        # headmap = set()

        # while head:
        #     if head not in headmap:
        #         headmap.add(head)
        #     else:
        #         return True
        #     head = head.next
        # return False
