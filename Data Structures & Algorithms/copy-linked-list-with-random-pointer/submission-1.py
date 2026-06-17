"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        newhead = head
        dictNode = {}
        while newhead:
            dictNode[newhead] = Node(newhead.val) #(val=newhead.val, next=None, random=None)
            newhead = newhead.next
        
        newhead = head
        while newhead:
            dictNode[newhead].next = dictNode.get(newhead.next)
            dictNode[newhead].random = dictNode.get(newhead.random)
            newhead = newhead.next
        return dictNode[head]
        