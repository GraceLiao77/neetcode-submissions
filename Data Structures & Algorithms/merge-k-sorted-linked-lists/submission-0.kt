/**
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */

class Solution {
    fun mergeKLists(lists: Array<ListNode?>): ListNode? {
        var n = lists.size
        if (n == 0) {
            return null
        }
        if (n == 1) {
            return lists[0]
        }

        var leftList = mergeKLists(lists.take(n / 2).toTypedArray())
        var rightList = mergeKLists(lists.drop(n / 2).toTypedArray())
        
        var dummyNode = ListNode(-1)
        var tail: ListNode = dummyNode
        while (leftList != null && rightList != null) {
            if (leftList.`val` <= rightList.`val`) {
                tail.next = leftList
                leftList = leftList.next
            } else {
                tail.next = rightList
                rightList = rightList.next
            }
            tail = tail.next!!
        }
        while (leftList != null) {
            tail.next = leftList
            leftList = leftList.next
            tail = tail.next!!
        }
        while (rightList != null) {
            tail.next = rightList
            rightList = rightList.next
            tail = tail.next!!
        }
        return dummyNode.next
    }
}
