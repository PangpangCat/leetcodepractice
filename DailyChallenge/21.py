# 21. Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Example 1:
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
# Example 2:
#
# Input: l1 = [], l2 = []
# Output: []
#
# Example 3:
#
# Input: l1 = [], l2 = [0]
# Output: [0]


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pre = cur = ListNode(0)
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1 or l2:
            cur.next = l1 or l2
        return pre.next
