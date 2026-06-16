# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointer
        dummy = ListNode(0, head) # del head list
        slow = fast = dummy

        while n > 0:
            fast = fast.next
            n -= 1
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummy.next

        # lenhead = 0
        # newHead = resHead = head
        # while newHead:
        #     lenhead += 1
        #     newHead = newHead.next
        # if n == lenhead:
        #     return head.next
        # # [1,2,3,4,5] n=2 5-2=3
        # pos = lenhead - n
        # while (pos - 1) > 0:
        #     head = head.next
        #     pos -= 1
        # head.next = head.next.next

        # return resHead


