# 19. Remove Nth Node From End of List
# Medium
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution(object):
#     def removeNthFromEnd(self, head, n):
#         """
#         :type head: ListNode
#         :type n: int
#         :rtype: ListNode
#         """
#         #Solution 1: Two pass algorithm
#
#         cur = head
#         count = 0
#         while cur != None:
#             count+=1
#             cur = cur.next
#         i = count - n #5-2 = 3
#         sentinel = ListNode(0)
#         sentinel.next = head
#         pre = sentinel
#         count = 0
#         cur = head
#         while cur!=None:
#             if count == i:
#                 if pre == sentinel: #如果删除头结点
#                     sentinel.next = cur.next
#                 pre.next = cur.next
#                 break
#             pre = cur
#             cur = cur.next
#             count+=1 #从第二个开始计数
#         return sentinel.next

# Time complexity : O(L)O(L).
#
# The algorithm makes two traversal of the list, first to calculate list length LL and second to find the (L - n)(L−n) th node.
# There are 2L-n2L−n operations and time complexity is O(L)O(L).
#
# Space complexity : O(1)O(1).
#
# We only used constant extra space.



class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #Solution 2: One pass algorithm
        sentinel = ListNode(0)
        sentinel.next = head
        first = sentinel
        second = sentinel
        for i in range(n):
            first = first.next
        while first.next!= None:
            first = first.next
            second = second.next

        second.next = second.next.next
        return sentinel.next

