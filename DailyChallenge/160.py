# 160. Intersection of Two Linked Lists
# Easy


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Solution 1： two point
        p1 = headA
        p2 = headB

        while p1 != p2:
            if p1 == None:
                p1 = headB
            else:
                p1 = p1.next
            if p2 == None:
                p2 = headA
            else:
                p2 = p2.next
        return p1

#N -> length of linked list A
#M -> length of linked list B
# time O(N+M)
# space O(1)

# class Solution(object):
#     def getIntersectionNode(self, headA, headB):
#         """
#         :type head1, head1: ListNode
#         :rtype: ListNode
#         """
#         #solution 2: hashtable
#         nodes_in_B = set()
#         while headB != None:
#             nodes_in_B.add(headB)
#             headB = headB.next
#         while headA != None:
#             if headA in nodes_in_B:
#                 return headA
#             headA = headA.next
#         return None
#
##N -> length of linked list A
#M -> length of linked list B
# time O(N+M)
# space O(M)






# if __name__ == "__main__":
#     headA = ListNode(1)
#     headB = ListNode(2)
#     sol = Solution()
#     print(sol.getIntersectionNode(headA, headB))