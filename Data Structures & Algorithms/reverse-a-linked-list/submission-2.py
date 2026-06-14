# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # https://labuladong.online/zh/algo/data-structure/reverse-linked-list-recursion/#%E9%80%92%E5%BD%92%E8%A7%A3%E6%B3%95
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