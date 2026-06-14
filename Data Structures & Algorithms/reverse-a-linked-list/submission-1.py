# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return last

        
        # iteration
        # if not head:
        #     return head
        # # none <-prev- 0 -next-> 1 -next-> 2 -next-> 3
        # # none <-prev- 0 <-prev- 1 <-prev- 2 <-prev- 3
        # prev, curr = None, head

        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp

        # return prev